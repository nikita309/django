from django.db import models

# Create your models here.
class msg(models.Model):
    id = models.IntegerField(primary_key=True)
    message = models.TextField()

    def __str__(self):
        return self.message
