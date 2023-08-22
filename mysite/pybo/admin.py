from django.contrib import admin
from .models import Qs

class QsAdmin(admin.ModelAdmin):
    search_fields = ['sbj']

admin.site.register(Qs,QsAdmin)
# Register your models here.
