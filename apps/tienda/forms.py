from django import forms
from apps.tienda.models import Producto, Pc

class PcForm(forms.ModelForm):
    class Meta:
        modelo = Pc

        fields = ['productos']
