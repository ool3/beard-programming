from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect  , Http404
# Create your views here.
class HomeView(ListView):
    model = Task
    template_name = 'main/home.html'
    cats = Category.objects.all()
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'main/tasks_template.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(TaskDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Task, id=self.kwargs['pk']) # получаем id поста
        article = stuff.article
        textarea = stuff.textarea
        examples = stuff.examples
        context['total_likes'] = total_likes
        context['article'] = article
        context['textarea'] = textarea
        context['examples'] = examples
        return context

		
