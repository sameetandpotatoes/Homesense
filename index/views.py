from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import *

def index(request):
    return render_to_response('base.html')
