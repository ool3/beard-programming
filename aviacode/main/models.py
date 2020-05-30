from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import admin
import datetime


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_absolute_url(self):
        # перемещение пользователя после добавление нового поста
        return reverse("home")


class Task(models.Model):
    article = models.CharField("Название", max_length=120)
    lvl = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="postcategory"
    )
    textarea = models.TextField(max_length=5600)
    examples = models.TextField("Примеры", max_length=2000)
    post_date = models.DateField("Date", default=datetime.date.today)

    def __str__(self):
        return "{}".format(self.article)


class Comment(models.Model):
    article = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=350, verbose_name="текст комментария")

    def __str__(self):
        return self.comment_text[:15]
