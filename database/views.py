from operator import is_
import re
import bcrypt
from django.shortcuts import render, redirect
from django.http import HttpResponse

from database.utils.JwtAuth import JwtAuth

from . import models
from . import forms

from uuid import uuid4
import json

# Create your views here.
def database_register(request):
    if request.method == 'POST':
        form = request.POST


        if form:
            if models.User.objects.filter(email=form['email']).exists():
                return HttpResponse('User already exists', status=400)
            
            
            hashed_password = bcrypt.hashpw(str(form['password']).encode('utf-8'), bcrypt.gensalt(rounds=8))

            user = models.User(
                        name=form['nickname'],
                        email=form['email'],
                        password=hashed_password,
                    )
            
            user.save()
            return HttpResponse('User registered', status=200)
        return HttpResponse('Invalid form', status=400)
    else:
        return HttpResponse('Invalid request method', status=400)

def database_login(request):
    form = request.POST

    if form:
        # 1. Busca o usuário uma única vez
        user = models.User.objects.filter(email=form['email']).first()

        if user:
            database_password_hash = user.password
            input_password = form['password'].encode('utf-8')

            # 4. Comparação (Assumindo que input_hash deve ser igual a user.password)
            if bcrypt.checkpw(input_password, database_password_hash):
                return HttpResponse('Password Ok')
            
            return HttpResponse('wrong password')
        
        return HttpResponse('user not found')
    
    return HttpResponse('Invalid request method', status=400)