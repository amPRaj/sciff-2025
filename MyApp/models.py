from django.db import models
import uuid


# Create your models here.
class Movie(models.Model):
    year = models.IntegerField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    dur = models.CharField(blank=True, null=True, max_length=20)
    dir = models.CharField(blank=True, null=True, max_length=120)
    screenplay = models.CharField(blank=True, null=True, max_length=120)
    prod = models.CharField(blank=True, null=True, max_length=120)
    title = models.CharField(max_length=120)
    desc1 = models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    file = models.FileField(upload_to='movies', default=None)
    image = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.title
