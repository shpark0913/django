from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('greeting/', views.greeting, name = 'greeting'),
    path('throw/', views.throw, name = 'dinner'),
    path('catch/', views.catch, name = 'catch'),
    path('hello/<name>', views.hello, name = 'hello'),
]
