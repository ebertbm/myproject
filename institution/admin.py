from django.contrib import admin
from institution.models import Institution


class PostAdmin(admin.ModelAdmin):
	list_display = ['name_institution', 'location']
	list_filter = ['created']
	search_fields = ['name_institution', 'location']
	date_hierarchy = 'created'
	save_on_top = True
	save_as = True
	prepopulated_fields = {"slug": ("name_institution",)}


admin.site.register(Institution, PostAdmin)
