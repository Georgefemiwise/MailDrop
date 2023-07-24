from django.contrib import admin
from . models import Company, Contact
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display =['name',]
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =['phone',]

