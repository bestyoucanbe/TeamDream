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
]
