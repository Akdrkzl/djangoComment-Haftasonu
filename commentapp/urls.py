from django.urls import path
from .views import *


urlpatterns = [
    path('home/',index,name='index'),
    path('detay/',detay,name='detay'),
    path('sil/',sil,name='sil')
]
