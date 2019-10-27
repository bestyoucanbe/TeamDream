from django.shortcuts import render

# This view takes you to the itemtype addition form.
# The itemtypes/addform.html is the template containing the form.


def itemtype_addform(request):
    template = 'itemtypes/addform.html'
    # Nothing needs to be sent to the template--so an empty dictionary is being sent.
    context = {}

    return render(request, template, context)
