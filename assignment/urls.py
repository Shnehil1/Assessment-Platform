from django.conf.urls import url
from .import views
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.static import static




urlpatterns= [
    # /assignment/
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'assignment/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'assignment/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^past-assessments/$', views.past_assessments, name='past_assessments'),
    url(r'^save/$', views.save, name='save'),
    url(r'^upload/$', views.model_form_upload, name='model_form_upload'),
    url(r'^email/$', views.email, name='email'),
    url(r'^exportcsv/$', views.exportcsv, name='exportcsv'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)