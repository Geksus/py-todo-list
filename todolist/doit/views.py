from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from doit.models import Task, Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("doit:tags")


class TagListView(generic.ListView):
    model = Tag


class TagDeleteView(generic.DeleteView):
    model = Task
    fields = ["name"]
    success_url = reverse_lazy("doit:tags")
    template_name = "doit/tag_delete.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("doit:tasks")


class TaskListView(generic.ListView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "tags", "completed"]
    success_url = reverse_lazy("doit:tasks")
    template_name = "doit/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("doit:tasks")
    template_name = "doit/task_delete.html"
