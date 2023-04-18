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

def Home(request):
    return render(request,'index.html', {'Home':Home})

def about(request):
    return render(request, "about.html", {'about':about})

def account(request):
    return render(request, "account.html", {'account':account})

def cart(request):
    return render(request, "cart.html", {'cart':cart}) 

def productdetail(request):
    return render(request, "product-detail.html", {'productdetail':productdetail}) 

def products(request):
    return render(request, "products.html", {'products':products})

def top(request):
    return render(request, "top.html", {'top':top})

def logout(request):
    return render(request, "logout.html", {'logout':logout})






