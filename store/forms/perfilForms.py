from django import forms
from store.models.perfil import UserProfile
from store.models.customer import Customer
from store.models.product import Product


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["img", "bio"]


class MyUserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "phone", "email"]


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "image",
            "price",
            "stock",
        ]

class ContactoForms(forms.Form):
    nombre = forms.CharField(label='Su nombre y apellido', required=True, widget=forms.TextInput(attrs={'class':'form-control border', 'placeholder':'Introduzca sus datos'}))
    correo = forms.EmailField(label='Correo Electrónico', required=True, widget=forms.EmailInput(attrs={'class':'form-control border', 'placeholder':'Introduzca su correo'}))
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escriba aquí su mensaje...','rows':5}))

class ContactoMensajeForms(forms.Form):    
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe alguna sugerencia o reclamo sobre la página...','rows':5}))