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
    #url(r'^accounts/', include('django.contrib.auth.urls')),
    #url(r'^signup/', SignUpView.as_view(), name='signup'),
    re_path(r'^signup/$', signup, name='signup'),
    path('signup_start', sign_b, name='signup_before'),
    path('signupNKO', signupNKO, name='signupNKO'),
    #url(r'^login/', signup, name='signup'),
    path('', index, name='index'),
    #path('', custom_login, name='index'),
    path('profile/index/', index_in, name='index_in'),
    path('polojenie/', pj, name='polojenie'),
    #path('', custom_login, name='index'),
    path('profile/polojenie/', pj_in, name='polojenie_in'),
    path('partner/', pt, name='partner'),
    #path('', custom_login, name='index'),
    path('profile/partner/', pt_in, name='partner_in'),
    re_path(r'^profile/$', profile, name='profile'),
    #url(r'^profile/', userView.as_view, name='userlist'),
    #url(r'^profile/', userlist, name='uslist'),
    path('profile/tokensdonate', totaldonation, name='totaldonation'),
    path('profile/tokensdonate2/<int:id>/', totaldonation2, name='totaldonation2'),
    path('profile/transactions/', transact, name='transactions'),
    path('profile/transactions/cancel/<int:id>/', cancel),
    path('profile/mytransactions/', transact, name='self_transactions'),
    path('profile/', profile, name='userlist'),
    #path('profile/', totaldonation, name='balance'),
    #url(r'^products/', pr_button, name='products'),
    #path('products', pr_button, name='products'),
    path('profile/products', product, name='products'),
    path('profile/addcomplaint', addcomplaint, name='addcomplaint'),
    path('profile/complaints', complaints, name='complaints'),
    path('productreg', productreg, name='productreg'),
    path('profile/ads/', ads, name='ads'),
    path('profile/advertisement/<int:id>/', advertisement, name='advertisement'),
    path('profile/views/', product_views, name='product_views'),
    #path('profile/edit/<int:id>/', edit, name='edit'),
    #path('profile/ads/edit', edit, name='edit'),
    path('profile/ads/edit/<int:id>/', edit, name='edit'),
    path('profile/ads/delete/<int:id>/', delete),
    path('profile/ads/changeS/<int:id>/', changeS),
    path('profile/search/', search, name='search'),
    path('profile/search_results/', SearchResultsView.as_view(), name='search_results'),
    #path('profile/ads_other/', ads_other, name='ads_other'),
   # path('profile/', tovar, name='tovars'),


    #url(r'^profile/', UsersListView, name='userlist'),
    #url(r'^profile/', UsersListView, name='userlist'),
    #ListView.as_view(queryset = Usvers.objects.all, template_name="accounts/profile.html")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
