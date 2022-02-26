from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginuser, logout as logoutuser

# Create your views here.
def index(request):
    if request.method == 'POST':
        data = request.POST
        return render(request, "website/index.html", {
            "data": data,
        })

    return render(request, "website/index.html")

# Create your views here.
def login(request):
    print("login")
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user"))
    return render(request, 'website/index.html')

def register(request):
    ''' Function to register user '''

    if request.method == "POST":
        passwd = request.POST["password"]
        cpasswd = request.POST["cpassword"]
        if passwd in [None, ""]:
            return render(request, "website/index.html", {
                'error': 'Please fill details'
            })
        if not (passwd == cpasswd):
            return render(request, 'website/index.html', {
                'error': "Passwords don't match",
                # If possible, return data
            })
        else:
            username = request.POST["username"]
            users = User.objects.all()
            # Conditional to check if username is already taken or not
            if username in [i.username for i in users]:
                return render(request, 'website/index.html', {
                    'error': 'Username already taken'
                })
            else:
                # Collecting left out data
                firstname = request.POST["firstname"]
                lastname = request.POST["lastname"]
                email = request.POST["email"]
                plantname = request.POST["plantname"]
                
                # Creating user
                user = User.objects.create_user(username=username,
                                                password=passwd,
                                                first_name=firstname,
                                                last_name=lastname,
                                                email=email,
                                                plantname=plantname)
                
                # Logging in the user
                loginuser(request, user)

                return render(request, 'website/user.html', {
                    'plantname': user.plantname,
                })

    elif request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user"))
    return render(request, 'website/index.html')

def logout(request):
    LOGGED_IN = False
    logoutuser(request)
    return render(request, "website/index.html")

def user(request):
    ''' Display user webpage '''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        # Checking if entered credentials are right
        if user is not None:
            loginuser(request, user)
            # Getting user alarms
            plant = request.user.plantname
            return render(request, 'website/user.html', {
                'plantname': plant,
            })
        return render(request, "website/index.html", {
            'failed_msg': 'Invalid Credentials'
        })

    # If user entered tab without logging in
    elif not request.user.is_authenticated:
        return render(request, "website/index.html")
    else:
        # Getting user alarms
        plant = request.user.plantname
        return render(request, 'website/user.html', {
            'plantname': plant,
        })
