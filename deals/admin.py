from django.contrib import admin
from deals.models import Deal


class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'institution', 'active']
	list_filter = ['created']
	search_fields = ['title']
	date_hierarchy = 'created'
	save_on_top = True
	save_as = True
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Deal, PostAdmin)
