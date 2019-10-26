from django.conf.urls import url
from .views import *

app_name = "teamdreamapp"

urlpatterns = [
    url(r'^$', action_item_list, name='home'),
    url(r'^actionitems$', action_item_list, name='actionitems'),
    # The following url takes you to the register_user method in views/auth/registration.py file.
    url(r'^register$', register_user, name='register'),
    # The following url takes you to the register_form method in views/auth/registerform.py file.
    url(r'^register/form$', register_form, name='registerform'),
    # The following url takes you to the action_item_addform method in views/actionitems/addform.py file.
    url(r'^actionitems/addform$', action_item_addform, name='actionitem_addform'),
    # The following url takes you to the sprint_addform method in views/sprints/addform.py file.
    url(r'^sprints/addform$', sprint_addform, name='sprint_addform'),
]
