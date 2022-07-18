from email.mime import image
from multiprocessing import context
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import ContactForm
from . models import Gallery,Contact,GroupofCompany,Product,Modal,Verticals,Brand,Ad,Client,Video
import json


# def test(request):
#     context = {

#     }
#     return render(request,'web/partials/h1.html',context)



def index(request):
    image = Gallery.objects.all()[:4]
    pimage =Product.objects.all()[:4]
    modaldis =Modal.objects.all()
    ad=Ad.objects.all()[:4]
    client=Client.objects.all()
    video=Video.objects.all()
    
    context={
         "image" :image,
         "is_home":True,
         "pimage" :pimage,
         "modaldis":modaldis,
         "ad":ad,
         "client":client, 
         "Video":video,
         

    }
        
    
    
    
    return render(request,'web/index.html',context)



def aboutus(request):
    context = {

    }
    return render(request,'web/aboutus.html',context)

def product(request):
    # brandname= Brand.objects.filter(is_active==True)
    brands = Brand.objects.filter(is_active = True )
    products =Product.objects.all()
    
    
    context = {
        "products":products,
        # "brand":brandname,
        "brands" : brands,


    } 
    return render(request,'web/product.html',context)


def groupofcompany(request):
    
    
    
    
    
    context={
         
        
         

    }
    return render(request,'web/vertical.html',context)


def gallery(request):
    image = Gallery.objects.all()
    context={
         "image" :image,

    }
    
    return render(request,'web/gallery.html',context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()   
    context= {
        "form":form,
    }
    return render(request,'web/contactus.html',context)


# def contact(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.referral = "web"
#             data.save()
#             response_data = {
#                 "status" : "true",
#                 "title" : "Successfully Submitted",
#                 "message" : "Message successfully submitted"
#             }
#         else:
           
#             response_data = {
                
#                 "status" : "false",
#                 "title" : "Form validation error",
#                 "message" : repr(form.errors)
#             }
#         return HttpResponse(json.dumps(response_data), content_type='application/javascript')
#     else:
#         context = {
#         "is_contact" : True,
#         "form" : form,
#         }
#         return render(request,'web/contactus.html',context)