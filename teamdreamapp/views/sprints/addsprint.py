import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from ..connection import Connection


@login_required
def add_sprint(request):

    if request.method == 'POST':
        form_data = request.POST

    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO teamdreamapp_sprint
        (
            sprint_name, start_date, end_date
        )
        VALUES (?, ?, ?)
        """,
                          (form_data['sprintname'], form_data['startdate'],
                           form_data['enddate']))

        return redirect(reverse('teamdreamapp:sprintlist'))
