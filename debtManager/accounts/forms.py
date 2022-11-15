from urllib import request
from django import forms
from .models import Products
from .models import Usvers
from .models import User
from .models import Complaints
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext, gettext_lazy as _

class addProduct(forms.ModelForm):
    CAT_1 = 'Товар'
    CAT_2 = 'Услуга'
    CAT_3 = 'Соц_задача'

    CAT_CHOICES = (
        (CAT_1, u"Товар"),
        (CAT_2, u"Услуга"),
        (CAT_3, u"Соц_задача")
    )
    PR_1 = 'Продать'
    PR_2 = 'Купить'

    PR_CHOICES = (
        (PR_1, u"Продать"),
        (PR_2, u"Купить")
    )
    category = forms.ChoiceField(choices=CAT_CHOICES)
    wanttobuy = forms.ChoiceField(choices=PR_CHOICES)

    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'category', 'wanttobuy', 'phot')

class addComplaint(forms.ModelForm):

    class Meta:
        model = Complaints
        fields = ('title', 'description')

class RegisterUserForm(UserCreationForm):
  username = UsernameField(label = 'Логин', widget = forms.TextInput(attrs={'class': 'form-input'}))
  NKO = forms.CharField(label = "Название НКО", required=False, widget = forms.TextInput(attrs={'class': 'form-input'}))
  email = forms.EmailField(label = "Email", widget = forms.EmailInput(attrs={'class': 'form-input'}))
  phone = forms.CharField(label = "Номер телефона", widget = forms.TextInput(attrs={'class': 'form-input'}))
  #phone = forms.CharField(label = "Номер телефона", widget = forms.TextInput(attrs={'class': 'form-input'}))
  first_name = forms.CharField(label = "Имя", widget = forms.TextInput(attrs={'class': 'form-input'}))
  last_name = forms.CharField(label = "Фамилия", widget = forms.TextInput(attrs={'class': 'form-input'}))
  password1 = forms.CharField(label = "Пароль", widget = forms.PasswordInput(attrs={'class': 'form-input'}))
  password2 = forms.CharField(label = 'Повтор пароля', widget = forms.PasswordInput(attrs={'class': 'form-input'}))

  class Meta:
    model = User
    fields = ('username', 'NKO', 'email', 'phone', 'first_name', 'last_name', 'password1', 'password2')
