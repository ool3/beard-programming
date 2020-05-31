from django.contrib.auth.models import User


def add_variable_to_context(request):
    if request.user.is_authenticated:
        username = User.objects.get(pk=request.user.id).username
        exp = User.objects.get(pk=request.user.id).profile.progress
        return {"username": username, "exp": exp}

    return {}
