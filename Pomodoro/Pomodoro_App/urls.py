from django.urls import path

from . import views

app_name = "Pomodoro"
urlpatterns = [
    path("", views.settings, name="settings"),
    path("timer/", views.pomodoro_timer, name="timer"),
    path("clock/",views.wallClock,name="clock"),
    path("delete-task/<int:task_id>/",views.deleteTask,name="task-deletion"),
]
