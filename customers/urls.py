from django.urls import path
from customers import views
from .views import profile_view

urlpatterns = [

    path('customers/profile/', views.ProfileView.as_view(), name='profile'),
    # path('customers/profiles/', profiles, name='profiles'),
    path('profile/', profile_view, name='profile_view'), 
]
