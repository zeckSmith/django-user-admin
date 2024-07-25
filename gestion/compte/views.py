from django.shortcuts import render

# Create your views here.


def homme_view(request):

    return render(request, 'base.html')