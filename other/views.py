from datetime import datetime

from django.views import View
from django.http import HttpResponse


class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)
