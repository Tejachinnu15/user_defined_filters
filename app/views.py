from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'Hai HeLlO bye Hai' }
    return render(request,'usdf.html',d)