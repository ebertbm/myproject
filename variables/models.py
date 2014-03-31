from django.db import models

# Create your models here.


class Location(models.Model):
    country = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.country
 
class StudyArea(models.Model):
    name_area = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name_area

class StudyLevel(models.Model):
    name_level = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name_level

class LanguageCourse(models.Model):
    name_language = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name_language

class Information(models.Model):
    info = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name_language