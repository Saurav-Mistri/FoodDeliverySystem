from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mob_no = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=100)
    #created = models.DateField(auto_now=True)

    class Meta:
        db_table = "user"

