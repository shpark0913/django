from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'name' : 'park'
    }
    return render(request, 'index.html', context)


def greeting(request):
    foods = ['apple', 'kimchi', 'cheese']
    info = {
        'name' : 'Park',
        'hobby' : 'SLEEP'
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'greeting.html', context)


def dinner(request):
    pass


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