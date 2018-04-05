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
        c={}
        c['msg']='Invalid username or password'
        return render(request,'login.html',c)

def loggedin(request):
    return render_to_response('loggedin.html',{"full_name":request.user.username})
def invalidlogin(request):
    c={}
    c['msg']='Invalid username or password'
    return render(request,'login.html',c)
def logout(request):
    c={}
    c['msg']='you are Loggedout'
    return render(request,'login.html',c)
def about_us(request):
    return render_to_response('about_us.html')
def FAQ(request):
    return render_to_response('FAQ.html')
def contact_us(request):
    return render_to_response('contact_us.html')
