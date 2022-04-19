from django.db import models

# Create your models here.
 
# Create your models here.
 
class admin_login(models.Model):
    admin_id = models.IntegerField()
    email = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    is_active = models.IntegerField(null=True)
 
    def __str__(self):
        return self.username
 
    admin_objects = models.Manager()

class AddBook(models.Model):
    id=models.IntegerField(primary_key="true")
    bname=models.CharField(max_length=50)
    sub=models.CharField(max_length=20)
    author= models.CharField(max_length = 30)
    #date=models.DateField()
    def __str__(self):
        return str(self.bname)+"["+str(self.id)+']'
    addbook=models.Manager()