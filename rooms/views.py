from django.utils import timezone
from django.views.generic import ListView
from . import models


class HomeView(ListView):
    """ HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"


"""
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage

def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"pages": rooms})
    except EmptyPage:
        return redirect("/")
"""

