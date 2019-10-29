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
			a.employee_id,
			a.itemtype_id,
			a.sprint_id
        FROM teamdreamapp_actionitem a
        WHERE a.id = ?
        """, (actionitem_id,))

        return db_cursor.fetchone()


def get_itemtypes():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(ItemType)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select 	i.id,
       			i.action_desc
        from teamdreamapp_itemtype i
        """)

        return db_cursor.fetchall()


def get_sprints():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Sprint)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select 	s.id,
     			s.sprint_name,
     			s.start_date,
     			s.end_date
        from teamdreamapp_sprint s
        """)

        return db_cursor.fetchall()


@login_required
def actionitem_edit_form(request, actionitem_id):

    if request.method == 'GET':
        actionitem = get_actionitem(actionitem_id)
        itemtypes = get_itemtypes()
        sprints = get_sprints()

        template = 'actionitems/editform.html'
        context = {
            'actionitem': actionitem,
            'itemtypes': itemtypes,
            'sprints': sprints
        }

        return render(request, template, context)
