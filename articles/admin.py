from django.contrib import admin
from .models import Tag, Classification, Article
# Register your models here.
admin.site.register(Tag)
admin.site.register(Classification)

class ArticleAdmin(admin.ModelAdmin):
      class Media:

         js = (

         'tinymce/tinymce.min.js',
         'tinymce/config.js',

         )

         

admin.site.register(Article,ArticleAdmin)