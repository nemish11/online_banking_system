from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.views import generic
from django.http import HttpResponseRedirect
from testApp.models import Bank_account,History,Feedback
from django.template.context_processors import csrf
from django.views import generic
from datetime import datetime
from django.contrib.auth.decorators import login_required

class HomePageView(TemplateView):
	def get(self,request,**kwargs):
		return render(request,'loginmodule/login.html',context=None)

@login_required(login_url="/loginmodule/login/")
def bank_account(request):
	bank_account_list=Bank_account.objects.all()
	c={}
	c['bank_account_list']=bank_account_list
	return render(request,'transaction.html',c)

@login_required(login_url="/loginmodule/login/")
def balance_inq(request):
	bank_account_list=Bank_account.objects.all()
	c={}
	c['bank_account_list']=bank_account_list
	return render(request,'balance_inq.html',c)

@login_required(login_url="/loginmodule/login/")
def history(request):
	bank_table=Bank_account.objects.all()
	history_table=History.objects.all()
	c={}
	bank_account_list=Bank_account.objects.all()
	c['bank_table']=bank_table
	c['history_table']=history_table
	return render(request,'history.html',c)

@login_required(login_url="/loginmodule/login/")
def do_transaction(request):
	if(request.POST.get('amount1','')=='' or request.POST.get('from_account','')==''):
		c={}
		bank_account_list=Bank_account.objects.all()
		c['bank_account_list']=bank_account_list
		c['msg']="Invalid account no...please try again."
		return render(request,'transaction.html',c)
	from_ac=Bank_account.objects.get(user_id=request.session.get('username'))
	sum=0
	sum=int(sum)
	history_table=History.objects.all()
	for cur in history_table:
		if(cur.from_account_no==from_ac.account_no):
			if(datetime.now().year==cur.time.year):
				if(datetime.now().month==cur.time.month):
					sum+=int(cur.amount_transfer)
	amount1=request.POST.get('amount1','')
	ac1=request.POST.get('from_account','')
	if (not amount1.isdigit()):
		c={}
		bank_account_list=Bank_account.objects.all()
		c['bank_account_list']=bank_account_list
		c['msg']="Invalid amount...please enter a correct amount."
		return render(request,'transaction.html',c)
	if(not ac1.isdigit()):
		c={}
		bank_account_list=Bank_account.objects.all()
		c['bank_account_list']=bank_account_list
		c['msg']="Invalid account no....enter correct account number"
		return render(request,'transaction.html',c)
	sum+=int(amount1)
	if(int(sum)>50000):
		c={}
		bank_account_list=Bank_account.objects.all()
		c['bank_account_list']=bank_account_list
		c['msg']="Your monthly limit exceed ...please try after month"
		return render(request,'transaction.html',c)
	try:
		to_ac=Bank_account.objects.get(account_no=request.POST.get('from_account',''))
	except:
		c={}
		bank_account_list=Bank_account.objects.all()
		c['bank_account_list']=bank_account_list
		c['msg']="Invalid account no....enter correct account number"
		return render(request,'transaction.html',c)
	if(int(amount1)<0):
		c={}
		bank_account_list=Bank_account.objects.all()
		c['bank_account_list']=bank_account_list
		c['msg']="Invalid amount...please enter a correct amount."
		return render(request,'transaction.html',c)
	if(from_ac.amount<int(amount1)):
		c={}
		bank_account_list=Bank_account.objects.all()
		c['bank_account_list']=bank_account_list
		c['msg']="Insufficient balance..."
		return render(request,'transaction.html',c)
	from_ac.amount-=int(amount1)
	to_ac.amount+=int(amount1)
	h=History(from_account_no=from_ac.account_no,to_account_no=to_ac.account_no,amount_transfer=amount1,time=datetime.now())
	h.save()
	to_ac.save()
	from_ac.save()
	bank_account_list=Bank_account.objects.all()
	c={}
	c['bank_account_list']=bank_account_list
	c['msg']="thank you.. Your transaction successful"
	return render(request,'transaction.html',c)

@login_required(login_url="/loginmodule/login/")
def profile(request):
	bank_account_list=Bank_account.objects.all()
	c={}
	c['bank_account_list']=bank_account_list
	return render(request,'view_profile.html',c)

@login_required(login_url="/loginmodule/login/")
def loan(request):
	return render(request,'loan.html')

@login_required(login_url="/loginmodule/login/")
def testView(request):
	return render(request, 'loginmodule/login.html')

@login_required(login_url="/loginmodule/login/")
def process_feedback(request):
	user_id=request.session.get('username')
	description=request.POST.get('feedback','')
	h=Feedback(user_id=user_id,description=description)
	h.save()
	c={}
	c['msg']="thank for giving feedback"
	return render(request,'notification.html',c)

@login_required(login_url="/loginmodule/login/")
def feedback(request):
	return render(request,'feedback.html')
