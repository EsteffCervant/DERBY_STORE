from django import forms


class FormularioBase(forms.Form):
    Deporte = forms.CharField(max_length=22)
    Marca = forms.CharField(max_length=18)
    Talla = forms.IntegerField()  

class AgregarPatinesForm(FormularioBase):...
    
    
class EditarPatinesForm(FormularioBase):...
    

class BuscarPatinesForm(forms.Form):
    Deporte = forms.CharField(max_length=22, required=False)