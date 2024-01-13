from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm
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
           
        return redirect('')
    
    context = {
        'form': form,
        }
    return render(request, 'webapp/register.html', context)


