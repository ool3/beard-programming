from django.urls import path, include
from .views import new_tasks, TaskDetailView, posts_easy, posts_somewhat, posts_hard, home

urlpatterns = [
    path("", home, name="home"),
    path("task_template/<int:pk>/", TaskDetailView.as_view(), name="task_template"),
    path("easy/", posts_easy, name="easy"),
    path("somewhat/", posts_somewhat, name="somewhat"),
    path("hard/", posts_hard, name="hard"),
    path("new_tasks/", new_tasks, name="new_tasks"),
]
