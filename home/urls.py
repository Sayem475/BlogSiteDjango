from django.urls import path, include
from . import views
from django.views import View
from . views import Home, ContactView, AboutView, Search, HandleSignup, HandleLogin, HandleLogout, LearnView,HTMLPage,CascadPage,JavaPage, PyPage, DjPage

urlpatterns = [
    
    path('', Home.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/', Search.as_view(), name='search'),
    path('signup', HandleSignup.as_view(), name='handlesignup'),
    path('login', HandleLogin.as_view(), name='handlelogin'),
    path('logout', HandleLogout.as_view(), name='handlelogout'),
    path('learn', LearnView.as_view(), name='learn'),
    path('hyppage', HTMLPage.as_view(), name='hyppage'),
    path('cascadpage', CascadPage.as_view(), name='cascadpage'),
    path('javaspage', JavaPage.as_view(), name='javaspage'),
    path('pypage', PyPage.as_view(), name='pypage'),
    path('djpage', DjPage.as_view(), name='djpage'),
    path('homeapi/', include('home.restapi.urls')),
]
