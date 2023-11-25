import itertools

from django.shortcuts import render

from franc_products.models import Product
from france_slider.models import Slider
from franc_setting.models import SiteSetting
def Header(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Header.html', context)
def Footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request,"shared/Footer.html",context)


def my_grouper(n,iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))
def home_page(request):
    sliders = Slider.objects.all()
    most_visit_products = Product.object.order_by('-visit_count').all()[:8]
    latest_products = Product.object.order_by('-id').all()[:8]
    context = {
        'data': 'new data',
        'sliders': sliders,
        'most_visit': my_grouper(4,most_visit_products),
        'latest_products':my_grouper(4,latest_products),
    }
    return render(request, 'home_page.html', context)


def about_us(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request,'about_page.html',context)
