from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product
    
class Cart(View):
    def get(self , request):
        cart = request.session.get('cart', {})  # Valor predeterminado: un diccionario vacío si 'cart' no está en la sesión
        ids = list(cart.keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )