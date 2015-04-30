from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from polls.models import *
from django.db.models import Q
import json
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.views.decorators.csrf import ensure_csrf_cookie

from django.contrib.gis.geos import *
from django.contrib.gis.measure import D

from datetime import *

def index(request):
    return render(request, 'polls/static_index.html')

def f(request):
    return render(request, 'polls/facebook.html')

def answeredqs(request, qlist):
    return render(request, 'polls/answeredqs.html', {'qlist':qlist})

# ---------------------- ajax site views ------------------------------

# function used in ajax views to return the next 50 questions relevant
# to user, NOT A VIEW.
def getQuestions(user_pk):
    questions = []
    try:
        user = User.objects.get(pk=user_pk)
    # in the case of the user not existing
    except:
        return questions
# get 50 closest questions ---------------
    #search_radius = 20 
    #current_location = user.location

    #qs = Question.objects.filter(location__distance_lte=(current_location, D(m=search_radius)))\
    #    .distance(current_location).order_by('distance')
# ----------------------------------------
    qs = Question.objects.order_by('-pub_date') # this will be relative to the user's location
    for each in user.answer_set.all():
        qs = qs.exclude(pk=each.question.pk) 
    count = 0
    for q in qs:
        # add questions that user has not already answered
        #if user.answer_set.filter(question=q).count() == 0:
        questions.append(q)
        count+=1
        # specifies number of unanswered questions to return
        if count >= 3:
            break
    return questions
    #Question.objects.order_by('-pub_date')[:5]

@csrf_exempt
def flag_question(request):
    return HttpResponse(json.dumps({'a':'a'}))

@csrf_exempt
def get_questions(request):
    if request.method == 'POST':
        user_pk = int(request.POST.get('user_pk'))
        # get user-relevant questions
        questions = getQuestions(user_pk)
        #questions = Question.objects.order_by('-pub_date')[:2]

        data = {}
        for q in questions:
            # create json
            dat = {}
            dat['question'] = q.question_text
            answers = q.answer_set.all()
            a = []
            for answer in answers:
                n = (answer.pk, answer.text)
                a.append(n)
            dat['answers'] = a
            data[q.pk] = dat
    else:
        data = {'error': 'this was not a POST request'}

    return HttpResponse(json.dumps(data))

def getAge(user):
    birth_date = user.birthday
    days_in_year = 365.2425    
    return int((date.today() - birth_date).days / days_in_year)

@csrf_exempt
def get_data(request):
    if request.method == 'POST':
        try:
            answer_pk = request.POST.get('answer_pk')
            q = Answer.objects.get(pk=answer_pk).question

            array = []
            for a in q.answer_set.all():
                obj = {}
                obj['answer'] = a.text
                obj['frequency'] = a.users.count()
                obj['maleFrequency'] = a.users.count()/2
                obj['femaleFrequency'] = a.users.count()/2
                ageArray = []
                for each in range(1,8):
                    ageArray.append(a.users.count()/8)
                obj['ageFreqs'] = ageArray
                array.append(obj)

            data = {'answers':array}
        except:
            data = {'error':'we couldn\'t find your question'}
    else:
        data = {'error': 'this was not a POST request'}
          
    return HttpResponse(json.dumps(data))

@csrf_exempt
def save_user(request):
    if request.method == 'POST':
        info = json.loads(request.POST.get('info'))
        fb_id = int(info['id'])
        name =  info['name']
        gender = info['gender']
        birthday = datetime.strptime(info['birthday'], "%m/%d/%Y")
        #email = info['email']
        lat = float(info['lat'])
        lng = float(info['lng'])

        #return HttpResponse(json.dumps({'bday':birthday.strftime('%m %d, %Y')}))

        try:
            if User.objects.filter(fb_id=fb_id).count() == 0:
                new_user = User(fb_id=fb_id, name=name, gender=gender, \
                    birthday=birthday, location=Point(lat,lng))
                new_user.save()
                data = {'success': 'new user created', 'user_pk': new_user.pk}
            else:
                try:
                    user = User.objects.get(fb_id=fb_id)
                    data = {'success': 'user info retrieved', 'user_pk': user.pk}
                except:
                    {'error': 'we have more than one representation of this user in the database'}
        except:
            data = {'error': 'user couldn\'t be saved (something is probably wrong with fb info sent)'}
    else:
        data = {'error': 'this was not a POST request'}

    return HttpResponse(json.dumps(data))

