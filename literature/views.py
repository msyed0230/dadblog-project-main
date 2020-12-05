from django.shortcuts import render

from .models import Literature

def literature(request):
    literature = Literature.objects
    return render(request, 'literature/literature.html', {'literature':literature})
