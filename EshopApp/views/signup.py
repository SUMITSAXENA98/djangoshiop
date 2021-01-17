from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from EshopApp.models import customer
from django.views import View

# Create your views here.



class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        postdata=request.POST
        first_name=postdata.get('firstname')
        last_name=postdata.get('lastname')
        contact=postdata.get('contactno')
        email=postdata.get('email')
        password=postdata.get('password')
        #validation

        value={
            'first_name': first_name,
            'last_name' : last_name,
            'contact' : contact,
            'email' : email,

        }
        
        error_mssg=None

          

        custom=customer(firstName=first_name,
                            lastName=last_name,
                            contactNo=contact,
                            email=email,
                            password=password)
                            
        error_mssg = self.validate_customer(custom)
        

        

        
        if not error_mssg:
            print(first_name,last_name,contact,email,password)
            custom.password=make_password(custom.password)
            custom.save()
            return redirect('homepage')
        
        else:
            
            return render(request,'signup.html',{'error':error_mssg,'values':value})



    def validate_customer(self,custom):
        error_mssg=None
        if (not custom.firstName):
            error_mssg="first name required!"
        elif len(custom.firstName)<4:
            error_mssg="first name much ne 4 character long"  
        elif (not custom.lastName):
            error_mssg="first name required!"
        elif len(custom.lastName)<4:
            error_mssg="last name much ne 4 character long" 
        elif (not custom.contactNo):
            error_mssg='phone is required'
        elif len(custom.contactNo)<10:
            error_mssg='invalid contact'
        elif len(custom.email)<5:
            error_mssg="email must be grater than 5 digit"
        elif len(custom.password)<6:
            error_mssg="password must be grater than 6 digit"

        return error_mssg
