from django.shortcuts import render, HttpResponse


# render html tmplate
def home(request):
    return render(request, 'accounts/home.html')
