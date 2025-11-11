from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm


def index(req):
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    return render(req, "menu/index.html", context)


def detail(req, id):
    item = Item.objects.get(id=id)
    context = {"item": item}
    return render(req, "menu/detail.html", context)


def create_item(req):
    form = ItemForm()
    context = {"form": form}
    return render(req, "menu/item-form.html", context)
