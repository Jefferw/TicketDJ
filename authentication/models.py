from django.db import models

# Create your models here.
class Helpdesk_User(models.Model):
    email=models.CharField(max_length=255)
    ephone_number=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    user_status=models.CharField(max_length=255)
    affiliation=models.CharField(max_length=255)