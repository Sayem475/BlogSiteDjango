from django.contrib import admin
from .models import Contact, design, FAQ, htmlchapters, htmldescription, csschapters,cssdescription, jschapters,jsdescription, pychapters,pydescription,djchapters,djdescription

# Register your models here.
admin.site.register((Contact,FAQ, design, htmlchapters, csschapters, jschapters, pychapters,djchapters))


@admin.register(htmldescription,cssdescription,jsdescription,pydescription,djdescription)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)





