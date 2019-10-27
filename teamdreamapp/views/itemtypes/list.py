import sqlite3
from django.shortcuts import render
from teamdreamapp.models import ItemType
from ..connection import Connection


def itemtype_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                i.action_desc
            from teamdreamapp_itemtype i
            """)

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
