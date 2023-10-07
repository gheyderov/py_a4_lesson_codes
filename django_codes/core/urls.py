from django.urls import path
from core.views import home, about, ContactView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name = 'contact')
]
