from django.http.response import HttpResponseRedirect 
from django.shortcuts import render, redirect
from .forms import LoginForm, RegForm
from django.http import HttpResponse

def Home(request):
    return render(request,'index.html')

def login_view(request):
   if request.method == "POST": 
       form = LoginForm(request.POST) 
       if form.is_valid(): 
            print('Username:', form.cleaned_data['Username'])
            print('Password:',form.cleaned_data['Password'])
            
            return redirect('Home')
   else: 
       form = LoginForm() 

   return render(request, "account.html", {'form':form})

def reg_view(request):
   if request.method == "POST": 
       form = RegForm(request.POST) 
       if form.is_valid(): 
            print('Username:', form.cleaned_data['Username'])
            print('Email:', form.cleaned_data['Email']) 
            print('Password:',form.cleaned_data['Password'])
            
            return redirect('Home')
   else: 
       form = RegForm() 

   return render(request, "account.html", {'form':form})
