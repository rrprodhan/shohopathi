from django.shortcuts import render
#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import CreateView #CreateView class displays a form for creating an object,
from . import forms           #redisplaying the form with validation errors (if there are any) and saving the object.


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    #Using reverse_lazy instead of reverse because it will activate only if submit button is pressed after filling up form
    success_url = reverse_lazy('login') #reverse lazy will only ativate after clicking the submit button on form
    template_name = 'accounts/signup.html' #template_name will show the page defined inside quotations
