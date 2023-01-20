from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tag, Raca

@login_required
def novo_pet(request):
    if request.method == "GET":
        tags = Tag.objects.all()

        return render(request, 'novo_pet.html', {'Nome': 'Donda'})
