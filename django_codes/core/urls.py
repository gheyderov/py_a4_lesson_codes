from django.urls import path
from core.views import home, about, ContactView, export_view

urlpatterns = [
    path('', home, name='home'),  
    path('export/', export_view, name='export'),  
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name = 'contact')
]
