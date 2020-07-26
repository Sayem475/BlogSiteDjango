from django.contrib import admin
from Blog.models import Post, BlogComment
# Register your models here.

admin.site.register((BlogComment))

# for connecting tinyMCE editor 
# its also register the table inside admin.py
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
