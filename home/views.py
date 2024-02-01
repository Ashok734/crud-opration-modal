from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
# Create your views here.
def home(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }
    return render(request, "home/index.html", context)




def addNew(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        description = request.POST.get('description')

        if len(name)<2 or len(email)<2 or len(phone)<10 or len(location)<2:
            messages.error(request, "please fill correct field name")

        else:
            add_new = Student(name=name, email=email, phone=phone, location=location, description=description)
            add_new.save()
            messages.success(request, "Successfull added.")

            
        return redirect('home')
        

    # return render(request, "home/index.html")
def edit(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }


    return redirect(request, 'home', context)

def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        description = request.POST.get('description')

        if len(name)<2 or len(email)<2 or len(phone)<10 or len(location)<2:
            messages.error(request, "please fill correct field name")

        else:
            add_new = Student(id=id, name=name, email=email, phone=phone, location=location, description=description)
            add_new.save()
            messages.success(request, "Successfull added.")
            return redirect('home')

    # return redirect(request, 'index.html')

def delete(request, id):
    student = Student.objects.filter(id=id)
    student.delete()
    messages.success(request, "Successfull delete.")
    
    return redirect("home")

    

