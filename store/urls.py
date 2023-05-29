from django.urls import path
from .views import ShopView, CartView, ProductSingleView

urlpatterns = [
    path('', ShopView.as_view()),
    path('cart/', CartView.as_view()),
    path('product/', ProductSingleView.as_view())
]
