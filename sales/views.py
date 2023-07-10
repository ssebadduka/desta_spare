from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import SalesFormset, SalesFormHelper, CustomerForm
from .models import SalesModel, CustomerModel
from inventory.models import InventoryModel
# Create your views here.

@login_required
def new_sale(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        formset = SalesFormset(request.POST)
        formhelper = SalesFormHelper()

        invalid_request = False
        if customer_form.is_valid() and formset.is_valid():
            customer = customer_form.cleaned_data['customer']
            contact = customer_form.cleaned_data['contact']
            for form in formset:
                sku = form.cleaned_data['sku']
                quantity = form.cleaned_data['quantity']
                price = form.cleaned_data['price']
                total_price = quantity * price
                
                not_available = False
                inventory = get_object_or_404(InventoryModel, sku=sku)
                if quantity <= inventory.available_quantity:
                    cust_model = CustomerModel(customer=customer, contact=contact)
                    cust_model.save()
                    
                    model = SalesModel(customer=cust_model, sku=sku, quantity=quantity, price=price, total_price=total_price)
                    model.save()

                    inventory.available_quantity -= quantity
                    inventory.save()
                else:
                    not_available = True
                    return render(request, 'sales/new_sale.html', {
                        'customer_form': CustomerForm(),
                        'formset': SalesFormset(queryset=SalesModel.objects.none()),
                        'helper': formhelper,
                        'not_available': not_available
                    })
            return HttpResponseRedirect(reverse('sales-history'))
        else:
            invalid_request = True
            return render(request, 'sales/new_sale.html', {
                'invalid_request': invalid_request,
                'customer_form': CustomerForm(),
                'formset': SalesFormset(queryset=SalesModel.objects.none()),
                'helper': SalesFormHelper()
            })

    else:
        return render(request, 'sales/new_sale.html', {
            'customer_form': CustomerForm(),
            'formset': SalesFormset(queryset=SalesModel.objects.none()),
            'helper': SalesFormHelper()
        })


@login_required
def sales_history(request):
    model = SalesModel.objects.all()
    return render(request, 'sales/sales_history.html', {
        'model': model
    })


@login_required
def delete_sale(request, order_no):
    model = SalesModel.objects.get(order_no=order_no)
    model.delete()
    return HttpResponseRedirect(reverse('sales-history'))