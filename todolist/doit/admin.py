from django.contrib import admin
from doit.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "content",
        "deadline",
        "completed",
    ]
    list_filter = ["tags"]
    search_fields = ["tags"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ["name"]
