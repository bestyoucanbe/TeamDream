import sqlite3
from django.contrib.auth.models import User
from ...models import Employee
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from ..connection import Connection


def register_user(request):

    if request.method == 'POST':
        form_data = request.POST

        new_user = User.objects.create_user(
            username=form_data['username'],
            email=form_data['email'],
            password=form_data['password'],
            first_name=form_data['first_name'],
            last_name=form_data['last_name']
        )

        employee = Employee.objects.create(
            department_name=form_data['department_name'],
            user=new_user)

        # Commit the user to the database by saving it
        employee.save()

    return redirect(reverse('teamdreamapp:actionitems'))
