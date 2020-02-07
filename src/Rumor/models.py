from django.db import models
from src.RumorValidator import settings
# Create your models here.


class RumorManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(RumorManager, self).all(*args, **kwargs).order_by("timestamp")
        return qs

class Rumor(models.Model):
    rumor       = models.CharField(max_length=200, null=True)
    isReal      = models.BooleanField(default=True)
    province    = models.CharField(max_length=4, default = 'CN', choices=settings.PROVINCE_CHOICES)
    timestamp   = models.DateTimeField(auto_now_add=True, null=True)

    objects = RumorManager()

    def save(self, *args, **kwargs):
        super(Rumor, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.rumor)

    def __unicode__(self):
        return str(self.rumor)

