from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.SuggestionModel)   # register that in the admin interface 
