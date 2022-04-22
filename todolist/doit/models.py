from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

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
        ordering = ["completed", "-created_at"]
        db_table = "task"

    def __str__(self):
        return f"{self.content} - {self.tags}"
