from django.urls import path

from .views import CurrentDateView

urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
]
