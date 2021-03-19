"""."""

# Django
from wds_store.shirts.models import Producto
from django import forms

class ProductoCreateForm(forms.Form):
    """."""
    producto = forms.CharField(
        min_length=2, 
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese un tipo de producto'
            }
        )
    )

    def save(self):
        data = self.cleaned_data

        producto = Producto.objects.create(**data)