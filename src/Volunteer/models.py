from django.contrib.auth.models import AbstractUser
from django.db import models
class Volunteer(AbstractUser):
    region = models.CharField(max_length=3, null=True)
    def save(self, *args, **kwargs):
        super(Volunteer, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.region)

    def __unicode__(self):
        return str(self.region)
