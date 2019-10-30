import sqlite3
from django.shortcuts import render
from teamdreamapp.models import ActionItem
from ..connection import Connection


def action_item_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            user = request.user

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
                join teamdreamapp_employee e ON e.id = a.employee_id
                where e.user_id = ?
            """, (user.id,))

            all_actions = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                action = ActionItem()
                action.id = row['id']
                action.description = row['description']
                action.start_date = row['start_date']
                action.finish_date = row['finish_date']
                action.personal_benefit = row['personal_benefit']
                action.team_benefit = row['team_benefit']
                action.presprint_review = row['presprint_review']
                action.employee_id = row['employee_id']
                action.itemtype_id = row['itemtype_id']
                action.sprint_id = row['sprint_id']

                all_actions.append(action)

        template = 'actionitems/list.html'
        context = {
            'all_actions': all_actions
        }

        return render(request, template, context)
