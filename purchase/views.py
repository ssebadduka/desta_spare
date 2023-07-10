from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import NewStockForm
from .models import NewStockModel
from inventory.models import InventoryModel
# Create your views here.


@login_required
def purchase_stock(request):
    if request.method == 'POST':
        form = NewStockForm(request.POST)
        if form.is_valid():
            sku = form.cleaned_data['sku']
            supplier = form.cleaned_data['supplier']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            total_price = quantity * price

            model = NewStockModel(sku=sku, supplier=supplier, quantity=quantity, price=price, total_price=total_price)
            model.save()

            inventory = get_object_or_404(InventoryModel, sku=sku)
            inventory.available_quantity += quantity
            inventory.save()
            return HttpResponseRedirect(reverse('purchase-history'))
    else:
        return render(request, 'purchase/purchase_stock.html', {
            'form': NewStockForm
        })


@login_required
def purchase_history(request):
    purchases = NewStockModel.objects.all()
    return render(request, 'purchase/purchase_history.html', {
        'purchases': purchases
    })


@login_required
def delete_purchase(request, order_no):
    model = NewStockModel.objects.get(order_no=order_no)
    model.delete()
    return HttpResponseRedirect(reverse('purchase-history'))
