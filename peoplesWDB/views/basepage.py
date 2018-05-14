from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "base.html"

class HelpPage(TemplateView):
    template_name = "help.html"

class AboutUsPage(TemplateView):
    template_name = "about_us.html"
