from django.conf.urls import include, url
from django.contrib import admin
from Shnehil import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^assignment/', include('assignment.urls')),
]
