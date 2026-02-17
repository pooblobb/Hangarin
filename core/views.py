from django.shortcuts import render
from .models import Task

def index(request):
    # Get the status from the URL query parameters (if any)
    status_filter = request.GET.get('status')

    # Filter tasks based on the parameter, otherwise get all
    if status_filter:
        tasks = Task.objects.filter(status=status_filter)
    else:
        tasks = Task.objects.all()

    context = {
        'tasks': tasks,
        'current_status': status_filter # Pass status to template for highlighting
    }
    return render(request, 'core/index.html', context)