from django import forms

from grocery_store.product.models import Product


class BaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'product_image', 'description', 'product_quantity', 'category']

        widgets = {
            'name': forms.TimeInput(
                attrs={
                    'placeholder': "Product name",
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter price',
                }
            ),
            'product_quantity': forms.NumberInput(
                attrs={
                    'placeholder': 'Quantity',
                }
            ),
            'product_image': forms.URLInput(
                attrs={
                    'placeholder': 'Link to images',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                }
            ),
        }


class ProductAddForm(BaseForm):
    pass


class ProductEditForm(BaseForm):
    pass


class ProductDeleteForm(BaseForm):
    hidden_field = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                'disabled': 'disabled',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
