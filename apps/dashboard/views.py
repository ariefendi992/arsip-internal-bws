from django.shortcuts import render


# Create your views here.
def index(request):

    context = {"titlePage": "Dashboard"}
    return render(request, "dashboard/index_dashboard.html", context)
