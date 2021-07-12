from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from users.models import Users,Logins,Courses,Chat,Quiz,QuizBranch,evaluation
from django.contrib import messages
from django.views.generic import CreateView, ListView
import urllib
import random as rd
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ChatForm,CHOICES
from django.core.files.storage import FileSystemStorage
#from django.utils.datastructures import MultiValueDictKeyError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import os
from .sending import sendmail,sendingmarks


i=0
# Create your views here.

def homepage(request):
	return render(request,'users/header.html')
#@login_required
def dashboard(request):
	return render(request,'users/dashboard.html')

def register(request):
	try:
		if request.method=='POST':
			new_name=request.POST['name']
			registration_no = request.POST['register_no']
			branch = request.POST['branch']
			new_email= request.POST['email']
			sendmail(new_email)
			new_password = request.POST['password']
			con_password = request.POST['con_password']
			if new_password == con_password:
				Users.objects.create(name=new_name,register_no=registration_no,branch=branch,email=new_email,password=new_password,con_password=con_password)
				messages.success(request,'{} is successfully registered'.format(registration_no))
				return redirect('/lgn/')
			else:
				messages.error(request,'password did not match')
				return redirect('/rgt/')
	except :
		return render(request,'users/register.html')
	return render(request,'users/register.html')

#@login_required
def login(request):
	try:
		if request.method=="POST":
			if request.POST['email']=='':
				return redirect('/rgt/') 
			email = request.POST['email']
			print(email)
			id = Users.objects.get(email=email)
			password = request.POST['password']
			if password==Users.objects.get(email= email).password:
				Logins.objects.create(email=email,password=password)
				messages.success(request,"{} is login successfully".format(email))
				return redirect('/dashboard/'+str(id.register_no))
			else:
				messages.error(request,'password did not match')
				return redirect('/rgt/')
	except:
		return render(request,'users/login.html')
	return render(request,'users/login.html')
			
def check(request):
	if request.method=="POST":
		name = request.POST['register']
		data = Users.objects.all()
		for i in data:
			if name == i.register_no:
				break
		else:
			return redirect('/rgt/')

		return redirect('/dashboard/'+str(name))
	return render(request,'users/check.html')

def dashboard(request,id):
	name = Users.objects.get(register_no=id)
	print(id)
	exams = evaluation.objects.filter(reg_no=id).filter(posted_at__lte=timezone.now()).order_by('-posted_at')

	if request.method=="POST":
		branch = request.POST['branch']
		if 'select' in request.POST:
			Courses.objects.create(reg_no=name.register_no,branch=branch)
			if branch=="IT":
				branch='CSE'
			return redirect('/courses/'+str(id)+'/'+str(branch))
		else:
			return redirect('/quiz/'+str(id)+'/')
	return render(request,'users/dashboard.html',{'id':id,'exams':exams})

def courses(request,id,branch):
	dataset_path = "./users/static/courses/"+str(branch)
	data =list(os.listdir(dataset_path))
	data1 =[urllib.parse.quote(i,safe="") for i in data]
	# for i in data:
	# 	data1[i]=urllib.parse.quote(i,safe="")
	redirect("/pdf/"+str(id)+str(branch))

	return render(request,'users/courses.html',{'notes':data,'branch':branch,'id':id})

def pdf(request,id,branch,course):
	Courses.objects.create(reg_no=id,branch=branch,course=course)
	Model = Courses.objects.all()
	for i in Model:
		print(i.reg_no,i.branch,i.course)
	print(id,branch,course)
	file_name='E:/elearning_platform/users/static/courses/'+str(branch)+'/'+str(course)
	messages.success(request,"{0} is open {1} of {2}".format(id,branch,course))
	with open(file_name,'rb') as pdf:
		response = HttpResponse(pdf,content_type='application/pdf')
		response['Content-Disposition'] = 'inline; filename="file_name"+/'
		return response 

def profile(request,id):
	f=id
	id = Users.objects.get(register_no=id)
	if request.method == "POST":
 		return redirect("/passwordchange/"+str(f))
	return render(request,"users/profile.html",{'id':id.register_no,'data':id})
	#id = Users.objects.get(register_no=id)
 	#return render(request,"users/profile.html",{'id':id})

def quiz(request,id):
	branch = ['CSE','EEE','IT','ECE','EIE','ME','CE']
	return render(request,'quizes/quiztemplate.html',{'id':id,'branch':branch})
