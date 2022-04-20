from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class Index(generic.ListView):
    model = Task
    template_name = "todo/index.html"


class TagView(generic.ListView):
    model = Tag
    template_name = "todo/tags_view.html"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "todo/task_create_view.html"
    success_url = reverse_lazy("todo/index.html")
    fields = ("content", "deadline", "tags", "completed")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ("completed",)
    success_url = reverse_lazy("todo/index.html")
    template_name = "todo/task_create_view.html"
