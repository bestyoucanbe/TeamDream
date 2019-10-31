import sqlite3
from django.shortcuts import render
from teamdreamapp.models import Sprint
from ..connection import Connection


def sprint_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            user = request.user

            db_cursor.execute("""
            select
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
                sprint.sprint_name = row['sprint_name']
                sprint.start_date = row['start_date']
                sprint.end_date = row['end_date']

                all_sprints.append(sprint)

        template = 'sprints/list.html'
        context = {
            'all_sprints': all_sprints
        }

        return render(request, template, context)
