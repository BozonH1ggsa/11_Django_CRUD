from django import forms
from CRUD.models import Crud


class RegUserForm(forms.ModelForm):
    class Meta:
        model = Crud
        fields = [
            'name',
            'email',
        ]