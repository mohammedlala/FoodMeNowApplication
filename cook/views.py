from django.contrib.auth.models import User
from user.models import Requirement, UserProfile
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CookProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def cookRegister(request):
    if request.method == 'POST':
        city = request.POST['city'].lower()
        area = request.POST['area'].lower()
        mobile = int(request.POST['mobile'])
        address = request.POST['address']
        firstname = request.POST['firstname'].lower()
        lastname = request.POST['lastname'].lower()
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']
        username = firstname + ' ' + lastname

        if CookProfile.objects.filter(firstname=firstname).exists() and CookProfile.objects.filter(lastname=lastname).exists():
            messages.warning(request, 'Name is already taken')
            return redirect('cook-register')

        elif CookProfile.objects.filter(email=email).exists():
            messages.warning(request, 'email is already taken')
            return redirect('cook-register')

        else:
            CookProfile.objects.create(
                email=email,
                password=password,
                firstname=firstname,
                lastname=lastname,
                address=address,
                gender=gender,
                city=city,
                area=area,
                mobile=mobile,
            )

            messages.success(request, f'Account Created For {firstname}')
            return redirect('cook-login')

    else:
        return render(request, 'cook/cook-register.html')


def cookLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        cook = CookProfile.objects.filter(
            email=email) and CookProfile.objects.filter(password=password)

        #user = authenticate(email=email, password=password)
        # print(cook)
        if cook:
            c = CookProfile.objects.filter(email=email).get()
            request.session['username'] = c.firstname+' '+c.lastname
            request.session['email'] = email
            return redirect('cook-home')
        else:
            messages.warning(request, 'Email or password is wrong')
            return redirect('cook-login')
    else:
        return render(request, 'cook/cook-login.html')


def cookLogout(request):
    del request.session['username']
    del request.session['email']
    return render(request, 'index.html')


def cookHome(request):
    if request.session.get('username'):
        return render(request, 'cook/cook-home.html')
    else:
        messages.warning(
            request, 'Your session has been expired, Kindly Logged-In again.')
        return redirect('cook-login')


def reqLoad(request):
    if request.session.get('username'):
        email = request.session.get('email')
        data = CookProfile.objects.get(email=email)
        details = Requirement.objects.filter(
            city=data.city, area=data.area).all()
        if details:
            return render(request, 'cook/req-result.html', {'req': details})
        else:
            messages.info(request, 'Oops...No Requirement Found in your area')
            return redirect('cook-home')
    else:
        messages.warning(
            request, 'Your session has been expired, Kindly Logged-In again.')
        return redirect('cook-login')


def reqDetails(request, id):
    if request.session.get('username'):
        requirement, u_id = Requirement.objects.filter(
            id=id).all(), Requirement.objects.get(id=id).user_id

        user, user1 = UserProfile.objects.filter(
            id=u_id).all(), User.objects.filter(id=u_id).all()

        return render(request, 'cook/req-details.html', {'requirement': requirement, 'user': user, 'user1': user1})
    else:
        messages.warning(
            request, 'Your session has been expired, Kindly Logged-In again.')
        return redirect('cook-login')
