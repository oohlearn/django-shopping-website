from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm

from .models import Item


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, "item/detail.html", {
        "item": item,
        "related_items": related_items
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            # 先存成一個物件，重點是要設定commit為false，不然會出錯
            item.created_by = request.user
            item.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()

    return render(request, "item/form.html", {
        'form': form,
        "title": "New Item"})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')
