from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=12000)
    date = models.DateField()

    def __str__(self):
        return self.date