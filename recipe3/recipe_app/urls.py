from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from .views import MyappView,MyappView2
from django.conf import settings

urlpatterns = [
              path(r'', MyappView.as_view(), name='index'),
              path('delete/', MyappView2.as_view(), name='index3'),
              ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
