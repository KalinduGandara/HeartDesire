from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    
    GENDER_TYPE = (('female', 'Female'),('male', 'Male'),('other', 'Other'))
    REL_TYPE = (('single', 'Singal'),('married', 'Married'),('divorced', 'Divorced'),('seperated', 'Seperated'),('widow', 'Widow'))
    
    personality_id = models.IntegerField()
    nic = models.CharField(max_length=20)
    gender = models.CharField(max_length=20,choices=GENDER_TYPE,default=None)
    rel_stats = models.CharField(max_length=20,choices=REL_TYPE,default=None)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    about = models.TextField()
    # profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)



