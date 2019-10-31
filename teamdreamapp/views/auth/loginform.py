from django.shortcuts import render

# This view takes you to the login form.
# The registration/login.html is the template containing the form.


def login_form(request):
    template = 'registration/login.html'
    # Nothing needs to be sent to the template--so an empty dictionary is being sent.
    context = {}

    return render(request, template, context)
