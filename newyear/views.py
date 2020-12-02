from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.date
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })