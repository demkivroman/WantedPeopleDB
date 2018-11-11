from django.views.generic.base import TemplateView
from ..util.util_func import read_file
from wantedDB.settings import STATIC_ROOT

class HomePageView(TemplateView):
    template_name = "base.html"

class HelpPage(TemplateView):
    template_name = "help.html"

class AboutUsPage(TemplateView):
    template_name = "about_us.html"

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(AboutUsPage, self).get_context_data(**kwargs)
        # url = '/home/wantedDB/WantedPeopleDB/peoplesWDB/static/content/aboutUs.txt'
        url = STATIC_ROOT + "/content/aboutUs.txt"
        context = read_file(url)
        return context
