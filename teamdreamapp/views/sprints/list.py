import sqlite3
from django.shortcuts import render
from teamdreamapp.models import Sprint
from ..connection import Connection


def sprint_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                s.sprint_name,
                s.start_date,
                s.end_date
            from teamdreamapp_sprint s
            order by s.start_date
            """)

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
