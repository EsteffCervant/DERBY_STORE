from django import forms

class AgregarPatinesForm(forms.Form):
    Deporte = forms.CharField(max_length=22)
    Marca = forms.CharField(max_length=18)
    Talla = forms.IntegerField()
    

class BuscarPatinesForm(forms.Form):
    Deporte = forms.CharField(max_length=22, required=False)