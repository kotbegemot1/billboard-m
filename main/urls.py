from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('<str:page>', other_page, name='other'),
    path('', index, name='index'),

]