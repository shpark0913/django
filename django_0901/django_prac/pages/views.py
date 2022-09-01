from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name' : 'park'
    }
    return render(request, 'pages/index.html', context)