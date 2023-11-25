from django.contrib import admin

from france_contact.models import ContactUS
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'full_name', 'subject','is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']




admin.site.register(ContactUS,ContactUsAdmin)
