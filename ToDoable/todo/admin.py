from django.contrib import admin

from todo.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display
    fieldsets = admin.ModelAdmin.fieldsets


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display
    fieldsets = admin.ModelAdmin.fieldsets
