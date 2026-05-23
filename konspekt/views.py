from django.shortcuts import render

def index(request):
    """Головна сторінка додатку"""

    return render(request, 'konspekt/index.html')
