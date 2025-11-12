from django.shortcuts import render, redirect
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

    form = ItemForm(req.POST or None)

    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("menu:index")

    if req.method == "GET":
        context = {"form": form}
        return render(req, "menu/item-form.html", context)

    return req


def update_item(req, id):
    item = Item.objects.get(id=id)
    form = ItemForm(req.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("menu:index")
    context = {"form": form}
    return render(req, "menu/item-form.html", context)


def delete_item(req, id):

    item = Item.objects.get(id=id)
    if req.method == "POST":
        item.delete()
        return redirect("menu:index")
    return render(req, "menu/delete_item.html")
