from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
	student_name = models.CharField(max_length=20)

class Login(models.Model):
	account_no = models.CharField(max_length=20)
	user_id = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class Bank_account(models.Model):
	account_no = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	amount = models.IntegerField()
	user_id = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	phone_no = models.CharField(max_length=20)
	email_id = models.CharField(max_length=25)

class History(models.Model):
	from_account_no = models.CharField(max_length=20)
	to_account_no = models.CharField(max_length=20)
	amount_transfer = models.CharField(max_length=20)
	time = models.DateTimeField('date published')
