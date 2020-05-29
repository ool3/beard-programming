from django.urls import path, include
from .views import HomeView, TaskDetailView, posts_easy, posts_somewhat, posts_hard

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("task_template/<int:pk>/", TaskDetailView.as_view(), name="task_template"),
    path("easy/", posts_easy, name="easy"),
    path("somewhat/", posts_somewhat, name="somewhat"),
    path("hard/", posts_hard, name="hard"),
]
