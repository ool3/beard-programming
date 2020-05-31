from django import forms
from .models import Task, Category, Comment

# choices = [('coding', 'coding'), ('sports', 'sports'), ('games', 'games')]
choices = Category.objects.all().values_list("name", "name")
choice_list = []
for item in choices:
    choice_list.append(item)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("article", "lvl", "textarea", "examples", "tests")
        widgets = {
            "article": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Напишите название"}
            ),
            "lvl": forms.Select(choices=choice_list, attrs={"class": "form-control"}),
            "textarea": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Напишите что-нибудь полезное :)",
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_text",)
