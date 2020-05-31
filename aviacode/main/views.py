from django.shortcuts import render
from .models import Task, Category, Comment
from .forms import CommentForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User

from .code_processer.parse import Parser
from . import rating


def new_tasks(request):
    post_easy = Task.objects.filter(lvl__name="easy").order_by("-id")[:2]
    post_medium = Task.objects.filter(lvl__name="medium").order_by("-id")[:2]
    post_hard = Task.objects.filter(lvl__name="hard").order_by("-id")[:2]
    context = {
        "post_easy": post_easy,
        "post_medium": post_medium,
        "post_hard": post_hard,
    }
    return render(request, "main/new_tasks.html", context)


def home(request):
    return render(request, "main/home.html")


class TaskDetailView(DetailView):
    model = Task
    template_name = "main/tasks_template.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()

        context = {}

        stuff = get_object_or_404(Task, id=self.kwargs["pk"])  # получаем id поста

        article = stuff.article
        textarea = stuff.textarea
        examples = stuff.examples
        tests = stuff.tests

        context["article"] = article
        context["textarea"] = textarea
        context["examples"] = examples
        context["asserts"] = tests.asserts
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)

        if request.user.is_authenticated:
            username = request.user.username
        else:
            username = None

        parser = Parser(username)
        code = request.POST.get("code")
        asserts = context["asserts"]
        code_with_asserts = f"{code}\n\n{asserts}"
        parser.save_code(code_with_asserts)

        context["code"] = code

        (
            context["result"],
            context["process_time"],
            context["output"],
        ) = parser.process_code()
        parser.delete_files()

        MEM = 0

        if context["result"] is None:
            context["rating"] = rating.count(
                context["process_time"],
                context["tests"].etalon_time,
                MEM,
                context["tests"].etalon_memory,
            )
        else:
            context["rating"] = "F"

        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        return render(
            request, self.template_name, context=self.get_context_data(*args, **kwargs)
        )


# Это все категории
def posts_easy(request):
    post = Task.objects.filter(lvl__name="easy")
    context = {
        "post": post,
    }
    return render(request, "main/easy.html", context)


def posts_somewhat(request):
    post = Task.objects.filter(lvl__name="medium")
    context = {
        "post": post,
    }
    return render(request, "main/somewhat.html", context)


def posts_hard(request):
    post = Task.objects.filter(lvl__name="hard")
    context = {
        "post": post,
    }
    return render(request, "main/hard.html", context)


class TaskCommentView(DetailView):
    template_name = "main/tasks_comment.html"

    def get_context_data(self, *args, **kwargs):

        context = {}

        context["form"] = CommentForm()
        context["comments"] = Comment.objects.filter(article__id=self.kwargs["pk"])
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            correct_tusk = Task.objects.get(pk=self.kwargs["pk"])
            correct_author = User.objects.get(pk=request.user.id)
            comment = Comment(
                article=correct_tusk,
                author=correct_author,
                comment_text=request.POST.get("comment_text"),
            )
            comment.save()

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return render(request, self.template_name, context=context)
