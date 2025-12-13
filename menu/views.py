from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


# @login_required
# def index(req):
#     item_list = Item.objects.all()
#     context = {"item_list": item_list}
#     return render(req, "menu/index.html", context)


@method_decorator(login_required, name="dispatch")
class IndexClassView(ListView):
    model = Item
    template_name = "menu/index.html"
    context_object_name = "item_list"


def detail(req, id):
    item = Item.objects.get(id=id)
    context = {"item": item}
    return render(req, "menu/detail.html", context)


@method_decorator(login_required, name="dispatch")
class DetailClassView(DetailView):
    model = Item
    template_name = "menu/detail.html"
    context_object_name = "item"


def create_item(req):

    form = ItemForm(req.POST or None)

    if req.method == "POST":
        if form.is_valid():
            print("residam")
            form.save()
            return redirect("menu:index")
        else:
            print(form.errors)

    context = {"form": form}
    return render(req, "menu/item-form.html", context)


class ItemCreateView(CreateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    template_name = "menu/item-form.html"

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


# def update_item(req, id):
#     item = Item.objects.get(id=id)
#     form = ItemForm(req.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect("menu:index")
#     context = {"form": form}
#     return render(req, "menu/item-form.html", context)


class UpdateClassView(UpdateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    template_name = "menu/item-form.html"

    def get_queryset(self):
        return Item.objects.filter(user_name=self.request.user)


# def delete_item(req, id):

#     item = Item.objects.get(id=id)
#     if req.method == "POST":
#         item.delete()
#         return redirect("menu:index")
#     return render(req, "menu/delete_item.html")


class DeleteClassView(DeleteView):
    model = Item
    template_name = "menu/delete_item.html"
    success_url = reverse_lazy("menu:index")
