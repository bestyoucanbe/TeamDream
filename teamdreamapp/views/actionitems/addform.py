from django.shortcuts import render

# This view takes you to the action item addition form.
# The actionitems/addform.html is the template containing the form.


def action_item_addform(request):
    template = 'actionitems/addform.html'
    # Nothing needs to be sent to the template--so an empty dictionary is being sent.
    context = {}

    return render(request, template, context)
