from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from user.models import User

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        return redirect("/todo/")
    elif request.method =="GET":
        return render(request, 'user/signup.html')
    else:
        return HttpResponse("Invalid request method", setatus=405)
    

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/admin/")
        else:
            return HttpResponse("Invalid auth", setatus=401)
    elif request.method == "GET":
        return render(request, "user/login.html")
    else:
        return HttpResponse("Invalid request method", setatus=405)