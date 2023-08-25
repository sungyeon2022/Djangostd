from django.contrib import admin
from .models import Qs,Aw

class QsAdmin(admin.ModelAdmin):
    search_fields = ['sbj']

class AwAdmin(admin.ModelAdmin):
    search_fields= ['con']

admin.site.register(Qs,QsAdmin)
admin.site.register(Aw,AwAdmin)
# Register your models here.
