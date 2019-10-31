import sqlite3
import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from ...models import Employee
from django.urls import reverse
from django.shortcuts import render, redirect
from ..connection import Connection


def register_user(request):

    if request.method == 'POST':
        # set up the form_data variable
        form_data = request.POST

        # use the Django default create_user method to create an entry in the User table
        new_user = User.objects.create_user(
            username=form_data['username'],
            email=form_data['email'],
            password=form_data['password'],
            first_name=form_data['first_name'],
            last_name=form_data['last_name']
        )

        # also create a record in the employee table
        employee = Employee.objects.create(
            department_name=form_data['department_name'],
            user=new_user)

        authenticated_user = authenticate(
            username=form_data['username'], password=form_data['password'])

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            # send them the url for where it should go after executing the above code
            return redirect(reverse('teamdreamapp:home'))

        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {}, {}".format('username', 'password'))
            return HttpResponse("Invalid login details supplied.")
