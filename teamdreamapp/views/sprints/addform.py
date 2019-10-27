from django.shortcuts import render

# This view takes you to the sprint addition form.
# The sprints/addform.html is the template containing the form.


def sprint_addform(request):
    template = 'sprints/addform.html'
    # Nothing needs to be sent to the template--so an empty dictionary is being sent.
    context = {}

    return render(request, template, context)
