from django.shortcuts import render
from .models import ContactUS
from france_contact.forms import CreateContactForm
from franc_setting.models import SiteSetting

def contact_page(request):
    contact_form = CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name  = contact_form.cleaned_data.get('full_name')
        email  = contact_form.cleaned_data.get('email')
        subject  = contact_form.cleaned_data.get('subject')
        text  = contact_form.cleaned_data.get('text')
        ContactUS.objects.create(full_name=full_name,email=email,subject=subject,text=text,is_read=False )
        contact_form = CreateContactForm()

    setting = SiteSetting.objects.first()
    context = {
        'contact_form':contact_form,
        'setting': setting
    }
    return render(request,'contact_us/contact_us_page.html',context)
