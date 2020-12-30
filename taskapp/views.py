from django.shortcuts import render,redirect
from django.http import HttpResponse
from taskapp.forms import StuFacultyForm
from taskapp.models import StuFac
# Create your views here.

def student(request):
	if request.method=='POST':
		name=request.POST.get('name')
		password=request.POST.get('password')
		rollno=request.POST.get('rollno')
		email=request.POST.get('email')
		collegename=request.POST.get('collegename')
		department=request.POST.get('department')
		#designation=request.POST.get('designation')
		StuFac.objects.create(name=name,password=password,rollno=rollno,email=email,collegename=collegename,department=department)
		return HttpResponse('done')
	return render(request,'sip.html')

def faculty(request):
	if request.method=='POST':
		fac_name=request.POST.get('fac_name')
		fac_password=request.POST.get('fac_password')
		id1=request.POST.get('id1')
		fac_email=request.POST.get('fac_email')
		fac_collegename=request.POST.get('fac_collegename')
		fac_department=request.POST.get('fac_department')
		salary=request.POST.get('salary')
		designation=request.POST.get('designation')
		StuFac.objects.create(fac_name=fac_name,fac_password=fac_password,id1=id1,fac_email=fac_email,fac_collegename=fac_collegename,fac_department=fac_department,salary=salary,designation=designation)
		return HttpResponse("Done")
	#f1=StuFacultyForm()
	return render(request,'fac.html')


def home(request):
	return render(request,'navbar.html')

def login(request):
	#data=StuFac.objects.get(i)
	if request.method=='POST':
		name = request.POST['name']
		password= request.POST['password']
		data=StuFac.objects.all().filter(name=name,password=password)
		data1=StuFac.objects.all().filter(fac_name=name,fac_password=password)
		if data:
			#return HttpResponse("This is student Data")
			#return render(request,'sip.html',{'data':data})
			return redirect('/sip')
		elif data1:
			return render(request,'fac.html',{'data1':data1})
			#return redirect('/fac')

	return render(request,'login.html')
