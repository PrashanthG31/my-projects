from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class userfill(models.Model):
       username = models.CharField(max_length=100)
       useremail = models.EmailField(max_length=255)
       event_name = models.CharField(max_length=100)
       user_address = models.TextField(default="")
       user_mobile = models.CharField(max_length=13,default="",validators=[RegexValidator(r'^\+91\s*[6-9]\d{9}$', message="Enter a valid Indian mobile number.")])
       select_event = models.CharField(max_length=100,default="")
       select_event_theme = models.CharField(max_length=100,default="")
       select_pack = models.CharField(max_length=100,default="")
       event_date = models.CharField(max_length=100,default="")
       event_date2 = models.CharField(max_length=100,default="")
       approx_people = models.IntegerField(default="")
       description = models.TextField(default="")
       status = models.CharField(max_length=50,default="")