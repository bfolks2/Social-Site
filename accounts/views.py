from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from accounts import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') #reverse_lazy will not execute until the Submit button is clicked.  reverse would execute immediately as the view opened
    template_name = 'accounts/signup.html'
