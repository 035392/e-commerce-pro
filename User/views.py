from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

from User.models import Customer
User=get_user_model()
from django.shortcuts import render
from Branch.models import Branch
from User.Forms import CustomerForm, UserEditForm, UserForm

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
            user= request.user
            # return HttpResponseRedirect(reverse("publisher:publisherView",
            # kwargs={"username":user.full_name}))
    if request.method=="POST":
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user= authenticate(request, username=email, password=password)
            if user:
                login(request,user)
            return HttpResponseRedirect(reverse('user:dashboardView', kwargs={'fullname':user.full_name}))
    else:
        form=AuthenticationForm()
    return render(request,"user/login.html",{"form":form})

def logoutView(request):
    if request.method=="POST":
        logout(request)
    return HttpResponseRedirect(reverse('user:loginView'))


def dashboardView(request,fullname):
    branch_instance = Branch.objects.get(id=1)
    return render(request,"user/dashboard.html",{"userform": UserForm})


def userView(request,userId,action):
    users = User.objects.all()
    if userId != 0:   
        user_instance = User.objects.get(id=userId)
    
    if request.method == "POST" and action == "add":
        form = UserForm(data= request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:userView',
            kwargs={"action":"view","userId":0}))
        else:
            return render(request,"user/user.html",
                  {"form":form,"userId":0,"action":"add"})  
            
    if action == "edit":
        if request.method == "POST":
            form = UserEditForm(data= request.POST,instance=user_instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('user:userView',
                        kwargs={"action":"view","userId":0}))
            else:
                return render(request,"user/user.html",
                  {"form":form,"userId":user_instance.id,"action":"edit"})
        else:
            return render(request,"user/user.html",
                  {"form":UserEditForm(instance=user_instance),
                   "userId":user_instance.id,"action":"edit"})
    
    if action == "delete":
        user_instance.delete()
        return HttpResponseRedirect(reverse('user:userView',
            kwargs={"action":"view","userId":0}))
                 
    return render(request,"user/user.html",
                  {"form":UserForm(),"userId":0,"action":"add","users":users})
    
    
    
def customerView(request,customerId,action):
    customers = Customer.objects.all()
    if customerId != 0:   
        customer_instance = Customer.objects.get(id=customerId)
    
    if request.method == "POST" and action == "add":
        form = CustomerForm(data= request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:customerView',
            kwargs={"action":"view","customerId":0}))
        else:
            return render(request,"user/customer.html",
                  {"form":form,"customerId":0,"action":"add"})  
            
    if action == "edit":
        if request.method == "POST":
            form = CustomerForm(data= request.POST,instance=customer_instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('user:customerView',
                        kwargs={"action":"view","customerId":0}))
            else:
                return render(request,"user/customer.html",
                  {"form":form,"customerId":customer_instance.id,"action":"edit"})
        else:
            return render(request,"user/customer.html",
                  {"form":CustomerForm(instance=customer_instance),
                   "customerId":customer_instance.id,"action":"edit"})
    
    if action == "delete":
        customer_instance.delete()
        return HttpResponseRedirect(reverse('user:customerView',
            kwargs={"action":"view","customerId":0}))
                 
    return render(request,"user/customer.html",
                  {"form":CustomerForm(),"customerId":0,"action":"add","customers":customers})    

    