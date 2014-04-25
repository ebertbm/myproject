from django.contrib import admin
from accounts.models import UserProfile, ClientProfile, ProductOrder, ClientOrder

admin.site.register(UserProfile)
admin.site.register(ProductOrder)



class OrderInline(admin.TabularInline):
    model = ClientOrder
    extra = 1


class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information',               {'fields': ['user', 'gender']}),
        ('Contact information', {'fields': ['location', 'address', 'zipcode', 'phone'],
                              }),
    ]
    
    inlines = [OrderInline]
    search_fields = ['user']

admin.site.register(ClientProfile, ClientAdmin)

