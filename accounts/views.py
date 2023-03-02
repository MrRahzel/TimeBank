from django.shortcuts import render
from django.db import models

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib import messages
from .models import Usvers
from .models import Products
from .models import *
from .forms import RegisterUserForm
from .forms import *
from django.db.models import Sum

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.db import connection, reset_queries

def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            #phone = form.cleaned_data.get('phone')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user =authenticate(username=username,password=password, email=email, phone=phone, first_name=first_name, last_name=last_name)
            instance = Usvers(user = user, balance = 5, phone=phone)
            instance.save()
            login(request, user)
            
            return redirect('profile')
    else:
        form = RegisterUserForm()
    return render(request, 'signup.html', {'form': form})

def signupNKO(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            NKO = form.cleaned_data.get('NKO')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user =authenticate(username=username,password=password, email=email, phone=phone, first_name=first_name, last_name=last_name)
            instance = Usvers(user = user, balance = 5, phone=phone, is_NKO = True, NKO_name=NKO)
            instance.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterUserForm()
    return render(request, 'signupNKO.html', {'form': form})

def sign_b(request):

    return render(request, 'signup_before.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        msg=""
        if request.method == "POST":
            try:
                username = request.POST["username"]
                amount = request.POST["amount"]
                senderUser = User.objects.get(username=request.user.username)
                receiverrUser =  User.objects.get(username=username)
                sender = Usvers.objects.get(user = senderUser)
                receiverr = Usvers.objects.get(user = receiverrUser)
                if ((sender.balance > 0) and ((sender.balance - int(amount)) >= 0)):
                    sender.balance = sender.balance - int(amount)
                    receiverr.balance = receiverr.balance + int(amount)
                sender.save()
                receiverr.save()
                msg = "Transaction Success"
                return redirect('profile')
            except Exception as e:
                print(e)
                msg = "Transaction Failure, Please check and try again"
                return redirect('profile')
        data = Products.objects.all()
        databal = Usvers.objects.all().filter(is_superuser = False)
        #databal2 = databal.user_id > 1
        adm = User.objects.get(username='Admin1')
        adm2 = Usvers.objects.get(user=adm)
        #adm3 = databal - adm2
        total_sum = sum(data.values_list('price', flat=True))
        bal_sum = sum(databal.values_list('balance', flat=True))
        adm2.balance = total_sum - bal_sum
        adm2.save()
        usver = Usvers.objects.get(user=request.user)
        user2 = Usvers.objects.all()

        return render(request,'profile.html',{"balance":usver.balance, "NKO_name":usver.NKO_name, "is_NKO":usver.is_NKO, "phone":usver.phone,"msg":msg, "userlist" : user2})

import datetime
def totaldonation(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        object_list = Products.objects.all()
        msg=""
        if request.method == "POST":
            try:
                username = request.POST["username"]
                amount = request.POST["amount"]
                senderUser = User.objects.get(username=request.user.username)
                receiverrUser =  User.objects.get(username=username)
                sender = Usvers.objects.get(user = senderUser)
                receiverr = Usvers.objects.get(user = receiverrUser)
                vr = datetime.datetime.now()
                tr = Transacts.objects.create(user11 = sender, user22 = receiverr, colvo1 = amount, time1 = vr)
                if ((sender.balance > 0) and ((sender.balance - int(amount)) >= 0)):
                    sender.balance = sender.balance - int(amount)
                    receiverr.balance = receiverr.balance + int(amount)
                sender.save()
                receiverr.save()
                tr.save()

                msg = "Transaction Success"
                return redirect('profile')
            except Exception as e:
                print(e)
                msg = "Transaction Failure, Please check and try again"
                return redirect('profile')

        return render(request,'totaldonation.html')

def totaldonation2(request, id):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        object_list = Products.objects.get(id=id)
        msg=""
        if request.method == "POST":
            try:
                username = request.POST["username"]
                amount = request.POST["amount"]
                senderUser = User.objects.get(username=request.user.username)
                receiverrUser =  User.objects.get(username=username)
                sender = Usvers.objects.get(user = senderUser)
                receiverr = Usvers.objects.get(user = receiverrUser)
                vr = datetime.datetime.now()
                tr = Transacts.objects.create(user11 = sender, user22 = receiverr, colvo1 = amount, time1 = vr)
                if ((sender.balance > 0) and ((sender.balance - int(amount)) >= 0)):
                    sender.balance = sender.balance - int(amount)
                    receiverr.balance = receiverr.balance + int(amount)
                sender.save()
                receiverr.save()
                tr.save()

                msg = "Transaction Success"
                return redirect('profile')
            except Exception as e:
                print(e)
                msg = "Transaction Failure, Please check and try again"
                return redirect('profile')

        return render(request,'totaldonation2.html', {"object_list":object_list})

def advertisement(request, id):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        object_list = Products.objects.get(id=id)
        vr = datetime.datetime.now()
        name = request.GET.get("prod")
        view_c = Product_views.objects.create(user = request.user, product = name, time = vr)
        view_c.save()
        tel = User.objects.select_related("Usvers").all()
        
        return render(request,'advertisement.html', {"object_list":object_list, "tel":tel})

def transact(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        tr = Transacts.objects.all()
        selftr = Transacts.objects.filter(user11 = request.user.username)
        count = Transacts.objects.filter(user11 = request.user.username).count()
        context = {'transactions': tr, 'self_transactions': selftr, 'count':count}
        return render(request, 'transactions.html', context)

def cancel(request, id):
    #try:
    tran = Transacts.objects.get(id=id)
    us = Usvers.objects.all()
    a = tran.user11
    b = tran.user22
    a2 = User.objects.get(username = a)
    b2 = User.objects.get(username = b)
    a1 = Usvers.objects.get(user_id = a2.id)
    b1 = Usvers.objects.get(user_id = b2.id)

    c = tran.colvo1
    b1.balance = b1.balance - c
    a1.balance = a1.balance + c
    a1.save()
    b1.save()
    tran.delete()

    return redirect('transactions')

from django.http import HttpResponseRedirect

from .models import Products
from .forms import addProduct

def index(request):
    want = request.GET.get("want", 'sale')
    query = request.GET.get('search', '')
    z = len(query) - 3
    if query == '':
        if want == 'sale':
            posts = Products.objects.filter(wanttobuy="Продать").order_by('-id')
        elif want == 'buy':
            posts = Products.objects.filter(wanttobuy="Купить").order_by('-id')
    else:
        if want == 'sale':
            posts = Products.objects.filter(wanttobuy="Продать", name__iregex = query[z]).order_by('-id')
        elif want == 'buy':
            posts = Products.objects.filter(wanttobuy="Купить", name__iregex = query[z]).order_by('-id')
    if 'page' in request.GET:
        page = request.GET['page']
    else:
        page = 1
    paginator = Paginator(posts, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {"posts" : posts, "want": want, "page_c": page, 'query': query})


def product_views(request):
    views = Product_views.objects.all()
    count = Product_views.objects.all().count()
    return render(request, 'product_views.html', {'views': views, 'count':count})


def pj(request):
    
    return render(request, 'polojenie.html')


def pt(request):
    
    return render(request, 'partner.html')


def product(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        error = ''
        us = Usvers.objects.get(user=request.user)
        pr = Products.objects.all()
        if request.method == "POST":
            form = addProduct(request.POST, request.FILES)
            if form.is_valid():
                saving = form.save(commit=False)
                saving.user = request.user
                saving.save()
                #if (pr.description != form.cleaned_data["description"]):
                #    print('неккоректно')
                return redirect('ads')
            else:
                error = 'Некорректная форма'
        else:
            form = addProduct()
        context = {'form': form, 'error' : error, "is_NKO":us.is_NKO}
        return render(request, 'products.html', context)

def addcomplaint(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        error = ''
        if request.method == "POST":
            form = addComplaint(request.POST)
            if form.is_valid():
                saving = form.save(commit=False)
                saving.user = request.user
                saving.save()
                return redirect('profile')
            else:
                error = 'Некорректная форма'
        form = addComplaint()
        context = {'form': form, 'error' : error}
        return render(request, 'add_complaint.html', context)

def complaints(request):
    cmpl = Complaints.objects.all()
    count = Complaints.objects.all().count()
    return render(request,'complaints.html',{"cmpl" : cmpl, 'count':count})

def productreg(request):
    error = ''
    us = Usvers.objects.get(user=request.user)
    if request.method == "POST":
        for i in range(0, 3):
            print(i)
            form = addProduct(request.POST, request.FILES)
            if form.is_valid():
                saving = form.save(commit=False)
                saving.user = request.user
                saving.save()
                return redirect('profile')
            else:
                return redirect('productreg')
        return redirect('profile')
    form = addProduct()
    context = {'form': form, 'error' : error, "is_NKO":us.is_NKO}
    return render(request, 'productreg.html', context)

def ads(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        tovars = Products.objects.filter(user=request.user)
        count1 = Products.objects.filter(user=request.user, category="Товар", wanttobuy="Продать").count()
        count2 = Products.objects.filter(user=request.user, category="Услуга", wanttobuy="Продать").count()
        count3 = Products.objects.filter(user=request.user, wanttobuy="Купить").count()
        count4 = Products.objects.filter(user=request.user, category="Соц_задача").count()
        us = Usvers.objects.get(user=request.user)
        return render(request,'ads.html',{"tovars" : tovars, "is_NKO":us.is_NKO, "count1":count1, "count2":count2, "count3":count3, "count4":count4})

def edit(request, id):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        prod = Products.objects.get(user=request.user, id=id)

        if request.method == "POST":
            prod.name = request.POST.get("name")
            prod.description = request.POST.get("description")
            prod.price = request.POST.get("price")
            prod.save()
            return redirect('ads')
        else:
            print('Некорректная форма')

        return render(request, "edit.html", {"prod": prod})

def delete(request, id):
    prod = Products.objects.get(id=id)
    prod.delete()

    return redirect('ads')

def changeS(request, id):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        prod = Products.objects.get(user=request.user, id=id)

        if request.method == "POST":
            prod.price = request.POST.get("price")
            prod.to_who = request.POST.get("to_who")
            prod.is_saled = True
            prod.save()
            return redirect('ads')
        else:
            print('Некорректная форма')

        return render(request, "changeS.html", {"prod": prod})

def search(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        tovars = Products.objects.filter(user=request.user)
        query = request.GET.get('q', '')
        if query == "":
            object_list = ""
        else:
            z = len(query) - 3   
            ct = request.GET.get('ct')
            #display_type = request.GET.get("display_type", None)
            display_type = 'other'
            if (display_type == 'other'):
                x = request.GET.get('x')
                y = request.GET.get('y')
                if ((x == '') and (y == '')):
                    x = 0
                    y = 0
                    object_list = Products.objects.filter(name__iregex = query[z], category = ct, is_saled = False)
                else:
                    object_list = Products.objects.filter(name__iregex = query[z], price__range = (x, y), category = ct, is_saled = False)
            else:
                object_list = Products.objects.filter(name = query, category = ct, is_saled = False)

        return render(request, 'search.html',{"tovars" : tovars, 'object_list' : object_list, 'que' : query})

"""
class SearchResultsView(ListView):
    model = Products
    template_name = 'search.html'
    def get_queryset(self): # новый
        query = self.request.GET.get('q', '')
        if query != "":
            z = len(query) - 3
        ct = self.request.GET.get('ct')
        display_type = self.request.GET.get("display_type", None)
        #display_type = 'other'
        if (display_type == 'other'):
            x = self.request.GET.get('x')
            y = self.request.GET.get('y')
            if ((x == '') and (y == '')):
                x = 0
                y = 0
                object_list = Products.objects.filter(name__iregex = query[z], category = ct, is_saled = False)
            else:
                object_list = Products.objects.filter(name__iregex = query[z], price__range = (x, y), category = ct, is_saled = False)
        else:
            object_list = Products.objects.filter(name = query, category = ct, is_saled = False)
        return object_list
"""        

