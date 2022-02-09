from datetime import timedelta

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from prices.models import PriceAction
# Create your views here.


def home(request):
    return render(request,'prices/home.html')


def short(request):
    items= PriceAction.objects.filter(created__gt=timezone.now()-timedelta(hours=1))
    return JsonResponse(list(items.values()),safe=False)
