from django.db import models

# Create your models here.
class Todo(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDiscription = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle