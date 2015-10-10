from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from forms import LoginForm, GroupForm, SensorForm
from models import Group, Sensor
import json
import helper
from django.shortcuts import *

@login_required(login_url='/login')
def index(request):
    groups = Group.objects.all()
    return render_to_response('index.html', { 'groups' : groups })

@login_required
def show_group(request, name):
    group = Group.objects.get(name=name)
    sensors = group.sensor_set.all()
    return render_to_response('index_sensors.html', { 'sensors' : sensors, 'group_name' : group.name })

def new_sensor(request, name):
    group = Group.objects.get(name=name)
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            payload = {}
            payload['sensorType'] = form.cleaned_data['sensorType']
            payload['zipCode'] = form.cleaned_data['zipCode']
            url = "https://a6.cfapps.io/groups/" + str(group.code) + "/sensors"
            result = json.loads(helper.post_request(url, {}))
            s = Sensor.objects.create(group_id=group.id,
                                    name=form.cleaned_data['name'],
                                    sensorType=payload['sensorType'],
                                    zipCode=payload['zipCode'],
                                    code=result['sensorId'])
            s.save()
            return HttpResponseRedirect("/group/"+group.name)
    else:
        form = SensorForm()
    return render_to_response('new_sensor.html', { 'form' : form, 'group_name': group.name }, context_instance=RequestContext(request))

def new_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group_code = helper.post_request("https://a6.cfapps.io/groups", {})
            groupID = json.loads(group_code)['groupId']
            group = Group.objects.create(code=groupID, name=form.cleaned_data['name'])
            group.save()
            return HttpResponseRedirect("/index")
    else:
        form = GroupForm()
    return render_to_response('new_group.html', { 'form' : form }, context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html')

#Switch to UserForm?
def login(request):
    if request.method =='POST':
         try:
             User.objects.get(username=request.POST['username'])
             user = authenticate(username=request.POST['username'], password=request.POST['password'])
             auth_login(request, user)
             return HttpResponseRedirect("/index")
         except User.DoesNotExist:
             return render_to_response('registration/login.html')
    else:
        form = LoginForm()
        return render_to_response('registration/login.html',
                                    { 'form': form },
                                    context_instance=RequestContext(request))

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password1'])
            user.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
            auth_login(request, new_user)
            return HttpResponseRedirect("/index")
    else:
        form = UserCreationForm()
        return render_to_response('registration/register.html',
                                { 'form': form },
                                context_instance=RequestContext(request))
