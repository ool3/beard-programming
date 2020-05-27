from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'main/base.html')


def task_template_page(request):
	return render(request, 'main/tasks_template.html')