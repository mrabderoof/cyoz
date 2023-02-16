# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('app/info/', views.info, name='info'),
    path('app/dashboard/', views.dashboard, name='dashboard'),

    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),

]
