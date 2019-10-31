from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout


def logout_user(request):
    # logout the user
    logout(request)
    # where to take the user after they are logged out
    return redirect(reverse('teamdreamapp:login'))
