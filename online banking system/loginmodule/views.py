from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from testApp.models import Bank_account
from django.contrib.auth.decorators import login_required


def login(request):
    if not request.user.is_authenticated:
        c={}
        c.update(csrf(request))
        return render_to_response('login.html',c)
    return HttpResponseRedirect('/loginmodule/loggedin/')
def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        request.session['username']=username
        b=Bank_account.objects.all()
        for user in b:
            if user.user_id==username:
                return HttpResponseRedirect('/loginmodule/loggedin/')
        c={}
        c['msg']='Invalid username or password'
        return render(request,'login.html',c)
    else:
        c={}
        c['msg']='Invalid username or password'
        return render(request,'login.html',c)

@login_required(login_url="/loginmodule/login/")
def loggedin(request):
    return render_to_response('loggedin.html',{"full_name":request.user.username})

def invalidlogin(request):
    c={}
    c['msg']='Invalid username or password'
    return render(request,'login.html',c)
def logout(request):
    c={}
    c['msg']='you are Loggedout'
    if request.user.is_authenticated:
        auth.logout(request)
    return render(request,'login.html',c)

def about_us(request):
    return render(request,'about_us.html')
def FAQ(request):
    return render(request,'FAQ.html')
def contact_us(request):
    return render(request,'contact_us.html')
