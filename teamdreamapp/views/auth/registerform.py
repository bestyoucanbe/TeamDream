from django.shortcuts import render

def register_form(request):
    template = 'registration/registration.html'
    context = {}

    return render(request, template, context)