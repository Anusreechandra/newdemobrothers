from re import M
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.text import slugify

# from tinymce.models import HTMLField




class Gallery(models.Model):
    image         = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    itwo          = VersatileImageField('Image',upload_to = 'image/testimagemodel/', null=True,)
    class Meta:
        verbose_name_plural =("Gallery")

    def __str__(self):
        return str(self.image)



class Brand(models.Model):
        brandname = models.CharField(max_length=50)
        is_active  = models.BooleanField(default=True)

        class Meta:
            db_table = 'brand'
            


class Video(models.Model):
        video = models.FileField(upload_to='videos_uploaded',null=True,)

        class Meta:
            db_table = 'Video'



class Product(models.Model):
    pimage         = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    
    brandname = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    pname = models.CharField(max_length=20,null=True)
    pdis = models.CharField(max_length=100,null=True)
   

    class Meta:
        verbose_name_plural =("Product")

    def __str__(self):
        return str(self.pimage)


class Verticals(models.Model):
    cimage         = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    
    cname = models.CharField(max_length=20,null=True)
    cdis = models.CharField(max_length=100,null=True)
   

    class Meta:
        verbose_name_plural =("verticals")

    def __str__(self):
        return str(self.cimage)        

class Ad(models.Model):
    adimage         = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    
    
    adtitle = models.CharField(max_length=100,null=True)
   

    class Meta:
        verbose_name_plural =("Ad")

    def __str__(self):
        return str(self.adimage)  




class Client(models.Model):
    clientimage         = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    
    clientname = models.CharField(max_length=20,null=True)
    clientwork  = models.CharField(max_length=20,null=True)
    clientdis = models.CharField(max_length=100,null=True)
   

    class Meta:
        verbose_name_plural =("Client")

    def __str__(self):
        return str(self.clientimage) 





class catagary(models.Model):
    catname = models.CharField(max_length=50)

    class Meta:
         db_table = 'catagary'






class Modal(models.Model):
        modaldis = models.CharField(max_length=50)

        class Meta:
            db_table = 'modal'




class Contact(models.Model):
    name  = models.CharField(max_length = 128)
    email       = models.EmailField(blank = True, null = True)
    phone       = models.CharField(max_length = 15)
    subject     = models.CharField(max_length = 128)
    message     = models.TextField()




class SocialMedia(models.Model): 
    SOCIAL_MEDIA_CHOICES = (('facebook','facebook'),('twitter','twitter'),('envelope-o','email'),('instagram','instagram'))
    title = models.CharField(max_length=100,choices=SOCIAL_MEDIA_CHOICES)
    link = models.URLField()

    def __str__(self):
        return str(self.link)

class GroupofCompany(models.Model):
    

    pass