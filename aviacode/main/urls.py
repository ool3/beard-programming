from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('task_template/', task_template_page, name='task_template'),
    
]