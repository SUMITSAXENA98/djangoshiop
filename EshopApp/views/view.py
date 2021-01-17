from django.shortcuts import render,redirect
from EshopApp.models import Product,Category
from django.views import View

# Create your views here.

class Index(View):
    
    def post(self,request):
        product=request.POST.get('product')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1

        request.session['cart']=cart
        print ('cart',request.session['cart'])

        return redirect("homepage")
    

    def get(self,request):
        product=None
       
        category=Category.objects.all()
        categoryID=request.GET.get('category')
        print(categoryID)
        if categoryID:
            product=Product.objects.filter(category=categoryID)
        else:
            product=Product.objects.all()

        
        print('you are :',request.session.get('customeremailobj_email'))  #session


        return render(request,'index.html',{'product':product,'category':category})




    




        

   









        
        


