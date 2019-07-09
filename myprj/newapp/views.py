from django.shortcuts import render, redirect, get_object_or_404
from newapp.models import Tableone
from .forms import *
from django.contrib.auth import authenticate, login


# Create your views here.

def main(request):
    return render(request, 'main.html')

def works(request):
    return render(request, 'single.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def view(request):

    ob = Tableone.objects.all()

    return render(request, 'view.html', {"obj": ob})



def add(request):

    return render(request, 'add.html')




def index(request):
    form = Addform
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        obj = Tableone(username=name, password=password, email=email)
        obj.save()
        return redirect(view)
    return render(request, 'index.html', {'form': form})






def delete(request, id):
   obj = Tableone.objects.get(id=id)
   obj.delete()

   return render(request, 'home.html', {'b': obj})





def edit(request, id):
    form2id = get_object_or_404(Tableone, id=id)
    print(form2id)
    form2 = Addform(request.POST or None, instance=form2id)
    if request.method == 'POST':
        if form2.is_valid():
            form2.save()
            return redirect(view)
    return render(request, 'index.html', {'form': form2})


def loggin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect(home)
    return render(request, 'login.html')

def signup(request):
    signupform = SignupForm(request.POST or None)

    if signupform.is_valid():
        signupform.save()
        username = signupform.cleaned_data.get('username')
        raw_password = signupform.cleaned_data.get('password1')
        print(username)
        print(raw_password)
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        email = signupform.cleaned_data.get('email')
        user.email = email
        user.save()
        print(user)
        return redirect(home)
    return render(request, 'signup.html', {'form': signupform})
