from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def index(request):
    data=Student.objects.all()
    context={'data':data}
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def insertdata(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        #return render(request,'index.html')
        return redirect('index')
def update(request,id):
    d=Student.objects.get(id=id)
    context={'d':d}
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        #return render(request,'edit.html',context)
        return redirect('index')
    return render(request,'edit.html',context)
def delete(request,id):
    x=Student.objects.get(id=id)
    x.delete()
    return redirect('index')
