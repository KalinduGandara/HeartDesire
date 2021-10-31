from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserBio(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    age = models.CharField(max_length=50,)
    height = models.CharField(max_length=50,)
    weight = models.CharField(max_length=50,)
    salary = models.CharField(max_length=50,)

    EDU_TYPE = (('ol','O/L'),('al','A/L'),('diploma','Diploma'),( 'Bachdeg','Bachelor\'s degree'),('Mastdeg','Master\'s degree') , ('phd','Phd'))
    NAT_TYPE = (('sinhala','Sinhala'),('tamil','Tamil'),('muslim','Muslim'),( 'other','Other'))
    REL_TYPE = (('buddhism','Buddhism'),('christian','Christian'),('hindu','Hindu'),('islam','Islam'),( 'other','Other'))
    SKI_TYPE = (('very_dark','Very dark'),('dark_brown','Dark brown'),('mid_brown','Mid brown'),('medium','Medium'),( 'fair','Fair'),( 'light','Light'))
    EYE_TYPE = (('black','Black'),('brown','Brown'),('blue','Blue'),('gray','Gray'),( 'hazel','Hazel'))
    OCC_TYPE = (('government','Government'),('private','Private'))

    education = models.CharField(max_length=50,choices=EDU_TYPE,default=None)
    nationality = models.CharField(max_length=50,choices=NAT_TYPE,default=None)
    religion = models.CharField(max_length=50,choices=REL_TYPE,default=None)
    skin_complexity = models.CharField(max_length=50,choices=SKI_TYPE,default=None)
    eye_color = models.CharField(max_length=50,choices=EYE_TYPE,default=None)
    occupation = models.CharField(max_length=50,choices=OCC_TYPE,default=None)

class PatnertBio(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    age = models.CharField(max_length=50,)
    height = models.CharField(max_length=50,)
    weight = models.CharField(max_length=50,)
    salary = models.CharField(max_length=50,)

    EDU_TYPE = (('ol','O/L'),('al','A/L'),('diploma','Diploma'),( 'Bachdeg','Bachelor\'s degree'),('Mastdeg','Master\'s degree') , ('phd','Phd'))
    NAT_TYPE = (('sinhala','Sinhala'),('tamil','Tamil'),('muslim','Muslim'),( 'other','Other'))
    REL_TYPE = (('buddhism','Buddhism'),('christian','Christian'),('hindu','Hindu'),('islam','Islam'),( 'other','Other'))
    SKI_TYPE = (('very_dark','Very dark'),('dark_brown','Dark brown'),('mid_brown','Mid brown'),('medium','Medium'),( 'fair','Fair'),( 'light','Light'))
    EYE_TYPE = (('black','Black'),('brown','Brown'),('blue','Blue'),('gray','Gray'),( 'hazel','Hazel'))
    OCC_TYPE = (('government','Government'),('private','Private'))

    education = models.CharField(max_length=50,choices=EDU_TYPE,default=None)
    nationality = models.CharField(max_length=50,choices=NAT_TYPE,default=None)
    religion = models.CharField(max_length=50,choices=REL_TYPE,default=None)
    skin_complexity = models.CharField(max_length=50,choices=SKI_TYPE,default=None)
    eye_color = models.CharField(max_length=50,choices=EYE_TYPE,default=None)
    occupation = models.CharField(max_length=50,choices=OCC_TYPE,default=None)

class MatchingCouples(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='main_user')
    patner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='patner')

    prefereceMatching = models.FloatField()