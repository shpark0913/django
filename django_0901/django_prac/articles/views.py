from django.shortcuts import render

# Create your views here.

def index(request):
    foods = ['apple', 'banana', 'carrot']
    info = {
        'name' : 'park',
        'hobby' : 'soccer',
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'articles/index.html', context)


def greeting(request):
    context = {
        'name' : 'park',
        'hobby' : 'soccer'
    }
    return render(request, 'greeting.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }

    return render(request, 'catch.html', context)


def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)