dataoutput =[]

def exam(request,id,branch):
	if request.method=="POST":
		f=0
		#QuizBranch.objects.create(reg_no=name.register_no,branch=branch)
		if branch=="IT":
			branch="CSE"
		name = Users.objects.get(register_no=id)
		questions = Quiz.objects.filter(branch=branch)
		length = len(questions)
		choices = list(range(length))
		rd.shuffle(choices)
		questionid = choices[:20]
		print("infv")
		for i in questionid:
			dataoutput.append(questions[i])
		return redirect("/quizexam/"+str(id)+'/'+str(branch))
	return render(request,'quizes/quizmain.html',{'id':id,'branch':branch})
dataresult=[]
list1=[]
def quizexam(request,id,branch):
		try: 
			f=0
			c=0
			data = dataoutput[f]
			context ={
				'id':id,
				'branch':branch,
				'data':data,
				'counter':c
			}
		except:
			pass

			
		if request.method=="POST":
			if 'CHOICES1' in request.POST:
				print('one')
				selected_option=data.option_1
			elif 'CHOICES2' in request.POST:
				print('teo')
				selected_option=data.option_2
			elif 'CHOICES3' in request.POST:
				print('three')
				selected_option=data.option_3
			elif 'CHOICES4' in request.POST:
				print('four')
				selected_option=data.option_4
			else:
				selected_option=''
			if selected_option==data.corranswer:
				print(selected_option,data.corranswer)
				list1.append(1)
			dataresult.append([data.question,data.corranswer,selected_option])
			dataoutput.pop(0)
			c+=1
		try:
			f=0
			data = dataoutput[f]
			context ={
				'id':id,
				'branch':branch,
				'data':data,
			}
		except IndexError:
			d = list1.count(1)
			p = (d/20)*100
			print(d,p)
			score=0
			list1.clear()
			return redirect('/result/'+str(id)+'/'+str(branch)+'/'+str(d)+'/'+str(p))


		return render(request,'quizes/quizexam.html',context)


	
def passchange(request,id):
	if request.method=="POST":
		print(id)
		data = Users.objects.get(register_no=id)
		pas = request.POST['newpass'];
		newpass = request.POST['renewpass']
		if pas ==newpass:
			data.password = pas 
			data.save()
			return redirect('/profile/'+str(id))
		else:
			return redirect('passwordchange'+str(id))
	return render(request,'users/passwordchange.html',{'id':id})




def chat(request,id):
	form_class = ChatForm
	model = ChatForm
	if request.method == "POST":
		chat = request.POST['message']
		if chat!="":
			Chat.objects.create(reg_no=id,message=chat,posted_at = timezone.now())
		objects_list = Chat.objects.filter(posted_at__lte=timezone.now()).order_by('-posted_at')
		return render(request,'chat/chatview.html',{'objects_list':objects_list,'id':id})
	return render(request,'chat/base.html',{'id':id})
class plot:
	def __init__(self,question,corranswer,selected_option):
		self.question=question
		self.corranswer=corranswer
		self.selected_option=selected_option


def result(request,id,branch,marks,percentage):
	evaluation.objects.create(reg_no=id,branch=branch,marks=marks,posted_at=timezone.now())
	data=[]
	for i in dataresult:
		f = plot(i[0],i[1],i[2])
		data.append(f)
	dataresult.clear()
	name = Users.objects.get(register_no=id)
	sendingmarks(name.email,branch,marks)
	if request.method=="POST":
		return redirect('/quiz/'+str(id))
	return render(request,'quizes/result.html',{'id':id,'marks':marks,'percentage':percentage,'data':data})
	

	# selected_option = all_choices.index(request.POST['CHOICES'])
	# print(selected_option)


def forgotpassword(request):
	if request.method=="POST":
		id = request.POST['register']
		return redirect("/forgot/"+str(id))
	return render(request,"users/forgotcheck.html")

def forgot(request,id):
	print('hii')
	if request.method=="POST":
		data = Users.objects.get(register_no=id)
		pas = request.POST['newpass'];
		newpass = request.POST['renewpass']
		if pas ==newpass:
			data.password = pas 
			data.save()
			return redirect('/lgn/')
		else:
			return redirect('/forgot/'+str(id))
	return render(request,'users/forgot.html',{'id':id})
