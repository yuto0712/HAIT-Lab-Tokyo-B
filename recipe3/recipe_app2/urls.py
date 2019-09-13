from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from .views import MyappView2
from django.conf import settings


urlpatterns = [
              url('', MyappView2.as_view(), name='index2'),
              ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
