from django.shortcuts import render

# Create your views here.

def dashboard(request):
    if request.method == "POST":
        return render(request,'dashboard.html',{"show":True})
    return render(request,'dashboard.html',{"show":False})