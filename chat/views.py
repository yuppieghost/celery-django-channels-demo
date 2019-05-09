import json

from django.http import HttpResponse
from . import tasks
from django.shortcuts import render

# Create your views here.
from django.utils.safestring import mark_safe



def index(req):
    return render(req, 'chat/index.html',{})


def room(req, room_name):
    return render(req, 'chat/room.html',{
        'room_name_json':mark_safe(json.dumps(room_name))

    })

def test(req):
    tasks.hello.delay()
    return HttpResponse(1)
