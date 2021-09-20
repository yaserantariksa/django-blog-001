from django.contrib import admin
from . import models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','published_date','status')

# Register your models here.
admin.site.register(models.Post,AuthorAdmin)