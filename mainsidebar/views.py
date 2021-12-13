from django.shortcuts import render


def sidebar(request):
    return render(request, "main-sidebar.html")