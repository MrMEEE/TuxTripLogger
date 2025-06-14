from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class location(models.Model):
  user = models.ForeignKey(User,on_delete=models.PROTECT)
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  address = models.CharField(max_length=1024, blank=True, null=True)
  city = models.CharField(max_length=255, blank=True, null=True)
  postcode = models.CharField(max_length=20, blank=True, null=True)
  country = CountryField(blank_label='(select country)', blank=True, null=True)
  lat = models.FloatField(blank=True, null=True)
  lon = models.FloatField(blank=True, null=True)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class log(models.Model):
  user = models.ForeignKey(User,on_delete=models.PROTECT)
  description = models.CharField(max_length=255)
  fromloc = models.ForeignKey(location, related_name='from_location', on_delete=models.PROTECT)
  toloc = models.ForeignKey(location, related_name='to_location', on_delete=models.PROTECT)
  distance = models.FloatField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.description} ({self.fromloc} to {self.toloc}) on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
  