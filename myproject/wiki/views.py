from django.shortcuts import render, get_object_or_404
from .models import Hero

def hero_list(request):
    heroes = Hero.objects.all()
    return render(request, 'wiki/hero_list.html', {'heroes': heroes})

def hero_detail(request, hero_id):
    hero = get_object_or_404(Hero, id=hero_id)
    return render(request, 'wiki/hero_detail.html', {'hero': hero})