"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import BasketListView, EditBasket, BasketDelete, create_basket, make_order, java_script_add_to_basket

app_name = 'Basket'
urlpatterns = [
    path('', BasketListView.as_view(), name='basket'),
    path('click_to_add/', java_script_add_to_basket, name='click_to_add'),
    path('make_order', make_order, name="make_order"),
    path('add_to_basket/<int:spare_part_id>', create_basket, name='add_to_basket'),
    path('<int:basket_id>', EditBasket.as_view(), name='edit_basket'),
    path('<int:basket_id>/delete/', BasketDelete.as_view(), name='delete_basket'),

]






