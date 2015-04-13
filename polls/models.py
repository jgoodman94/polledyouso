from django.db import models
from django.utils import timezone

class User(models.Model):
    fb_id = models.CharField(max_length=100) #no idea what maxlength is
    #does user have anything else?
    def __unicode__(self):
        return self.fb_id

class Question(models.Model):
    text = models.CharField(max_length=100, default="")
    #creator = models.ForeignKey(User, defaul)
    pub_date = models.DateTimeField('date published', default=timezone.now()) # will have to expand this to time published
    pub_loc = models.CharField(max_length=40, blank=True, verbose_name="location") # use GeoDjango

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ('text',)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=100)
    users = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ('text',)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		return self.user.username