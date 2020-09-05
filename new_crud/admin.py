from django.contrib import admin
from .models import *

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'location', 'date_created']


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'creator','paradigm', 'date_created']


class ProgrammerAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'age', 'company']


admin.site.register(Person)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Programmer, ProgrammerAdmin)
