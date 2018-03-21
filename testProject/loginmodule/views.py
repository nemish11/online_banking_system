from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
# Create your views here.
def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)
def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        request.session['username']=username
        return HttpResponseRedirect('/loginmodule/loggedin/')
    else:
        return HttpResponseRedirect('/loginmodule/invalidlogin/')
def loggedin(request):
    #print('hii')
    return render_to_response('loggedin.html',{"full_name":request.user.first_name})
def invalidlogin(request):
    return render_to_response('invalidlogin.html')
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
