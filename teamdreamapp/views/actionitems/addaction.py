import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from ..connection import Connection


@login_required
def action_item_addaction(request):

    if request.method == 'POST':
        form_data = request.POST

    # Set the value of presprint review.
    if form_data.get('presprintreview'):
        presprintvalue = True
    else:
        presprintvalue = False

    # Set the value of start date
    if form_data.get('start_date'):
        startdatevalue = form_data.get('start_date')
    else:
        startdatevalue = null

    # Set the value of finish date
    if form_data.get('presprintreview'):
        presprintvalue = True
    else:
        presprintvalue = False

    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO teamdreamapp_actionitem
        (
            description, start_date, finish_date,
            personal_benefit, team_benefit, presprint_review, employee_id,itemtype_id, sprint_id
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
                          (form_data['description'], form_data['start_date'],
                           form_data['finish_date'],
                           form_data['personal_benefit'],
                           form_data['team_benefit'], presprintvalue,
                           request.user.employee.id, form_data['actiondescription'],
                           form_data['sprintdescription']))

        return redirect(reverse('teamdreamapp:actionitems'))
