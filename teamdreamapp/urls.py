from django.conf.urls import url
from django.urls import path
from .views import *

app_name = "teamdreamapp"

urlpatterns = [
    url(r'^$', action_item_list, name='home'),
    url(r'^actionitems$', action_item_list, name='actionitems'),
    # The following url takes you to the register_user method in views/auth/registration.py file.
    url(r'^register$', register_user, name='register'),
    # The following url takes you to the register_form method in views/auth/registerform.py file.
    url(r'^register/form$', register_form, name='registerform'),
    # The following url takes you to the sprint_addform method in views/sprints/addform.py file.
    url(r'^sprints/addform$', sprint_addform, name='sprintaddform'),
    # The following url takes you to the add_sprint method in views/sprints/addsprint.py file.
    url(r'^addsprint$', add_sprint, name='addsprint'),
    # The following url takes you to the sprint_list method in views/sprints/list.py file.
    url(r'^sprints/list$', sprint_list, name='sprintlist'),
    # The following url takes you to the itemtype_addform method in views/itemtypes/additemform.py file.
    url(r'^itemtypes/addform$', itemtype_addform, name='itemtypeaddform'),
    # The following url takes you to the add_itemtype method in views/itemtypes/additemtype.py file.
    url(r'^additemtype$', add_itemtype, name='additemtype'),
    # The following url takes you to the itemtype_list method in views/itemtypes/list.py file.
    url(r'^itemtypes/list$', itemtype_list, name='itemtypelist'),
    # The following url takes you to the action_item_addform method in views/actionitems/addform.py file.
    url(r'^actionitems/addform$', action_item_addform, name='actionitemaddform'),
    # The following url takes you to the action_item_addaction method in views/actionitems/addaction.py file.
    url(r'^actionitems/addaction$', action_item_addaction,
        name='actionitemaddaction'),
    # The following url takes you to the action_item_details method in views/actionitems/actionitemdet.py file
    path('actionitem/<int:actionitem_id>',
         action_item_details, name='actionitem'),
    url(r'^actionitems/(?P<actionitem_id>[0-9]+)/form$',
        actionitem_edit_form, name='actionitem_edit_form'),
]
