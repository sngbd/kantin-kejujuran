from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import User, Item, Balance
from .forms import CreateForm, BalanceBox, SortChoice


def index(request):
    a = Item.objects.order_by('-datetime')
    if request.method == "POST":
        form = SortChoice(request.POST)
        if form.is_valid():
            sort = form.cleaned_data['sort']
            if (sort == "DTASC"):
                a = Item.objects.order_by('datetime')
            elif (sort == "DTDSC"):
                a = Item.objects.order_by('-datetime')
            elif (sort == "NMASC"):
                a = Item.objects.order_by('name')
            elif (sort == "NMDSC"):
                a = Item.objects.order_by('-name')
    return render(request, "kantin/index.html", {
        "items": a,
        "title": "Available",
        "form": SortChoice
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        student_id = request.POST["student_id"]
        password = request.POST["password"]
        user = authenticate(request, username=student_id, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("kantin:index"))
        else:
            return render(request, "kantin/login.html", {
                "message": "Invalid Student ID and/or password."
            })
    else:
        return render(request, "kantin/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("kantin:index"))


def register(request):
    if request.method == "POST":
        student_id = request.POST["student_id"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "kantin/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            if len(student_id) != 5:
                return render(request, "kantin/register.html", {
                    "message": "Invalid Student ID."
                })
            sums = 0
            for i in student_id[:3]:
                sums += int(i)
            if sums != int(student_id[3:]):
                return render(request, "kantin/register.html", {
                    "message": "Invalid Student ID."
                })
            user = User.objects.create_user(student_id, email, password)
            user.save()
        except IntegrityError:
            return render(request, "kantin/register.html", {
                "message": "Account has been registered."
            })
        except:
            return render(request, "kantin/register.html", {
                "message": "Invalid Student ID."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("kantin:index"))
    else:
        return render(request, "kantin/register.html")

@login_required
def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            date_time = timezone.localtime().strftime("%B %d, %Y, %I:%M%p")
            a = Item(
                name=name, 
                description=description, 
                price=price, 
                image=image, 
                lister=request.user.username, 
                datetime=date_time
            )
            a.save()
            return HttpResponseRedirect(reverse('kantin:index'))
    else:
        return render(request, "kantin/create.html", {
            "form": CreateForm
        })


def item(request, id):
    data = Item.objects.get(id=f'{id}')
    if request.method == "POST":
        data.delete()
        return HttpResponseRedirect(reverse('kantin:index'))
    else:
        return render(request, "kantin/item.html", {
            "data": data,
        })
    

@login_required
def balance(request):
    if request.method == 'POST':
        form = BalanceBox(request.POST)
        if form.is_valid():
            bal = Balance.objects.get(id=1)
            b = form.cleaned_data['balance']
            if request.POST.get("Add"):
                bal.balance = bal.balance + b
            elif request.POST.get("Withdraw"):
                bal.balance = max(0, bal.balance - b)
            bal.save()
            return HttpResponseRedirect(reverse('kantin:balance'))
    else:
        b = Balance.objects.get(id=1)
        return render(request, "kantin/balance.html", {
            "form": BalanceBox,
            "balance": b.balance
        })