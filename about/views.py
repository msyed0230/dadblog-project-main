from django.shortcuts import render, get_object_or_404

from .models import About

def about(request):
    about = About.objects
    return render(request, 'about/about.html', {'about':about})

