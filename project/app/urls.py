from django.urls import path
from . import views

app_name = 'logs'

urlpatterns = [
    path('', views.tordi, name='tordi'),
    path('index', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('parameter/', views.parameter, name='parameter'),
    path('view/<int:pk>/', views.view_las, name='view_las'),
    path('api/curve/<int:pk>/<str:curve_mnemonic>/', views.curve_api, name='curve_api'),
]
