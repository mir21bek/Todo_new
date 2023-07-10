from django.db import models
from django.contrib.auth.models import User


class BlogModel(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'Active', 'Active'
        PROGRESS = 'Progress', 'Progress'
        DONE = 'Done', 'Done'

    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default='Active'
     )

    class Priority(models.TextChoices):
        HIGH = 'High', 'High'
        MEDIUM = 'Medium', 'Medium'
        LOW = 'Low', 'Low'

    priority = models.CharField(
        max_length=100,
        choices=Priority.choices,
        default='Medium'
    )

    title = models.CharField(max_length=150)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
