from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def go_home(request):

    template = 'home/home.html'
    context = {}

    return render(request, template, context)
