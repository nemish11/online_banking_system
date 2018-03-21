from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.views import generic
from django.http import HttpResponseRedirect
from testApp.models import Bank_account,History
from django.template.context_processors import csrf
from django.views import generic
from datetime import datetime
class HomePageView(TemplateView):
	def get(self,request,**kwargs):
		return render(request,'transaction.html',context=None)

class Bank_account_view(generic.ListView):
	model=Bank_account
	template_name='transaction.html'

class balance_inq_view(generic.ListView):
	model=Bank_account
	template_name='balance_inq.html'

def history(request):
	bank_table=Bank_account.objects.all()
	history_table=History.objects.all()
	c={}
	c['bank_table']=bank_table
	c['history_table']=history_table
	return render(request,'history.html',c)

def do_transaction(request):
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
	sum+=int(amount1)
	print(sum)
	if(int(sum)>50000):
		return render_to_response('limit_exceed.html')
	try:
		to_ac=Bank_account.objects.get(account_no=request.POST.get('from_account',''))
	except NameError:
		return render_to_response('invalid_account_no.html')
	if(int(amount1)<0):
		return HttpResponseRedirect('invalid_amount')
	if(from_ac.amount<int(amount1)):
		return HttpResponseRedirect('insufficient_bal')
	from_ac.amount-=int(amount1)
	to_ac.amount+=int(amount1)
	h=History(from_account_no=to_ac.account_no,to_account_no=from_ac.account_no,amount_transfer=amount1,time=datetime.now())
	h.save()
	to_ac.save()
	from_ac.save()
	return HttpResponseRedirect('transaction_success')
def transaction_success(request):
	return render_to_response('transaction_success.html')
def insufficient_bal(request):
	return render_to_response('insufficient_bal.html')
def invalid_amount(request):
	return render_to_response('invalid_amount.html')
def invalid_account_no(request):
	template_name='invalid_account_no'
	return render_to_response('invalid_account_no.html')
