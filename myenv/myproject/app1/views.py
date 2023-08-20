from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login
# from .forms import EmployeeForm
# Create your views here.
# def index(request):
#     return render(request,'index.html')


# def index (request):
#     if request.method=='POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return render(request,'submit-contact.html')
#     form = EmployeeForm
#     forms={
#         'form':form
#         }
#     return render(request,'index.html',forms)
def employe_list(request):
    employees={
        'emp_list':Employee.objects.all()
    }
    return render(request,'employe_list.html',employees) 
def index (request):
    if request.method == 'POST':
        name = request.POST['name']
        emp_id = request.POST['emp_id']
        email = request.POST['email']
        phone = request.POST['phone']
        employee = Employee()
        employee.emp_id = emp_id
        employee.name = name
        employee.email = email
        employee.phone = phone
        employee.save()
        return redirect(employe_list)
    return render(request,'index.html')


def emp_delete (request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect(employe_list)

def emp_update(request,id):
    emp_update = Employee.objects.get(pk=id)
    return render (request,'update.html', {'emp_update':emp_update})


def emp_doupdate (request,id):
    # if request.method == 'POST':
        name = request.POST['name']
        emp_id = request.POST['emp_id']
        email = request.POST['email']
        phone = request.POST['phone']
        employee = Employee.objects.get(pk=id)
        employee.emp_id = emp_id
        employee.name = name
        employee.email = email
        employee.phone = phone
        employee.save()
        return redirect(employe_list)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(login_view)
    else:
            form = UserCreationForm()
            form.fields['username'].help_text = None
            form.fields['password1'].help_text = None
            form.fields['password2'].help_text = None
    return render(request,'register.html',{'form':form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)     
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(index)
    else:
                form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})
