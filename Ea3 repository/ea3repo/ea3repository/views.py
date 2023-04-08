from django.shortcuts import render
from .models import Artifact

def search_by_name(request):
    query = request.GET.get('q')
    artifacts = Artifact.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'artifacts': artifacts})

def search_by_level_layer(request):
    level = request.GET.get('level')
    layer = request.GET.get('layer')
    artifacts = Artifact.objects.filter(level__name=level, layer__name=layer)
    return render(request, 'search_results.html', {'artifacts': artifacts})
# Create your views here.
