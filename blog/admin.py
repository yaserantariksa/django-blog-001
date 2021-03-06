from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','author','published_date','status')
    prepopulated_fields = {
        "slug":("title",),
    }
    search_fields = ("title","status")

admin.site.register(models.Category)

admin.site.register(models.Comment, MPTTModelAdmin)