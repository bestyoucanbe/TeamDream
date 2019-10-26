from django.conf.urls import url
from .views import *

app_name = "teamdreamapp"

urlpatterns = [
    url(r'^$', action_item_list, name='home'),
    url(r'^actionitems$', action_item_list, name='actionitems'),
    url(r'^register$', register_user, name='register'),
    url(r'^register/form$', register_form, name='registerform'),
]
