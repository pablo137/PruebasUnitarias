import os
from venv import logger
from django.shortcuts import render, redirect
from django.urls import reverse
from store.forms.perfilForms import ContactoForms, ContactoMensajeForms
from django.core.mail import EmailMessage
from django.contrib import messages
from twilio.rest import Client
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def contacto(request):
    # print('Tipo de petición: {}'.format(request.method))
    contact_form = ContactoForms()
    
    if request.method == 'POST':
        # Estoy enviando el formulario
        contact_form = ContactoForms(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('nombre', '')
            email = request.POST.get('correo', '')
            message = request.POST.get('mensaje', '')

            # Enviar el correo electrónico
            email = EmailMessage(
                'Mensaje de contacto recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message),
                email,
                ['523a1a06ac16bd@inbox.mailtrap.io','dahofcmmejia@gmail.com'],
                reply_to=[email],
            )
            
            try:
                email.send()
                # Está todo OK
                return redirect(reverse('contacto')+'?ok')
            except Exception as e:
                # Ha habido un error y retorno a ERROR
                logger.error("Error al enviar correo: %s", str(e))
                return redirect(reverse('contacto')+'?error')

    return render(request, 'contacto.html', {'form':contact_form}) 

@require_http_methods(["POST"])
def contactanos(request):
    if request.method == 'POST':
        form = ContactoMensajeForms(request.POST, request.FILES)
        if form.is_valid():
            
            account_sid = 'AC6b6ffc0469b49c70652ce4bb9014adb3'
            
            
            auth_token = os.environ.get("AUTH_TOKEN", "Valor predeterminado si no se encuentra el secreto")
            # print(settings.TOKEN_TWILIO)
            client = Client(account_sid, auth_token)
            client.messages.create(
                from_='whatsapp:+14155238886',
                body=form.cleaned_data['mensaje'],
                to='whatsapp:+59164888167'
            )
            messages.success(request,"Ha sido enviado correctamente")
            
            return redirect('contactanos')
    else:
        form = ContactoMensajeForms()
    context = {'form': form}
    return render(request, 'contactanos.html', context)