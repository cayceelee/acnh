from django.shortcuts import render
from .models import Section

# Create your views here.
def home(request):
    sections = Section.objects.filter(display=True)
    context = {
        'sections': sections, 
    }

    return render(request, 'base/index.html', context)