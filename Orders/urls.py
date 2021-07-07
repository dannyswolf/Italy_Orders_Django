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
from .views import OrdersListView, OrdersEdit, OrderDelete

app_name = 'Orders'
urlpatterns = [
    path('', OrdersListView.as_view(), name='orders'),
    # path('inactive/', InactiveMachinesListView.as_view(), name='inactive_machines'),
    # path("add_machine", CreateMachine.as_view(), name="add_machine"),
    # path('add_machine/<int:customer_id>', add_machine_from_customers, name='add_machine_from_customers'),
    path('<int:order_id>', OrdersEdit.as_view(), name='edit_order'),
    path('<int:order_id>/delete/', OrderDelete.as_view(), name='delete_order'),
    # path('search_machine', search_machine_view,  name='search_machine'),
    # path('search_inactive_machine', search_inactive_machine_view,  name='search_inactive_machine'),
    # path('transfer/<int:machine_id>', TransferMachine.as_view(), name='transfer_machine'),

]






