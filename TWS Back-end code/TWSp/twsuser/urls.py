from django.urls import path
from . import views
urlpatterns = [
   path('register/', views.register, name='register'),
   path('login1/', views.login1, name='login1'),
]
