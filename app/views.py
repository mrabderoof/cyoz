# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from customers.models import Profile
from customers.filters import ProfileFilter
from django.core.paginator import Paginator

def tables(request):
    return render(request, 'tables.html')

def index(request):
    
    story_list = Profile.objects.order_by('user')
    story_filter = ProfileFilter(request.GET, queryset=story_list)

    paginator = Paginator(story_filter.qs, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'segment': 'index', "page_obj": page_obj, "filter": story_filter, 'value':'profiles'}
    
    return render(request, 'index.html', context)

def info(request):
    context = {'segment': 'info'}

    html_template = loader.get_template('info.html')
    return HttpResponse(html_template.render(context, request))

def dashboard(request):
    context = {'segment': 'dashboard'}

    html_template = loader.get_template('dashboard.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