@csrf_exempt
def save_question(request):
    #return HttpResponse(json.dumps({"ahh":"ahh"}))
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        answers = json.loads(request.POST.get('answers'))
        user_pk = request.POST.get('user_pk')
        # lat = float(json.loads(request.POST.get('lat')))
        # lon = float(json.loads(request.POST.get('lon')))

        # checks for equivalence of text; could also do answers.
        if Question.objects.filter(question_text=question_text).count() > 0:
            return HttpResponse(json.dumps({'error': 'this question is already in our database'}))
        # -------------------------------------
        # perform some field checking, e.g. the question can't already exist (or can it?)
        # -------------------------------------
        # save the question to the database (checking of fields done on front end)
        try:
            user = User.objects.get(pk=1)
            q = Question(question_text=question_text, location=user.location)
            q.save()
            for answer in answers:
                a = Answer(question=q, text=answer)
                a.save()
            #data = {'success': 'your question was saved to the database'}
            data = {'success': 'this question was saved at {0} to {1}'.format(user.location, user.name)}
        except:
            data = {'error': 'your question couldn\'t be saved to the database'}
    else:
        data = {'error': 'this was not a POST request'}

    return HttpResponse(json.dumps(data))

@csrf_exempt
def save_answers(request):
    if request.method == 'POST':
        user_pk = int(request.POST.get('user_pk')) 
        answer_pks = json.loads(request.POST.get('answer_pks'))

        errors = {}
        user = User.objects.get(pk=user_pk)

        for pk in answer_pks:
            answer_pk = int(pk[1])
            try:
                answer = Answer.objects.get(pk=answer_pk)
                # check user has not already answered this question
                try:
                    user.answer_set.get(pk=a.pk)
                    raise Exception('you have already answered this question')
                except:
                    pass
                    #return HttpResponse(json.dumps({"answer": answer.text}))
                    # all is well, add to database
                    if user.answer_set.filter(question=answer.question).count()==0:
                        #and AnswerInfo.objects.filter(user=user,answer=answer).count() == 0:
                        answer.users.add(user)
                        # NEED TO INCLUDE TIMESTAMP FROM AJAX
                        AnswerInfo(answer=answer,user=user).save() # time set to now by default
                    else:
                        errors[answer_pk] = "question is already in our database"

            except Exception as err:
                # do I want to keep going like this? or stop?
                errors[answer_pk] = err
        if len(errors) == 0:
            data = {'success': 'all answers were recorded in the database'}
        else:
            data = {'error': 'several questions were not recorded in the database', 'errors_by_index': errors}
    else:
        data = {'error': 'this was not a POST request'}

    return HttpResponse(json.dumps(data))

# ---------------------- test site views ------------------------------
def create_user(request):
    return render(request, 'test/createuser.html')

# ---------------- antiquated non-ajax site views ---------------------
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/index.html', {'q':question})

def submitq(request):
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!
    errors = []
    if 'q' in request.GET:
        # filter out end and multiple spaces
        q = ' '.join(request.GET['q'].split())
        a1 = ' '.join(request.GET['a1'].split())
        a2 = ' '.join(request.GET['a2'].split())
        a3 = ' '.join(request.GET['a3'].split())
        a4 = ' '.join(request.GET['a4'].split())
        a5 = ' '.join(request.GET['a5'].split())

        message = "question submitted (good work bae)"
        if not q:
            errors.append("you need to type a question bae!")
        if not (a1 and a2):
            errors.append("you need at least two answers bae!")

        if errors != []:
            message = "question not submitted (bad work bae!)"
        else:
            # submit question to database
            savedq = Question(text=q)
            savedq.save()
            a = Answer(question=savedq, text=a1)
            a.save()
            a =Answer(question=savedq, text=a2)
            a.save()
            if a3:
                a = Answer(question=savedq, text=a3)
                a.save()
            if a4:
                a = Answer(question=savedq, text=a4)
                a.save()
            if a5:
                a = Answer(question=savedq, text=a5)
                a.save()

        # now missing this view, 'submitq.html', because i accidentally deleted it. 
        return render(request, 'polls/submitq.html', {"message":message, "errors": errors})

def answered(request, question_id, answer_id):
    question = Question.objects.get(pk=question_id)
    a = question.answer_set.get(pk=answer_id) #doesn't allow non-distinct sets of answers
    user = User.objects.first()
    a.users.add(user)
    a.save()
    return render(request, 'polls/answered.html', {'q':question, 'a':a})
