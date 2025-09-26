from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from MyApp.models import Movie
from django.contrib.auth import logout
import json


# Create your views here.
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return render(request, 'index.html')


@login_required(login_url='/accounts/login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def movieList(request):
    obj = Movie.objects.filter().latest('create')
    mov = Movie.objects.all()
    return render(request, 'user_dashbord/browse.html', context={'mov': mov, 'lat': obj})


@login_required(login_url='/accounts/login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def details(request, name):
    mov = Movie.objects.get(title=name)
    return render(request, 'movieDetail.html', {'mov': mov})


@login_required(login_url='/accounts/login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def play_view(request, title):
    mov = Movie.objects.get(title=title)
    return render(request, 'user_dashbord/play.html', {'mov': mov})


@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'account/logout.html')


@login_required(login_url='/accounts/login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def dash(request):
    return render(request, 'user_dashbord/home.html')


@login_required(login_url='/accounts/login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def ser(request):
    return render(request, 'user_dashbord/search.html')


@login_required(login_url='/accounts/login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def res(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        try:
            obj = Movie.objects.get(title__iexact=title)
        except:
            return render(request, 'user_dashbord/search.html', {'err': 'Search Result Not Found'})
        return render(request, 'user_dashbord/search.html', {'res': obj})
    return render(request, 'user_dashbord/search.html')


@login_required(login_url='/accounts/login')
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def lat_view(request):
    last_ten = Movie.objects.all().order_by('-id')[:10]
    return render(request, 'user_dashbord/latest.html', {'lat': last_ten})
