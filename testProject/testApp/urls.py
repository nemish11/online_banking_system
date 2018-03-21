#
from django.conf.urls import url
from testApp.views import Bank_account_view,balance_inq_view,do_transaction,transaction_success,insufficient_bal,invalid_amount,invalid_account_no,history
from testApp import views
from . import views
urlpatterns=[
	url(r'^$',views.HomePageView.as_view()),
	url(r'transaction/$',Bank_account_view.as_view()),
	url(r'balance_inq/$',balance_inq_view.as_view()),
	url(r'do_transaction',do_transaction),
	url(r'transaction_success/$',transaction_success),
	url(r'insufficient_bal/$',insufficient_bal),
	url(r'invalid_amount/$',invalid_amount),
	url(r'invalid_account_no/$',invalid_account_no),
	url(r'history/$',history),
]
