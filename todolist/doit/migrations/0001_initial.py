# Generated by Django 4.0.4 on 2022-04-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "tags",
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField()),
                ("completed", models.BooleanField(default=False)),
                ("tags", models.ManyToManyField(related_name="tags", to="doit.tag")),
            ],
            options={
                "db_table": "task",
                "ordering": ["completed", "-created_at"],
            },
        ),
    ]
