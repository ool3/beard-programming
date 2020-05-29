from django.shortcuts import render
from .models import Task, Category
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

from .code_processer.parse import Parser


def new_tasks(request):
    new = Task.objects.order_by('-id')[:10]
    context = {'new': new}
    return render(request, 'main/new_tasks.html', context)

def home(request):
    return render(request, 'main/home.html')


class TaskDetailView(DetailView):
    model = Task
    template_name = "main/tasks_template.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        # context = super(TaskDetailView, self).get_context_data(*args, **kwargs)

        context = {}

        stuff = get_object_or_404(Task, id=self.kwargs["pk"])  # получаем id поста

        article = stuff.article
        textarea = stuff.textarea
        examples = stuff.examples
        context["article"] = article
        context["textarea"] = textarea
        context["examples"] = examples
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)

        username = None
        if request.user.is_authenticated:
            username = request.user.username

        parser = Parser(username)
        parser.save_code(request.POST.get("code"))

        (
            context["result"],
            context["process_time"],
            context["output"],
        ) = parser.process_code()

        parser.delete_files()
        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        return render(
            request, self.template_name, context=self.get_context_data(*args, **kwargs)
        )

# Это все категории
def posts_easy(request):
    post = Task.objects.filter(lvl__name="easy")
    context = {
        'post': post,
    }
    return render(request, 'main/easy.html', context)

def posts_somewhat(request):
    post = Task.objects.filter(lvl__name="somewhat")
    context = {
        'post': post,
    }
    return render(request, 'main/somewhat.html', context)

def posts_hard(request):
    post = Task.objects.filter(lvl__name="hard")
    context = {
        'post': post,
    }
    return render(request, 'main/hard.html', context)