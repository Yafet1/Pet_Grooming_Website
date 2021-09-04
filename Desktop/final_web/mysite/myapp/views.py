from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login


# Create your views here.
def index(request):
    return render(request, 'home.html')

def chat(request):
    return render(request, 'chat/chat.html')

def room(request, room_name):
    return render(request, 'chat/rooms.html', {
        'room_name': room_name
    })

def rates(request):
    return render(request, 'rates.html')

def meet(request):
    return render(request, 'meet.html')


def service(request):
    if request.method == "POST":
        suggestion_form = forms.SuggestionForm(request.POST)
       # if suggestion_form.is_valid():
            # save the data 
        #    suggestion_form.save()
         #   suggestion_form = forms.SuggestionForm()

        if request.user.is_authenticated:
            if suggestion_form.is_valid():
                suggestion_form.save(request)
                suggestion_form = forms.SuggestionForm()

    else:
        suggestion_form = forms.SuggestionForm()
        
    content = models.SuggestionModel.objects.all()
    context = {
    "body":"Body",
    #"list":content,
    "form":suggestion_form,
    }
    return render(request,'service.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/login/')



def register_view(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            user = form_instance.save()
            # login(request, user)
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()

    context = {
        "title":"Registration",
        "form":form_instance
    }

    return render(request, "registration/register.html", context=context)   








    


