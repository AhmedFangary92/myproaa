from django import forms
from django.db.models import fields
from .models import List

class ListForm(forms.ModelForm) :
    class Meta :
        model = List
        fields = ['item', 'completed']