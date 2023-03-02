from django.contrib import admin
from django.conf.urls import include
from .models import Usvers

from . import views
from .views import signup
#from .views import SignUpView
#from .views import profile, ads, edit
#from .views import UsersListView
from .views import *
from django.urls import path, re_path
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
#from .views import userView
#from .views import UsersListView
#from .views import ProductsView
#from .views import tovar

urlpatterns = [
    re_path(r'^signup/$', signup, name='signup'),
    path('signup_start', sign_b, name='signup_before'),
    path('signupNKO', signupNKO, name='signupNKO'),
    path('', index, name='index'),
    path('polojenie/', pj, name='polojenie'),
    path('partner/', pt, name='partner'),
    re_path(r'^profile/$', profile, name='profile'),
    path('profile/tokensdonate', totaldonation, name='totaldonation'),
    path('profile/tokensdonate2/<int:id>/', totaldonation2, name='totaldonation2'),
    path('profile/transactions/', transact, name='transactions'),
    path('profile/transactions/cancel/<int:id>/', cancel),
    path('profile/mytransactions/', transact, name='self_transactions'),
    path('profile/', profile, name='userlist'),
    path('profile/products', product, name='products'),
    path('profile/addcomplaint', addcomplaint, name='addcomplaint'),
    path('profile/complaints', complaints, name='complaints'),
    path('productreg', productreg, name='productreg'),
    path('profile/ads/', ads, name='ads'),
    path('profile/advertisement/<int:id>/', advertisement, name='advertisement'),
    path('profile/views/', product_views, name='product_views'),
    path('profile/ads/edit/<int:id>/', edit, name='edit'),
    path('profile/ads/delete/<int:id>/', delete),
    path('profile/ads/changeS/<int:id>/', changeS),
    path('profile/search/', search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
