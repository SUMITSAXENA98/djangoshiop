from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from EshopApp.models import customer
from django.views import View

# Create your views here.

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customeremail=customer.get_customer_by_email(email)
        customeremailobj=customeremail[0]
        
        error_mssg=None
    
    
        if customeremailobj:
            flag= check_password(password,customeremailobj.password)
            if flag:
                request.session['customeremailobj_id']=customeremailobj.id
                request.session['customeremailobj_email']=customeremailobj.email
                return redirect('homepage')
            else:
                error_mssg = "email and password invalid"

        else:
            error_mssg = "email and password invalid "

        return render(request,'login.html',{'error':error_mssg})
    
    def get_customer_by_email(self,email):
        return(customer.objects.all.get(email=email))
    