from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        post_data = request.POST
        first_name = post_data.get('firstname')
        last_name = post_data.get('lastname')
        phone = post_data.get('phone')
        email = post_data.get('email')
        password = post_data.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "Primer nombre es requerido!!"
        elif len(customer.first_name) < 4:
            error_message = 'Primer nombre deberia tener al menos 4 o mas caracteres '
        elif not customer.last_name:
            error_message = 'El apellido es requerido'
        elif len(customer.last_name) < 4:
            error_message = 'El apellido deberia tener al menos 4 o mas caracteres'
        elif not customer.phone:
            error_message = 'El telefono es requerido'
        elif len(customer.phone) < 10:
            error_message = 'El telefono debe tener al menos 10 caracteres'
        elif len(customer.password) < 6:
            error_message = 'La contraseña debe tener al menos 6 caracteres'
        elif len(customer.email) < 5:
            error_message = 'El email debe tener al menos 5 caracteres'
        elif customer.isExists():
            error_message = 'La direccion email ya esta registrada..'
        # saving

        return error_message
