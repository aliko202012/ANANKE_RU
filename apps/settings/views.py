from django.shortcuts import render
from apps.settings.models import BaseSettings
# Create your views here.

def settings(request):
    setting = BaseSettings.objects.latest('id')
    return render(request, "index.html", locals())