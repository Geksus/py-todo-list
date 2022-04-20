from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        verbose_name_plural = "tasks"
        ordering = ["completed", "-created_at"]

    def __str__(self):
        if len(self.content) > 50:
            return self.content[:50] + "..."
        return self.content
