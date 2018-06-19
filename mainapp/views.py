from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from wagtail.core.models import Page
from .models import ArticlePage

def index(request):
    """Return Index View"""
    context = {
        'last_articles': Page.objects.filter(numchild=0).order_by('-first_published_at')[:6]
    }
    return render(request, 'mainapp/index.html', context)

def about(request):
    """Return About View"""
    return render(request, 'mainapp/about.html')

def guides(request):
    """Return Guides View"""
    return render(request, 'mainapp/guides.html')

def streamers(request):
    """Return Streamers View"""
    return render(request, 'mainapp/streamers.html')

def faq(request):
    """Return FAQ View"""
    return render(request, 'mainapp/faq.html')

def contact(request):
    """Return Contact View"""
    return render(request, 'mainapp/contact.html')

# def signup(request):
#     """Return Signup View"""
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'main/signup.html', {'form': form})

# def account(request):
#     """Return Account View"""
#     if request.user.is_authenticated:
#         if request.method == 'POST' and 'descriptionchange' in request.POST:
#             try:
#                 request.user.profile.description = request.POST.get('description')
#                 request.user.save()
#             except Exception:
#                 pass
#         return render(request, 'main/account.html')
#     return render(request, 'main/notlogged.html', status=401)