from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings

from .models import *

def home(request):
    news = News.objects.order_by("-id")[:4]
    services = Service.objects.order_by("id")[:4]
    doctors = Doctor.objects.order_by("id")[:4]
    partners = Partner.objects.order_by("-id")[:4]
    images = Image.objects.order_by("-id")[:4]
    return render(request, 'home.html', {
        'news': news,
        'services': services,
        'doctors': doctors,
        'partners': partners,
        'images': images
    })


def news(request):
    Pag = Paginator(News.objects.order_by("-id"), 12)
    page = request.GET.get('page')
    news = Pag.get_page(page)

    return render(request, 'news.html', {
        'news': news
    })


def news_detail(request, id):
    n = News.objects.get(id=id)

    return render(request, 'news_detail.html', {
        'x': n
    })


def doctors(request):
    doctors = Doctor.objects.order_by("id")

    return render(request, 'doctors.html', {
        'doctors': doctors
    })


def services(request):
    services = Service.objects.order_by("id")

    return render(request, 'services.html', {
        'services': services
    })


def about(request):
    about = About.objects.order_by("id")

    return render(request, 'about.html', {
        'about': about
    })


def ourpartners(request):
    partners = Partner.objects.all()

    return render(request, 'ourpartners.html', {
        'partners': partners
    })


def fotogalereya(request):
    fotogalereya = Image.objects.order_by("-id")

    return render(request, 'fotogalereya.html', {
        'fotogalereya': fotogalereya
    })