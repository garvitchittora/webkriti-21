from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        "test" :"test",
    }
    return render(request, "home.html",data)
