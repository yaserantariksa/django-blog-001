from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','published_date','status')
    prepopulated_fields = {
        "slug":("title",),
    }
    search_fields = ("title","status")
@admin.register(models.Comment)
class Comments(admin.ModelAdmin):
    list_display = ('post','name','email','publish','status')
    list_filter = ("status","publish")
    search_fields = ("name","email","content")

# Register your models here.
# admin.site.register(models.Post,AuthorAdmin)
# admin.site.register(models.Comment,Comments)