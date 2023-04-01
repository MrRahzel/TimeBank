from django.db import models
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .apps import model_st

from .abstract_model_vector import Vector

from django.db.models.signals import post_save
from django.dispatch import receiver

#Для векторов
import math
import re
import seaborn as sns
import numpy as np
from scipy import spatial
from matplotlib import pyplot as plt
#import razdel
import pickle


# Create your models here.
from django.contrib.auth.models import User
class Usvers(models.Model):
  #usver = models.ForeignKey(User, on_delete=models.CASCADE)
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  balance = models.IntegerField(default = 0)
  NKO_name = models.CharField(max_length=100)
  phone = models.CharField(max_length=11, default = '00000000000')
  is_superuser = models.BooleanField(default = 0)
  is_NKO = models.BooleanField(default = False)
  #email =  models.CharField(max_length=200)

  def __str__(self):
    return self.user.username

   # def __init__(self, user, balance):
    #    """Инициализация"""
     #   self.name = user
      #  self.balance = balance

    #def __str__(self):
     #   return "{} {}".format(self.user, self.balance)


class Products(Vector):
  def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Файл слишком большой. Размер не должен превышать 2МБ')


  def file_size2(value): # add this to some file where you can import it from
    limit = 20
    if len(value) < limit:
        raise ValidationError('Длина описания меньше 20ти символов!')


  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  #usver = models.ForeignKey(Usvers, default = user, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.CharField(validators=[file_size2], max_length=500)
  price = models.IntegerField()
  category = models.CharField(max_length=200, default = 'Товар')
  is_saled = models.BooleanField(default = False)
  to_who = models.CharField(max_length=200, default=None, null=True, blank=True)
  phot = models.ImageField(upload_to='images/', default=None, null=True, validators=[file_size])
  wanttobuy = models.CharField(max_length=200, default = 'Продать')


  def __str__(self):
    return self.name
  
  """
  def array_dist(arr1,arr2):
    if len(arr1)!=len(arr2):
        raise TypeError('Length Difference')
    summ=0.0
    for i in range(len(arr1)):
        summ+= (arr1[i]-arr2[i])*(arr1[i]-arr2[i])
    return math.sqrt(summ)
  """

class Transacts(models.Model):
  user11 = models.CharField(max_length=200)
  user22 = models.CharField(max_length=200)
  colvo1 = models.IntegerField(default=None, null=True, blank=True)
  time1 = models.DateTimeField(default=None, null=True, blank=True)

  def __str__(self):
    return self.user11.username

class Complaints(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(validators=[MinLengthValidator(10)], max_length=500)

    def __str__(self):
      return self.title


class Product_views(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product = models.CharField(max_length=200)
  time = models.DateTimeField(default=None, null=True, blank=True)

class TransactionDetail(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)



#Обработчик сигнала(все будущие модели лучше писать над ним)
"""
@receiver(post_save, sender=Products, dispatch_uid="update_products_count")
def update_product(sender, instance, **kwargs):
  #count = Products.objects.all().count()
  instance.v10 = (model_st.encode(instance.description))[10]
  instance.save()
"""  
