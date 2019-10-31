import sqlite3
from django.shortcuts import render
from teamdreamapp.models import ItemType
from ..connection import Connection


def itemtype_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            user = request.user

            db_cursor.execute("""
            select
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
                itemtype.action_desc = row['action_desc']

                all_itemtypes.append(itemtype)

        template = 'itemtypes/list.html'
        context = {
            'all_itemtypes': all_itemtypes
        }

        return render(request, template, context)
