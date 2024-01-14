from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
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
    return render(request,'webapp/dashboard.html')



#logout
def logout(request):
    auth.logout(request)
    return redirect('/')



   


            


