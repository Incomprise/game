from django.http import HttpResponse
from django.shortcuts import render
from game.models import Character

def index(request):
    character = Character.objects.all()
    context = {'character': character}
    return render(request, 'game/index.html', context)