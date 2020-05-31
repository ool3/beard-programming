from django.urls import path, include
from .views import (
    new_tasks,
    TaskDetailView,
    posts_easy,
    posts_somewhat,
    posts_hard,
    home,
    TaskCommentView,
    task_solution,
    user,
)

urlpatterns = [
    path("", home, name="home"),
    path("task_template/<int:pk>/", TaskDetailView.as_view(), name="task_template"),
    path(
        "task_template/<int:pk>/comments/",
        TaskCommentView.as_view(),
        name="task_comment",
    ),
    path("task_template/<int:pk>/solution/", task_solution),
    path("easy/", posts_easy, name="easy"),
    path("user/", user, name="user"),
    path("somewhat/", posts_somewhat, name="somewhat"),
    path("hard/", posts_hard, name="hard"),
    path("new_tasks/", new_tasks, name="new_tasks"),
]
