from haystack import indexes
from .models import Institution


class InstitutionIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	type_institution = indexes.CharField(model_attr='type_institution', faceted=True)
	location = indexes.CharField(model_attr='location', faceted=True)
	levels = indexes.MultiValueField(faceted=True)
	languages = indexes.MultiValueField(faceted=True)
	areas = indexes.MultiValueField()
	
	
	def get_model(self):
		return Institution
	
	def index_queryset(self, using=None):
		return self.get_model().objects.all()

	def prepare_levels(self, obj):
		return [(p.name_level) for p in obj.level_study.all()]


	def prepare_languages(self, obj):
		return [(p.name_language) for p in obj.course_language.all()]		
		
	def prepare_areas(self, obj):
		return [(p.name_area) for p in obj.study_area.all()]

	def prepare_type_institution(self, obj):
		return obj.get_type_institution_display()