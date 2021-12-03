from django.shortcuts import render

def index(request):
#    return render(request, "pages/index.html")
     return render(request, 'pages/home.html')
