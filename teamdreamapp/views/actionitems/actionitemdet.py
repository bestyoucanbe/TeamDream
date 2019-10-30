import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from teamdreamapp.models import ActionItem
from teamdreamapp.models import model_factory
from ..connection import Connection


def get_actionitem(actionitem_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(ActionItem)
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select 	a.id,
		    a.description,
		    a.start_date,
		    a.finish_date,
		    a.personal_benefit,
		    a.team_benefit,
		    a.presprint_review,
		    a.employee_id,
		    a.itemtype_id,
		    a.sprint_id
            from teamdreamapp_actionitem a
            where a.id = ?
        """, (actionitem_id,))

        # Only 1 record being fetched--therefore using fetchone() method.
        return db_cursor.fetchone()


@login_required
def action_item_details(request, actionitem_id):
    if request.method == 'GET':
        actionitem = get_actionitem(actionitem_id)

        template = 'actionitems/detail.html'
        context = {
            'actionitem': actionitem
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting an action item

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM teamdreamapp_actionitem
                WHERE id = ?
                """, (actionitem_id,))

            return redirect(reverse('teamdreamapp:actionitems'))

        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            # Set the value of presprint review.
            if form_data.get('presprintreview'):
                presprintvalue = True
            else:
                presprintvalue = False

            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE teamdreamapp_actionitem
                SET description = ?,
                    start_date = ?,
                    finish_date = ?,
                    personal_benefit = ?,
                    team_benefit = ?,
                    presprint_review = ?,
                    employee_id = ?,
                    itemtype_id = ?,
                    sprint_id = ?
                WHERE id = ?
                """,
                                  (form_data['description'], form_data['start_date'],
                                   form_data['finish_date'],
                                   form_data['personal_benefit'],
                                   form_data['team_benefit'], presprintvalue,
                                   request.user.employee.id, form_data['actiondescription'],
                                   form_data['sprintdescription'], actionitem_id))

                return redirect(reverse('teamdreamapp:actionitems'))
