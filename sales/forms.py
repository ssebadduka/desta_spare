from django import forms
from django.forms.models import modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button

from .models import SalesModel, CustomerModel


class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].widget.attrs.update({'class': 'mt-4 me-4'})
        self.fields['contact'].widget.attrs.update({'class': 'mt-4'})

    class Meta:
        model = CustomerModel
        fields = '__all__'
        labels = {
            'customer': 'Customer Name',
            'contact': 'Contact'
        },
        

class SalesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False

    class Meta:
        model = SalesModel
        exclude = ['customer', 'order_no', 'date', 'total_price']
        labels = {
            'item': 'item',
            'quantity': 'Quantity',
            'price': 'Price Per Quantity (Ugx)'
            }

SalesFormset = modelformset_factory(SalesModel, form=SalesForm)


class SalesFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Row(
                Column('item', css_class='mt-4 col '),
                Column('quantity', css_class='mt-4 col'),
                Column('price', css_class='mt-4 col'),
            ),
        Button('button', 'Add more', css_class='mt-2 btn btn-dark', css_id='add-more'),
        Button('button', 'Remove', css_class='ms-3 mt-2 btn btn-danger', css_id='remove'),
        Submit('submit', 'Save', css_class='ms-3 mt-2 btn btn-dark'),
        Button('cancel', 'Cancel', onclick="location.href = '/sales/sales-history/'", css_class='ms-3 mt-2 btn btn-dark'),
        )
