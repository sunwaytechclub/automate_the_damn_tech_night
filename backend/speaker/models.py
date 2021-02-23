from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=29)
    position = models.CharField(max_length=323)
    avatar = models.ImageField(upload_to="speakers")