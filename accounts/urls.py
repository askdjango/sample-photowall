from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={
        'template_name': 'accounts/login_form.html',
    }),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
]

