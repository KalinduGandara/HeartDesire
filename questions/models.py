from django.db import models

# Create your models here.
class Question(models.Model):
    questionNumber = models.IntegerField()
    questionPage = models.IntegerField()
    question = models.CharField(max_length=500)
    answer0 = models.CharField(max_length=500)
    answer1 = models.CharField(max_length=500)

class PersonalityTest(models.Model):
    E_ans = models.CharField(max_length=20)
    S_ans = models.CharField(max_length=20)
    T_ans = models.CharField(max_length=20)
    J_ans = models.CharField(max_length=20)
    E_value = models.CharField(max_length=20)
    S_value = models.CharField(max_length=20)
    T_value = models.CharField(max_length=20)
    J_value = models.CharField(max_length=20)
    Personality_type = models.CharField(max_length=20)
