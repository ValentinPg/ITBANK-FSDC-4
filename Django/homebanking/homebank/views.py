from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def vista(request):
    return render(request,"homebank/home.html")

# Create your views here.
