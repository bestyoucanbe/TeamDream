import sqlite3
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from teamdreamapp.models import ActionItem, ItemType, Sprint
from teamdreamapp.models import model_factory
from ..connection import Connection


def get_actionitem(actionitem_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(ActionItem)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
			a.description,
			a.start_date,
			a.finish_date,
			a.personal_benefit,
			a.team_benefit,
			a.presprint_review,
			a.itemtype_id,
			a.sprint_id
        FROM teamdreamapp_actionitem a
        WHERE a.id = ?
        """, (actionitem_id,))

        return db_cursor.fetchone()


def get_itemtypes(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(ItemType)
        db_cursor = conn.cursor()

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

        return db_cursor.fetchall()


def get_sprints(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Sprint)
        db_cursor = conn.cursor()

        user = request.user

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

        return db_cursor.fetchall()


@login_required
def actionitem_edit_form(request, actionitem_id, whichlist):

    if request.method == 'GET':
        actionitem = get_actionitem(actionitem_id)
        all_itemtypes = get_itemtypes(request)
        all_sprints = get_sprints(request)

        template = 'actionitems/editform.html'
        context = {
            'actionitem': actionitem,
            'all_itemtypes': all_itemtypes,
            'all_sprints': all_sprints,
            'whichlist': whichlist
        }

        return render(request, template, context)
