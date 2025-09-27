from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LoginView

from .models import Student
from .forms import StudentForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "There was an error with your signup. Please check the form and try again.")
    else:
        form = UserCreationForm()
    return render(request, 'students/signup.html', {'form': form})


def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'students/login.html', {'form': form})



@staff_member_required
def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = UserCreationForm()
    return render(request, 'students/add_user.html', {'form': form})


def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk = id) 
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            try:
                new_student = form.save()  
                return render(request, 'students/add.html', {
                    'form': StudentForm(),
                    'success': True
                })
            except Exception as e:
                # If save fails, add error message
                messages.error(request, f"Error saving student: {str(e)}")
        else:
            # Form is not valid, add error message
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {
        'form': form
    })


def edit(request, id):
    student = get_object_or_404(Student, pk=id)

    # Check if the user is a superuser
    if request.user.is_superuser:
        if request.method == 'POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid(): 
                form.save()
                return render(request, 'students/edit.html', {
                    'form': form,
                    'success': True
                })
        else:
            form = StudentForm(instance=student)
    else:
        return redirect('index')  

    return render(request, 'students/edit.html', {
        'form': form
    })

def delete(request, id):
    # Check if the user is a superuser
    if request.user.is_superuser and request.method == 'POST':
        student = get_object_or_404(Student, pk=id)
        student.delete()
        return HttpResponseRedirect(reverse('index'))

    return redirect('index')  
