#from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone

# ------------------ models for user ----------------------------

class User(models.Model):
    fb_id = models.CharField(max_length=100) #no idea what maxlength is
    gender = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True) # takes a datetime.datetime instance
    location = models.PointField(null=True, blank=False)
    # non-significant fields
    email = models.EmailField(null=True)
    name = models.CharField(max_length=100, null=True)
    def __unicode__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=100, default="")
    creator = models.ForeignKey(User, null=True, related_name='question_created')
    pub_date = models.DateTimeField('date published', default=timezone.now()) # will have to expand this to time published
    flags = models.ManyToManyField(User, blank=True, related_name='question_flagged')
    location = models.PointField(null=True, blank=False)
    def __unicode__(self):
        return self.question_text
    class Meta:
        ordering = ('question_text',)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=100)
    users = models.ManyToManyField(User, blank=True)
    def __unicode__(self):
        return self.text
    class Meta:
        ordering = ('text',)

# makeshift class that details info between a User-Answer connection
# must ensure that there are never two AnswerInfos for a User-Answer connection
class AnswerInfo(models.Model):
    answer = models.ForeignKey(Answer)
    user = models.ForeignKey(User)
    location = models.PointField(null=True, blank=False)
    time = models.DateTimeField('time answered', default=timezone.now())
    def __unicode__(self):
        return self.answer.text

# ------------------ geodjango ----------------------------

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.name
