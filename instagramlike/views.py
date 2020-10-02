from django.http import HttpResponse
import json


def sort_integers(request):

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)

    # import pdb; pdb.set_trace()
    data = {
        'status':200,
        'numbers':sorted_ints,
        'message':'Integers sorted successfully'

    }

    return HttpResponse(
        json.dumps(data,indent=4),
        content_type='application/json')

def say_hi(request,name,age):
    """return a greeting"""
    if age < 12:
        message = "Sorry {}, you are not allowed here".format(name)
    else:
        message = 'Hello, {}! Welcome'.format(name)

    return HttpResponse(message)