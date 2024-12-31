from operator import is_
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse

from database.utils.HashUtils import HashUtils
from database.utils.JwtAuth import JwtAuth

from . import models
from . import forms

from uuid import uuid4
import json

# Create your views here.
def database_register(request):
    if request.method == 'POST':
        form = forms.UserSignInForm(request.POST)

        if form.is_valid():
            if models.User.objects.filter(email=form['email']).exists():
                return HttpResponse('User already exists', status=400)
            
            
            hash_n_salt = HashUtils().generate_n_hash(form.cleaned_data['password'])

            user = models.User(
                        name=form.cleaned_data['name'],
                        email=form.cleaned_data['email'],
                        password=hash_n_salt['password'],
                        salt=hash_n_salt['salt']
                    )
            
            user.save()
            return HttpResponse('User registered', status=200)
        return HttpResponse('Invalid form', status=400)
    else:
        return HttpResponse('Invalid request method', status=400)