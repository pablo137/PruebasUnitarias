from django.test import TestCase, Client
from django.urls import reverse
from store.views.home import Index

class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_Index_post_quantity_increment(self):
        response = self.client.post('', {'product': 'product_id', 'quantity': 'false'})
        request = response.wsgi_request
        request.session['cart'] = {'product_id': 3}
        response = Index.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(request.session['cart']['product_id'], 4)

    def test_Index_post_quantity_decrement(self):
        response = self.client.post('', {'product': 'product_id', 'remove': 'true'})
        request = response.wsgi_request
        request.session['cart'] = {'product_id': 3} 
        response = Index.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(request.session['cart']['product_id'], 2) 

    def test_Index_post_product_removal(self):
        response = self.client.post('', {'product': 'product_id', 'remove': 'true'})
        request = response.wsgi_request
        request.session['cart'] = {'product_id': 1}
        response = Index.as_view()(request)
        self.assertEqual(response.status_code, 302) 
        self.assertNotIn('product_id', request.session['cart']) 

    def test_Index_post_product_addition(self):
        response = self.client.post('', {'product': 'new_product', 'remove': 'false'})
        request = response.wsgi_request
        request.session['cart'] = {'product_id': 3}
        response = Index.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(request.session['cart']['new_product'], 1)  

    def test_Index_get(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 302)

    def test_store_view(self):
        response = self.client.get(reverse('store'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        # self.client.session.pop('cart', None)  # Elimina 'cart' de la sesión
        # response = self.client.get(reverse('store'))
        # self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('store') + '?category=1')
        self.assertEqual(response.status_code, 200) 
        

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_condiciones_uso_view(self):
        response = self.client.get(reverse('condiciones'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'html_static/condiciones_uso.html')

    def test_privacidad_view(self):
        response = self.client.get(reverse('privacidad'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'html_static/privacidad.html')

    def test_acerca_de_view(self):
        response = self.client.get(reverse('acerca_de'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'acerca_de.html')