from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('task_template', task_template_page)
]