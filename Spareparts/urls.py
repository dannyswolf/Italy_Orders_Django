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
from .views import SparepartsView, EditSpareParts, CreateSparepart, DeleteSparePart


app_name = 'Spareparts'
urlpatterns = [
    path("", SparepartsView.as_view(), name="list_spare_parts"),
    path("add", CreateSparepart.as_view(), name="create_spare_part"),
    # path("finished_jobs", FinishedCalendarListView.as_view(), name="finished_jobs"),
    # path("add_calendar/<int:machine_id>", create_calendar, name="add_calendar"),
    path('<int:spare_part_id>', EditSpareParts.as_view(), name='edit_sparepart'),
    # path('<int:service_id>/delete-files', delete_files, name='delete_files'),
    path('<int:spare_part_id>/delete/', DeleteSparePart.as_view(), name='delete_spare_part'),
    # path('search_calendar', search_calendar,  name='search_calendar'),
    # path('search_finished_calendar', search_finished_calendar,  name='search_finished_calendar'),
    # path('search_calendar_dte', search_calendar_dte,  name='search_calendar_dte'),
    # path('search_finished_calendar_dte', search_finished_calendar_dte,  name='search_finished_calendar_dte'),
    # path('calendar', CalendarView.as_view(),  name='calendar'),
    # path('finished_calendar', FinishedCalendarView.as_view(),  name='finished_calendar'),


]
