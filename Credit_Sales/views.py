from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Credit_Sales.forms import PaymentForm

from Credit_Sales.models import Credit_Sale, Payment
from User.models import Customer

# Create your views here.

def creditSalesView(request,customerID):
    credits = []
    message =None
    
    if request.method == "POST":
        data = request.POST
        phone_number = data['phone_number']
        credits = Credit_Sale.objects.filter(
            customer__phone_number = phone_number, fully_paid=False )
        if not credits:
            message = "No data found. Please be sure the phone number is correct"
        
    if customerID>0:
        credits = Credit_Sale.objects.filter(
            customer = customerID, fully_paid=False )
        if not credits:
            message = "No data found. Please be sure the phone number is correct"
        
    
        
    return render(request,"credit_sales/credit.html",{"credits":credits,"message":message}) 


def paymentView(request,creditId,action):
    
    previous_payments = None
    customer = None
    paymentId= None
    payment_instance = None
    
    if action =="add" or action =='view':
        customer = Customer.objects.get(credit_sale_customer__id = creditId)
        previous_payments = Payment.objects.filter(credit_sale=creditId)
        
    if action == "edit" or action =='delete':
        paymentId = creditId
        payment_instance = Payment.objects.get(pk=paymentId)
        creditId = payment_instance.credit_sale.id
        customer = Customer.objects.get(credit_sale_customer__id = creditId)
        previous_payments = Payment.objects.filter(credit_sale=creditId)

    if request.method == "POST" and action == "add":
        form = PaymentForm(data= request.POST)
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            credit_sale = Credit_Sale.objects.get(pk=creditId)
            Payment.objects.create(amount=amount,credit_sale=credit_sale)
            return HttpResponseRedirect(reverse('credit_sales:paymentView',
            kwargs={"action":"view","creditId":creditId}))
        else:
            return render(request,"credit_sales/payment.html",
                  {"form":form,"creditId":creditId,
                   'customer':customer,"previous_payments":previous_payments})  
            
    if action == "edit":
        if request.method == "POST":
            form = PaymentForm(data= request.POST,instance=payment_instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('credit_sales:paymentView',
                        kwargs={"action":"view","creditId":creditId}))
            else:
                return render(request,"credit_sales/payment.html",
                  {"form":form,"creditId":payment_instance.id,
                   'customer':customer,"previous_payments":previous_payments})
        else:
            return render(request,"credit_sales/payment.html",
                  {"form":PaymentForm(instance=payment_instance),
                   "creditId":payment_instance.id,"action":"edit",
                   'customer':customer,"previous_payments":previous_payments})
    
    if action == "delete":
        payment_instance.delete()
        return HttpResponseRedirect(reverse('credit_sales:paymentView',
            kwargs={"action":"view","creditId":creditId}))
    
    return render(request,"credit_sales/payment.html",
                      {"previous_payments":previous_payments,
                       "form":PaymentForm(),'creditId':creditId,"action":"add",
                       'customer':customer})
        