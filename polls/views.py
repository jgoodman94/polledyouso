from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.template import RequestContext

from polls.form import UserForm, UserProfileForm

from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter

from config import CONFIG

from polls.models import *

authomatic = Authomatic(CONFIG, 'a super secret random string')

def index(request):
    question = Question.objects.order_by('-pub_date').first()
    return render(request, 'polls/index.html', {'q':question})

def detail(request, question_id):
    if 'uans' in request.GET:
        return HttpResponse("AHAH")
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/index.html', {'q':question})

def submitq(request):
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        a1 = request.GET['a1']
        a2 = request.GET['a2']
        a3 = request.GET['a3']
        a4 = request.GET['a4']
        a5 = request.GET['a5']

        message = "question submitted (good work bae)"
        if not q:
            errors.append("you need to type a question bae!")
        if not (a1 and a2):
            errors.append("you need at least two answers bae!")

        if errors != []:
            message = "question not submitted"
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
            
        return render(request, 'polls/submitq.html', {"message":message, "errors": errors})

def answered(request, question_id, question_answer):
    question = Question.objects.get(pk=question_id)
    a = question.answer_set.get(text=question_answer) #doesn't allow non-distinct sets of answers
    user = User.objects.first()
    a.users.add(user)
    a.save()
    return render(request, 'polls/answered.html', {'q':question, 'a':question_answer})

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {'question': p,'error_message': "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def registerI(request):
	# Like before, get the request's context.
	context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
	registered = False

    # If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
			user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
			profile.save()

            # Update our variable to tell the template registration was successful.
			registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
		else:
			print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

    # Render the template depending on the context.
	return render_to_response('polls/registerI.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},context)

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/polls/")
	else:
		form = UserCreationForm()
	return render(request, "polls/register.html", {
        'form': form,
    })

def login(request, provider_name):
    # We we need the response object for the adapter.
	response = HttpResponse()
    
    # Start the login procedure.
	result = authomatic.login(DjangoAdapter(request, response), provider_name)
     
    # If there is no result, the login procedure is still pending.
    # Don't write anything to the response if there is no result!
	if result:
        # If there is result, the login procedure is over and we can write to response.
		response.write('<a href="..">Home</a>')
        
		if result.error:
            # Login procedure finished with an error.
			response.write('<h2>Damn that error: {0}</h2>'.format(result.error.message))
        
		elif result.user:
            # Hooray, we have the user!
            
            # OAuth 2.0 and OAuth 1.0a provide only limited user data on login,
            # We need to update the user to get more info.
			if not (result.user.name and result.user.id):
				result.user.update()
            
            # Welcome the user.
			response.write(u'<h1>Hi {0}</h1>'.format(result.user.name))
			response.write(u'<h2>Your id is: {0}</h2>'.format(result.user.id))
			response.write(u'<h2>Your email is: {0}</h2>'.format(result.user.email))
            
            # Seems like we're done, but there's more we can do...
            
            # If there are credentials (only by AuthorizationProvider),
            # we can _access user's protected resources.
			if result.user.credentials:
                
                # Each provider has it's specific API.
				if result.provider.name == 'fb':
					response.write('Your are logged in with Facebook.<br />')
                    
                    # We will access the user's 5 most recent statuses.
					url = 'https://graph.facebook.com/{0}?fields=feed.limit(5)'
					url = url.format(result.user.id)
                    
                    # Access user's protected resource.
					access_response = result.provider.access(url)
                    
					if access_response.status == 200:
                        # Parse response.
						#statuses = access_response.data.get('feed').get('data')
						#error = access_response.data.get('error')
						response.write('Your are logged in with Facebook.<br />')
					else:
						response.write('Damn that unknown error!<br />')
						response.write(u'Status: {0}'.format(response.status))
	return response