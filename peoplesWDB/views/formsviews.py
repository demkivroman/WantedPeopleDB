from django.views.generic.base import TemplateView

class AddPersonForm(TemplateView):
    template_name = "forms/add_form.html"


class ContactForm(TemplateView):
    template_name = "forms/contact_form.html"
