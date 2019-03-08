from django import forms
from .models import GarageSaleModel


class GarageSaleForm(forms.ModelForm):
    class Meta:
        model = GarageSaleModel
        fields = "__all__"