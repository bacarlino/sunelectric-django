from django.shortcuts import render, redirect
from core.forms import ContactForm
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


def contact(request):
    form_class = ContactForm

    if request.method == "POST":
        form = form_class(request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            template = get_template('core/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "new contact form submission",
                content,
                "Your website" +'',
                ['bacarlino@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'core/contact.html', {'form': form_class})
