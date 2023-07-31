from grocery_store.inventory.models import Delivery
from django import forms


class DeliveryAddForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['product', 'delivery_date', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the form fields here (e.g., add labels, help texts, etc.)
        # For example, you can change the delivery_date widget to use a DateInput:
        self.fields['delivery_date'].widget = forms.DateInput(attrs={'type': 'date'})