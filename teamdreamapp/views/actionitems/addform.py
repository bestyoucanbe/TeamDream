import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from teamdreamapp.models import ItemType, Sprint
from ..connection import Connection

# This view takes you to the action item addition form.
# The actionitems/addform.html is the template containing the form.


def action_item_addform(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # The following section is to get the itemtypes (action descriptions)

        user = request.user

        db_cursor.execute("""
        select
            i.id,
            i.action_desc,
            i.employee_id
            from teamdreamapp_itemtype i
            join teamdreamapp_employee e ON e.id = i.employee_id
            where e.user_id = ?
        """, (user.id,))

        all_itemtypes = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            itemtype = ItemType()
            itemtype.id = row['id']
            itemtype.action_desc = row['action_desc']

            all_itemtypes.append(itemtype)

        # The following section is to get the sprints

        db_cursor.execute("""
            select
                s.id,
                s.sprint_name,
                s.start_date,
                s.end_date,
                s.employee_id
            from teamdreamapp_sprint s
           	join teamdreamapp_employee e ON e.id = s.employee_id
           	where e.user_id = ?
            order by s.start_date
            """, (user.id,))

        all_sprints = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            sprint = Sprint()
            sprint.id = row['id']
            sprint.sprint_name = row['sprint_name']
            sprint.start_date = row['start_date']
            sprint.end_date = row['end_date']

            all_sprints.append(sprint)

    template = 'actionitems/addform.html'

    # Sending both itemtypes (action descriptions) and sprints to the form.
    context = {
        'all_itemtypes': all_itemtypes,
        'all_sprints': all_sprints
    }

    return render(request, template, context)
