from django.urls import path
from .views import page

urlpatterns = [
    path('', page.home, name='home'),
    path('<int:service_id>/', page.detail, name='detail'),
    path('service/', page.makenstart, name='service'),

]