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


class HomeView(ListView):
    model = Task
    template_name = "main/home.html"
    cats = Category.objects.all()
    ordering = ["-post_date"]

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = "main/tasks_template.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        # context = super(TaskDetailView, self).get_context_data(*args, **kwargs)

        context = {}

        stuff = get_object_or_404(
            Task, id=self.kwargs["pk"])  # получаем id поста

        total_likes = stuff.total_likes()
        article = stuff.article
        textarea = stuff.textarea
        liked = False

        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked  # context['liked'] - это для html
        context["article"] = article
        context["textarea"] = textarea
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)

        username = None
        if request.user.is_authenticated:
            username = request.user.username

        parser = Parser(username)
        parser.save_code(request.POST.get("code"))

        context['result'], context['process_time'], context['output'] = parser.process_code()
        print(parser.process_code())
        # parser.delete_files()
        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data(*args, **kwargs))


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    # post_id - название кнопки
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("task_template", args=[str(pk)]))
