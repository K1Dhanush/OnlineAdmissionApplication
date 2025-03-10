from django.shortcuts import render,redirect

#for register
from .forms import RegisterForm
from django.contrib import messages




# Create your views here.
from .models import Category
from .forms import CategoryForm
from .models import Product
from .forms import ProductForm
from .models import un #
from .forms import un

#register
def registerpage(request) :
    #form=UserCreationForm()
    form=RegisterForm()
    if request.method=='POST':
        #form=UserCreationForm(request.POST)
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            uname=request.POST['username']
            messages.success(request,'Account created Successfully for '+uname)
            return redirect('login')
    
    return render(request,'register.html',{'form':form})

#home
def homepage(request) :
    return render(request,'home.html')
#new iit
def iitpage(request) :
    return render(request,'iit.html')
#new nit
def nitpage(request) :
    return render(request,'nit.html')
#new deemed
def deemedpage(request) :
    return render(request,'deemed.html')
#new deemed
def TamilNadupage(request) :
    return render(request,'TamilNadu.html')
#new deemed
def Maharashtrapage(request) :
    return render(request,'Maharashtra.html')
#new deemed
def APpage(request) :
    return render(request,'AP.html')



#base
def indexpage(request) :
    return render(request,'index.html')

#for login
def loginpage(request) :
    
    #new
    form=RegisterForm()
    if request.method=='POST':
        #form=UserCreationForm(request.POST)
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            uname=request.POST['username']
            #messages.success(request,'Account created Successfully for '+uname)
            
        return redirect('listproduct')
    
    return render(request,'login.html')



#productApp----
def listCategory(request):
    allcategories=Category.objects.all()
    return render(request,'listcategory.html',{'allcategories':allcategories,}) 

def insertCategory(request,id=0):
    if id==0:
        if request.method=='GET':
            form=CategoryForm()
            return render(request,'insertcategory.html',{'form':form})
        else:
            form=CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/listcategory')
    else:
        if request.method=='GET':
            cat=Category.objects.get(id=id)
            form = CategoryForm(instance=cat) 
            return render(request,'insertcategory.html',{'form':form})
        else:
            cat=Category.objects.get(id=id)
            form=CategoryForm(request.POST,instance=cat)
            if form.is_valid():
                form.save()
                return redirect('/listcategory') 

def deleteCategory(request,id=0):
    emp=Category.objects.get(id=id)
    emp.delete()
    return redirect('/listcategory')


def listProduct(request):
    allproducts=Product.objects.all()
    allcategories=Category.objects.all()
    #allcategories added below
    return render(request,'listproduct.html',{'allproducts':allproducts,'allcategories':allcategories,})


def insertProduct(request,id=0):
    if id==0:
        if request.method=='GET':
            form=ProductForm()
            return render(request,'insertproduct.html',{'form':form})
        else:
            form=ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/listproduct') 
    
    else:
        if request.method=='GET':
            product=Product.objects.get(id=id)
            form = ProductForm(instance=product) 
            return render(request,'insertproduct.html',{'form':form})
        else:
            product=Product.objects.get(id=id)
            form=ProductForm(request.POST,instance=product)
            if form.is_valid():
                form.save()
                return redirect('/listproduct') 

def deleteProduct(request,id=0):
    emp=Product.objects.get(id=id)
    emp.delete()
    return redirect('/listproduct')