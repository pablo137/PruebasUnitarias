from django.shortcuts import render, redirect, get_object_or_404
from store.models.product import Product
from store.models.customer import Customer
from store.forms.perfilForms import ProductoForm
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def ver_productos(request):
    user_id = request.session.get("customer")
    user = Customer.objects.get(id=user_id)

    productos = Product.objects.filter(user=user)
    
    if productos.exists():

        return render(request, 'producto/ver_productos.html', {
            'productos': productos,
            'user':user,
            })
    else:
        mensaje = "No tienes productos actualmente."
        return render(request, 'producto/ver_productos.html', {
            'mensaje': mensaje,
            'user':user,
            })

@require_http_methods(["POST"])
def crear_producto(request):
    user_id = request.session.get("customer")
    user = Customer.objects.get(id=user_id)

    if request.method == 'POST':
        
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.user = user
            producto.save()
            return redirect('perfil')
    else:
        form = ProductoForm()
    return render(request,'producto/crear_producto.html', {'form': form,'user':user})

@require_http_methods(["POST"])
def editar_producto(request, producto_id):
    user_id = request.session.get("customer")
    user = Customer.objects.get(id=user_id)

    producto = get_object_or_404(Product, id=producto_id, user=user)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ver_productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'producto/editar_producto.html', {'form': form, 'producto': producto,'user':user})

@require_http_methods(["POST"])
def eliminar_producto(request, producto_id):
    user_id = request.session.get("customer")
    user = Customer.objects.get(id=user_id)
    
    producto = get_object_or_404(Product, id=producto_id, user=user)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    
    return render(request, 'producto/eliminar_producto.html', {'producto': producto,'user':user})