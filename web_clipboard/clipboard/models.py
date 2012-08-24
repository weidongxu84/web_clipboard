from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=256)
    ip_addr = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.username + self.ip_addr

class Clip(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    content_text = models.TextField()
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.pub_date + self.user
