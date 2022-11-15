from django.db import models
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

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


class Products(models.Model):
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
