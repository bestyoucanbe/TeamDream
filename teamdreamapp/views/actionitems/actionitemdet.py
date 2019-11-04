import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from teamdreamapp.models import ActionItem, ItemType, Sprint
from teamdreamapp.models import model_factory
from ..connection import Connection


def get_actionitemplus(actionitem_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(ActionItem)
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select 	a.id a2,
		    a.description,
		    a.start_date,
		    a.finish_date,
		    a.personal_benefit,
		    a.team_benefit,
		    a.presprint_review,
		    a.itemtype_id,
		    a.sprint_id,
		    i.id i2,
		    i.action_desc,
		    s.id s2,
		    s.sprint_name
            from teamdreamapp_actionitem a
            join teamdreamapp_itemtype i ON a.itemtype_id = i.id
            join teamdreamapp_sprint s ON a.sprint_id = s.id
            where a.id = ?
        """, (actionitem_id,))

        # Only 1 record being fetched--therefore using fetchone() method.
        return db_cursor.fetchone()


@login_required
def action_item_details(request, actionitem_id, whichlist):
    if request.method == 'GET':
        actionitemplus = get_actionitemplus(actionitem_id)

        # Convert the boolean value for the pre-sprint review into a human readable value.
        if actionitemplus.presprint_review == 1:
            presprint_value = "Yes"
        else:
            presprint_value = "No"

        template = 'actionitems/detail.html'
        context = {
            'actionitemplus': actionitemplus,
            'whichlist': whichlist,
            'presprint_value': presprint_value
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

            if whichlist == "all":
                return redirect(reverse('teamdreamapp:actionitems'))
            elif whichlist == "completed":
                return redirect(reverse('teamdreamapp:actionitemscompleted'))
            elif whichlist == "presprintreview":
                return redirect(reverse('teamdreamapp:actionitemspresprint'))

        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            # Convert the checkbox value into a boolean value.
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
                    itemtype_id = ?,
                    sprint_id = ?
                WHERE id = ?
                """,
                                  (form_data['description'], form_data['start_date'],
                                   form_data['finish_date'],
                                   form_data['personal_benefit'],
                                   form_data['team_benefit'], presprintvalue,
                                   form_data['actiondescription'],
                                   form_data['sprintdescription'], actionitem_id))

                if whichlist == "all":
                    return redirect(reverse('teamdreamapp:actionitems'))
                elif whichlist == "completed":
                    return redirect(reverse('teamdreamapp:actionitemscompleted'))
                elif whichlist == "presprintreview":
                    return redirect(reverse('teamdreamapp:actionitemspresprint'))
