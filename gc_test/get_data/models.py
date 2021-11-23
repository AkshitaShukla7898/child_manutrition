from django.db import models
from datetime import date

# Create your models here.
GENDER_CHOICES = (
    ("",'Select'),
    (0, 'girl'),
    (1, 'boy'),
)
class Data(models.Model):
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.FloatField(max_length=3)
    weight = models.FloatField(max_length=3) #change to float
    height = models.FloatField(max_length=3)
    dob = models.DateField()


  #  @property
  #  def age(self):
  #      if self.dob != None:
  #          self.age = date.today()-self.dob



