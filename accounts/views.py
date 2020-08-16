from django.shortcuts import render,redirect
from django.conf.urls.static import static
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import accpython
from .models import record
import datetime
# Create your views here.
def login(request):
	if (request.method=='POST'):
		username= request.POST['username']
		password= request.POST['password']

		user=auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect("selection")
		else:
			messages.info(request,"Invalid Username or password")
			return redirect('login')
	else:	
		return render (request,'login.html')

def register(request):
	if (request.method=="POST"):
		first_name= request.POST['name']
		username= request.POST['username']
		password= request.POST['password']
		re_password= request.POST['re_password']
		email= request.POST['email']
		if (password==re_password):
			if(User.objects.filter(username=username).exists()):
				messages.info(request,"Username already Taken!")
				return redirect('register')
			else:
				
				user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name)
				user.save();
				print('user created')
				return redirect('login')
		else:
			messages.info(request,"Password Didn't Match")	
			return redirect('register')
	else:	
		return render(request,'register.html')	

def quiz(request):
	ques = accpython.objects.all()
	return render(request,'quizpage.html',{'ques':ques})	

def selection(request):
	return render(request,'selection.html')	

def logout(request):
	auth.logout(request)
	return redirect('/')
def result(request):
	return render(request,'result.html')	

def get_data(request):
	data=request.POST['answer']
	ques = accpython.objects.all()
	corr_ans=[]
	for q in ques:
		corr_ans.append(str(q.id)+str(q.corr))
	response=list(data.split(','))
	marks=0	
	total=len(corr_ans)

	for i in range(len(response)):
		if (corr_ans[i]==response[i]):
			marks+=1
	user_id=request.POST['user']
	b=record(user=user_id,marks=marks,date=datetime.datetime.now()
		)
	b.save()
	qualified=True if (marks>=total//2) else False		
	return render(request,'result.html',{'marks':marks,'total':total,'ques':ques,'response':response,'corr_ans':corr_ans})
def logout(request):
	auth.logout(request)
	return redirect('/')
