from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SuggestionModel(models.Model):
    suggestion = models.CharField(max_length=240)
    #suggestion_2 = models.CharField(max_length=240)    # evertime you add new model like suggestion_2 you must makemigration 


    def __str__(self):
    #	return str(self.id) + " " + self.suggestion      # return SUGGESTION MODEL created inside the admin interface 
    	return self.suggestion 
		