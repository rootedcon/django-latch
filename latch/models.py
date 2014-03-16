from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class LatchSetup(models.Model):
    latch_appid = models.CharField(max_length = 256, null = False, unique = True)
    latch_secret = models.CharField(max_length = 128, null = False,  unique = True)
    def __unicode__(self):
        return u'Latch Setup' 
    class Meta:
        verbose_name_plural = 'Latch Setup'


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    latch_accountId = models.CharField(max_length=128, default='', null = True, blank=True) 


