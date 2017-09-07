from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms import ContactForm
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            company = form.cleaned_data['company']
            message = form.cleaned_data['message']

            template = get_template('core/contact_template.txt')
            context = {
                'name': name,
                'email': email,
                'phone': phone,
                'company': company,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                "new contact form submission",
                content,
                "Your website" +'',
                ['bacarlino@gmail.com'],
                headers = {'Reply-To': email }
            )
            email.send()
            messages.success(request, 'Thank you for your inquiry! We will be in touch.')
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})
