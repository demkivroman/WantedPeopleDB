"""wantedDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from peoplesWDB.views.basepage import HomePageView, HelpPage, AboutUsPage 
from peoplesWDB.views.formsviews import AddPersonForm, ContactForm

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name = 'home'),
    url(r'^add/$', AddPersonForm.as_view(), name = 'add_person'),
    url(r'^contact/$', ContactForm.as_view(), name = 'contact'),
    url(r'^help/$', HelpPage.as_view(), name = 'help'),
    url(r'^about/us/$', AboutUsPage.as_view(), name = 'about_us'),
    url(r'^admin/', admin.site.urls),
]
