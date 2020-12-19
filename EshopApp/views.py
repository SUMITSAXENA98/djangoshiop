from django.shortcuts import render
from .models import Product,Category
# Create your views here.
def index(request):
    product=Product.objects.all()
    category=Category.objects.all()
    return render(request,'index.html',{'product':product,'category':category})


