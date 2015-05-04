from polls.models import *

users = User.objects.all()

for user in users:
    for each in user.answer_set.all():
        each.users.remove(user)