from django.urls import path

from .views import CurrentDateView, RandomView, HelloView, IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', CurrentDateView.as_view()),
    path('random/', RandomView.as_view()),
    path('hello/', HelloView.as_view()),
]
