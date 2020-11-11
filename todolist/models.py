from django.db import models

# Create your models here.

class Todolist(models.Model):
    text = models.CharField(max_length = 150)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    