from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from . import models 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields


def must_end_zero(value):
	if not value.endswith("0"):
		raise forms.ValidationError("Must end with zero")
	return value

def must_be_int(value): 
    if value.isdigit()==False:
        raise ValidationError('Must be a number')
    return value
	

def must_be_capitalized(value):
    if value != value.capitalize():
        raise ValidationError('First letter is not capitalized try again')
    return value
    
def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email Already Exists")
    return value    


class SuggestionForm(forms.Form):
	suggestion_field = forms.CharField(
		label="Enter your name (make you first letter capitalized)",
		required=True,
		max_length=50, 
		validators=[must_be_capitalized]
	)

	suggestion_field_2 = forms.CharField(
		label="Enter your email ",
		required=True,
		max_length=50, 
		validators=[validate_email]
	)
	suggestion_field_3 = forms.CharField(
		label="What breed of pet do you have ",
		required=True,
		max_length=50, 
		validators=[must_be_capitalized]
	) 
	suggestion_field_4 = forms.CharField(
		label="How much does your pet weight in lbs ",
		required=True,
		max_length=50, 
		validators=[must_be_int]
	) 


	#def save (self):
	def save (self,request):

		suggestion_instance = models.SuggestionModel()
		suggestion_instance.suggestion = self.cleaned_data["suggestion_field"]
		suggestion_instance.author = request.user
		#suggestion_instance.suggestion = self.cleaned_data["suggestion_field_1"]
		suggestion_instance.save()
		return suggestion_instance



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user



        


