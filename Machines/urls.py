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
from .views import MachinesListView, CreateMachine, EditMachine, MachineDelete, get_ital_price_view, get_info_price_view

app_name = 'Machines'
urlpatterns = [
    path('', MachinesListView.as_view(), name='machines'),
    # path('inactive/', InactiveMachinesListView.as_view(), name='inactive_machines'),
    path("add", CreateMachine.as_view(), name="add_machine"),
    # path('add_machine/<int:customer_id>', add_machine_from_customers, name='add_machine_from_customers'),
    path('<int:machine_id>', EditMachine.as_view(), name='edit_machine'),
    path('<int:machine_id>/delete/', MachineDelete.as_view(), name='delete_machine'),
    # path('search_machine', search_machine_view,  name='search_machine'),
    # path('search_inactive_machine', search_inactive_machine_view,  name='search_inactive_machine'),
    path('get_italy_price/<int:machine_id>', get_ital_price_view, name='get_italy_price'),
    path('get_info_price/<int:machine_id>', get_info_price_view, name='get_info_price'),

]






