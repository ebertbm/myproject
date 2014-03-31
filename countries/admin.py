from django.contrib import admin
from countries.models import Country, CountryGallery





class GalleryInline(admin.TabularInline):
    model = CountryGallery
    extra = 1


class PostAdmin(admin.ModelAdmin):
	list_display = ['title','active']
	list_filter = ['created']
	search_fields = ['title']
	date_hierarchy = 'created'
	save_on_top = True
	save_as = True
	inlines = [GalleryInline]
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Country, PostAdmin)