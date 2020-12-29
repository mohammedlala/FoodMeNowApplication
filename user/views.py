from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Requirement, UserProfile
from cook.models import CookProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def userRegister(request):
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

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Name is already taken')
            return redirect('user-register')

        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'email is already taken')
            return redirect('user-register')

        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=firstname,
                last_name=lastname,
            )
            # user.save()
            UserProfile.objects.create(
                address=address,
                gender=gender,
                city=city,
                area=area,
                mobile=mobile,
                user=user,
            )

            messages.success(request, f'Account Created For {firstname}')
            return redirect('user-login')

    else:
        return render(request, 'user_register.html')


def userLogout(request):
    logout(request)
    return render(request, 'index.html')


@login_required
def userHome(request):
    return render(request, 'user-home.html')


def areaLoad(request):
    city = request.GET['name']
    areas = UserProfile.objects.filter(city=city).values('area').distinct()
    return render(request, 'shows.html', {'cities': areas})


@login_required
def searchCook(request):
    if request.method == 'POST':
        city = request.POST['city']
        area = request.POST['area']
        gender = request.POST['gender']

        cook = CookProfile.objects.filter(
            city=city, area=area, gender=gender).all()

        if cook:
            return render(request, 'search-result.html', {'cook': cook})

        else:
            messages.info(request, 'No Cook Found According to your Search')
            return redirect('user-home')
    else:
        return render(request, 'user-home.html')


@login_required
def resultDetail(request, email):
    cook = CookProfile.objects.filter(email=email)
    return render(request, 'result-detail.html', {'cook': cook})


@login_required
def reqCreate(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        gender = request.POST['gender']
        city = request.POST['city']
        area = request.POST['area']
        times = request.POST['times']
        age = request.POST['age']
        food = request.POST['food']
        food_category = request.POST['food_category']
        Requirement.objects.create(
            title=title,
            description=description,
            gender=gender,
            city=city,
            area=area,
            times=times,
            age=age,
            food=food,
            food_category=food_category,
            user=request.user
        )
        messages.success(request, f'Your Requirement has been Posted')
        return redirect('user-home')
    else:
        return render(request, 'req-form.html')
