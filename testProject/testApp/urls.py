#
from django.conf.urls import url
from testApp.views import bank_account,balance_inq,do_transaction,feedback,process_feedback,history,profile,loan, testView
from loginmodule.views import login
from testApp import views
from . import views
urlpatterns=[
	url(r'^$',views.HomePageView.as_view()),
	url(r'transaction/$',bank_account),
	url(r'process_feedback',process_feedback),
	url(r'balance_inq/$',balance_inq),
	url(r'do_transaction',do_transaction),
	url(r'history/$',history),
	url(r'profile/$',profile),
	url(r'loan/$',loan),
	url(r'test/$', testView),
	url(r'feedback/$',feedback),
	url(r'^$',login),
]
