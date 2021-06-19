from django.forms import ModelForm
from django import forms

from ordenamiento.models import Parroquia, \
        Barrio_Ciudadela

class ParroquiaForm(ModelForm): 
    class Meta:
        model = Parroquia 
        fields = ['nombre', 'tipo'] 


class Barrio_CiudadelaForm(ModelForm): 
    class Meta:
        model = Barrio_Ciudadela 
        fields = ['nombre', 'numViviendas', 'numParques', 'numEdif', 'parroquia'] 


class Parr_BarrioForm(ModelForm): 
    
    def __init__(self, parroquia, *args, **kwargs):
        super(Parr_BarrioForm, self).__init__(*args, **kwargs)
        self.initial['parroquia'] = parroquia
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        
    class Meta:
        model = Barrio_Ciudadela 
        fields = ['nombre', 'numViviendas', 'numParques', 'numEdif', 'parroquia'] 