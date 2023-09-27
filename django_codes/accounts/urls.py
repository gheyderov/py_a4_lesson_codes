from django.urls import path
from accounts.views import register, login, logout, profile


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register')
]
