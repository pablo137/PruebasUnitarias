from django.contrib import admin
from django.urls import path
from .views.home import Index, store, home, condiciones_uso, privacidad, acerca_de
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.perfil import view_profile, edit_profile
from .views.producto import crear_producto, ver_productos, editar_producto, eliminar_producto
from .views.contacto import contacto, contactanos
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('home', home, name='home'),
    path('condiciones', condiciones_uso, name='condiciones'),
    path('privacidad', privacidad, name='privacidad'),

    path('store', store, name='store'),
    path('contacto', contacto, name='contacto'),
    path('contactanos', contactanos, name='contactanos'),
    path('acerca_de', acerca_de, name='acerca_de'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),

    path('perfil/', auth_middleware(view_profile), name='perfil'),
    path('perfil/edit/', auth_middleware(edit_profile), name='edit_perfil'),

    path('ver_productos/', ver_productos, name='ver_productos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('editar_producto/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),

    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
