from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from todo.models import Todo

# Create your views here.
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        context = {
            "todos":todos,
        }
        return render(request, 'todo/index.html', context)
    else:
        return HttpResponse("Invalid request method", setatus=405)

@csrf_exempt
def create(request):
    if request.method == "POST":
        Todo.objects.create(content=request.POST["content"])
        return redirect("/todo/")
    elif request.method =="GET":
        return render(request, 'todo/create.html')
    else:
        return HttpResponse("Invalid request method", setatus=405)
  