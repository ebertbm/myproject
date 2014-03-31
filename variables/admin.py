from django.contrib import admin
from variables.models import Location, StudyArea, StudyLevel, LanguageCourse

# Register your models here.

admin.site.register(Location)
admin.site.register(StudyArea)
admin.site.register(StudyLevel)
admin.site.register(LanguageCourse)