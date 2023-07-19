from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username == "angaar" and password == "angaar":
            return redirect("success")
        
        else:
            return redirect("invalid")
    
    return render(request, "home.html")

def success(request):
    return render(request, "success.html")

def invalid(request):
    return render(request, "invalid.html")

