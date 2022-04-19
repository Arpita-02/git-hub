from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import admin_login
from .models import AddBook
# Create your views here.
def registration(request):
    return render(request, 'registration.html')
def login(request):
    return render(request,'login.html')   
def dashborad(request):
    return render(request,'dashborad.html')   

from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root",database='library')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="fname":
                fn=value
           
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into registration Values('{}','{}','{}')".format(fn,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'registration.html')
id=""
bn=""
sub=""
aut=""

#bdate=""
def addbook(request):
    global id,bn,sub,aut
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root",database='library')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id":
                id=value
           
            if key=="bname":
                bn=value
            if key=="sub":
                sub=value
            if key=="author":
                aut=value
            # if key=="bdate":
            #     bdate=value
        
        c="insert into addbook1 Values('{}','{}','{}','{}')".format(id,bn,sub,aut)
        cursor.execute(c)
        m.commit()
        # t=tuple(cursor.fetchall())
        # if t==():
        #     return render(request,'error.html')
        # else:
        #     return render(request,'http://127.0.0.1:8000/dashborad/')


    return render(request,"addbook.html")





em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root",database='library')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from registration where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"dashborad.html")

    return render(request,'login.html')


def addbook(request):
    Book = AddBook.objects.all()
    return render(request,'addbook.html',{'Book':Book})

def updatedetails(request,id=2):
    if request.session.has_key('is_logged'):
        if request.method=="POST":
                add=AddBook.objects.get(id=2)
                add.id=request.POST["id"]
                add.bname=request.POST["bname"]
                add.sub=request.POST["sub"]
                add.author=request.POST['author']
                add.save()
                return redirect("dashboard")
    return redirect('update.html')
def editbookdetails(request,id):
    if request.session.has_key('is_logged'):
        Book = AddBook.objects.get(id=2)
        return render(request,'update.html',{'Book':Book})
    return redirect('updatedetails/')
def deletebook(request,id):
    if request.session.has_key('is_logged'):
        AddBook_info = AddBook.objects.get(id=id)
        AddBook_info.delete()
        return redirect("dashboard")
    return redirect("login") 