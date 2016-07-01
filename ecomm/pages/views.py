from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from products.models import Product
from .forms import ContactForm


def index(request):
    latest_products = Product.objects.all().order_by('-id')[:4]
    featured_products = Product.objects.filter(is_featured=True).order_by('-id')[:4]
    context = {
        "latest_products": latest_products,
        "featured_products": featured_products
    }
    return render(request, "pages/index.html", context)


def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = form(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('message', '')
            template = get_template('pages/contact-template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)
            email = EmailMessage("New contact form submission", content, "SeeChic",
                                 ['arahman.hamdy91@gmail.com'], headers={'Reply-To': contact_email})
            email.send()
            return redirect('pages:contact-success')

    return render(request, 'pages/contact.html', {
        'form': form,
    })


def contact_success(request):
    return render(request, "pages/contact-complete.html")


def handle_404_view(request):
    return render(request, "pages/404.html")
