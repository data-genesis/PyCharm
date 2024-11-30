from django.urls import path
from . import views

urlpatterns = [
    path('', views.function_based_view, name='function_based_view'),  # Путь по умолчанию
    path('function/', views.function_based_view, name='function_based_view'),
    path('class/', views.class_based_view, name='class_based_view'),
]
