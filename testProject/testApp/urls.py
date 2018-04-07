#
from django.conf.urls import url
from testApp.views import bank_account,balance_inq,do_transaction,transaction_success,insufficient_bal,invalid_amount,invalid_account_no,history,process_loan,profile,loan, testView
from testApp import views
from . import views
urlpatterns=[
	url(r'^$',views.HomePageView.as_view()),
	url(r'transaction/$',bank_account),
	url(r'balance_inq/$',balance_inq),
	url(r'do_transaction',do_transaction),
	url(r'transaction_success/$',transaction_success),
	url(r'insufficient_bal/$',insufficient_bal),
	url(r'invalid_amount/$',invalid_amount),
	url(r'invalid_account_no/$',invalid_account_no),
	url(r'history/$',history),
	url(r'process_loan/$',process_loan),
	url(r'profile/$',profile),
	url(r'loan/$',loan),
	url(r'test/$', testView),
]
