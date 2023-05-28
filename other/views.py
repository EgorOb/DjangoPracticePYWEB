from datetime import datetime

from django.views import View
from django.http import HttpResponse
from random import random
from django.shortcuts import render


class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)


class RandomView(View):
    def get(self, request):
        random_number = random()
        return HttpResponse(random_number)


class HelloView(View):
    def get(self, request):
        return HttpResponse("""<h1>Hello, World</h1>""")


class IndexView(View):
   def get(self, request):
       return render(request, 'other/index.html')
