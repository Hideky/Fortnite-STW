from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.core.paginator import Paginator
from wagtail.core.models import Page
from .models import ArticlePage, GuidePage, AnswerPage
import requests

def index(request):
    """Return Index View"""
    articles = ArticlePage.objects.all().order_by('-first_published_at')
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    context = {
        'last_articles': paginator.get_page(page)
    }
    return render(request, 'mainapp/index.html', context)

def about(request):
    """Return About View"""
    return render(request, 'mainapp/about.html')

def guides(request):
    """Return Guides View"""
    articles = GuidePage.objects.all().order_by('-first_published_at')
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    context = {
        'last_guides': paginator.get_page(page)
    }
    return render(request, 'mainapp/guides.html', context)

def streamers(request):
    """Return Streamers View"""
    streamers = requests.get("https://api.twitch.tv/kraken/streams/?community_id=ad656dbf-b45e-4b4c-8265-6917fc55e0a1", headers={'Client-ID': 'wsrzzhn3ssyklusb3esisf2iz96xu9', 'Accept': 'application/vnd.twitchtv.v5+json'}).json()['streams']
    paginator = Paginator(streamers, 9)
    page = request.GET.get('page')
    context = {
        'streamers': paginator.get_page(page)
    }
    return render(request, 'mainapp/streamers.html', context)

def faq(request):
    """Return FAQ View"""
    answers = AnswerPage.objects.all()
    context = {
        'answers': answers
    }
    return render(request, 'mainapp/faq.html', context)

def contact(request):
    """Return Contact View"""
    return render(request, 'mainapp/contact.html')