# from django.conf.urls import url, include
from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  re_path(r'^admin/', admin.site.urls),
  re_path(r'^file/', include('mpesa_statements.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)