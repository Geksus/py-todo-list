from django.urls import path

from todo.views import Index, TagView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("tags/", TagView.as_view(), name="tags"),
    path("create/",
         TaskCreateView.as_view(),
         name="task_create_view"),
    path("create/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task_update_view")
]

app_name = "todo"
