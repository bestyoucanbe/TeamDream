import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from ..connection import Connection


@login_required
def add_itemtype(request):

    if request.method == 'POST':
        form_data = request.POST

    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO teamdreamapp_itemtype
        (
            action_desc,
            employee_id
        )
        VALUES (?, ?)
        """,
                          (form_data['actiondesc'], request.user.employee.id))

        return redirect(reverse('teamdreamapp:itemtypelist'))
