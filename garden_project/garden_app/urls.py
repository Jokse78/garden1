from django.contrib import admin
from django.urls import path

from . import views
from .views import mano_veisles, vaisiu_poreikis



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mano_veisles/', views.mano_veisles, name='mano_veisles'),
    path('vaisiu_poreikis/<int:veisle_id>/', views.vaisiu_poreikis, name='vaisiu_poreikis'),
]
