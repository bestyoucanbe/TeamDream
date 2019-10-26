import sqlite3
from django.contrib.auth.models import User
from ...models import Employee
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import render
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

    # send them the url for where it should go after executing the above code
    return redirect(reverse('teamdreamapp:actionitems'))
