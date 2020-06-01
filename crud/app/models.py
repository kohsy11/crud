from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    due = models.DateTimeField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'todos', default = "")

    def __str__(self):
        return self.title

class Comments(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name = 'comments')
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments', default = "")