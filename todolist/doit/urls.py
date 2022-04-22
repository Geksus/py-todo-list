from django.urls import path

from doit.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagDeleteView,
    TagCreateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("doit/", TaskCreateView.as_view(), name="task-create"),
    path("doit/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("doit/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag-form"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "doit"
