from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from app import views

urlpatterns = [
    url(r'^games/', views.Game, name='Game'),
    url(r'^horse', views.Hourse, name='Hourse'),
    url(r'^jockey/', views.Jockeys, name='add'),
    url(r'^owners/', views.Owners, name='Owner'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()