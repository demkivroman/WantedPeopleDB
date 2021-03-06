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
from peoplesWDB.views.siteviews import CommentSave, UserProfile
from peoplesWDB.views import formsviews, siteviews
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name = 'home'),
    url(r'^add/$', formsviews.add_wanted_person, name = 'add_person'),
    url(r'^contact/$', formsviews.contact_form, name = 'contact'),
    url(r'^send/mail/$', formsviews.sendMail, name = 'send_mail'),
    url(r'^help/$', HelpPage.as_view(), name = 'help'),
    url(r'^about/us/$', AboutUsPage.as_view(), name = 'about_us'),
    url(r'^search/$', formsviews.db_search, name = 'search'),
    url(r'^comment/(?P<pk>\d+)$', CommentSave.as_view(), name = 'comment'),
    url(r'^ajax/comment/save/$',CommentSave.as_view(), name = 'comment_save'),
    url(r'^signup/$',siteviews.signup_addphoto, name = 'sign_up'),
    url(r'^user/profile/(?P<pk>\d+)$',UserProfile.as_view(), name = 'user_profile'),
    url(r'^delete/persons/',formsviews.deletePersons, name = 'delete_persons'),
    url(r'^person/edit/',formsviews.editPerson, name = 'edit_persons'),
    url(r'^delete/comments/',formsviews.deleteComments, name = 'delete_comments'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    # urls for authentications
    url(r'^accounts/', include('allauth.urls'), name = 'login'),

    # urls for encrypt
    # url(r'^\.well-known/', include('letsencrypt.urls'), name = 'detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]"""
