from .models import *
from django.forms import ModelForm


class CreateVegiForm(ModelForm):
    class Meta:
        model = Vegitables
        fields = ('name','quantity')

class UpdateVegiForm(ModelForm):
    class Meta:
        model = Vegitables
        fields = ('name','quantity')