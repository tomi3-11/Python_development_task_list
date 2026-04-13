from django.urls import path

from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("tasks/new/", views.task_create, name="task_create"),
    path("tasks/<int:task_id>/toggle/", views.task_toggle, name="task_toggle"),
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
]
