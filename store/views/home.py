from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from django.views.decorators.http import require_http_methods


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')


    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

@require_http_methods(["GET"])
def store(request):

    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    if category_id:
        products = Product.get_all_products_by_categoryid(category_id)
    else:
        products = Product.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

@require_http_methods(["GET"])
def home(request):
    categorias = Category.get_all_categories()
    context = {'categorias' : categorias,}
    return render(request, "home.html", context)

@require_http_methods(["GET"])
def condiciones_uso(resquest):
    return render(resquest, 'html_static/condiciones_uso.html')

@require_http_methods(["GET"])
def privacidad(resquest):
    return render(resquest, 'html_static/privacidad.html')

@require_http_methods(["GET"])
def acerca_de(resquest):
    return render(resquest, 'acerca_de.html')