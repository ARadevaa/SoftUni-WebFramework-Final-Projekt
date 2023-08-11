from django import forms

from grocery_store.product.models import Product

from django import forms


class SearchForm(forms.Form):
    search_text = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by product name...',
            },
        )
    )


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'disabled'
            field.widget.attrs['disabled'] = 'readonly'

