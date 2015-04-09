from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

#  "python manage.py makemigrations polls"
#  "python manage.py sqlmigrate polls 0001"
#  "python manage.py migrate"
#  "python manage.py syncdb"

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):              # __unicode__ on Python 2
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.choice_text

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		return self.user.username