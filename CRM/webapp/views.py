from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
# Create your views here.

def index(request):
    return render(request, 'webapp/index.html')

#register a user
def register(request):
    form = CreateUserForm()
    if request.method == "POST": #if the user has submitted the form
        form = CreateUserForm(request.POST) #create a form with the data passed in
        if form.is_valid(): #check to make sure all fields are filled out correctly
            form.save() 
           
        return redirect('login')
    
    context = {
        'form': form,
        }
    return render(request, 'webapp/register.html', context)

# Login a user
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid(): 

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
    context = {
                'form' : form,
                }
            
    return render(request,'webapp/login.html',context)

#dashboard
@login_required(login_url='login') #decorator
def dashboard(request):
    record = Record.objects.all()
    context={
        "records":record,
        }
    return render(request,'webapp/dashboard.html', context)

#create a record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method=='POST':
        form = CreateRecordForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {
        'form':form,
        }
    return render(request,'webapp/create-record.html',context)

#update a record
@login_required(login_url="login")
def update_record(request,pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(instance=record, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect ('dashboard')
        context ={
            'form': form,
            }
    return render (request , 'webapp/update-record.html', context)

#read or view a single record
@login_required(login_url="login")
def singular_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context = {
        'record':all_records,
        }
    return render(request,"webapp/view-record.html", context)


    



#logout
def logout(request):
    auth.logout(request)
    return redirect('/')



   


            


