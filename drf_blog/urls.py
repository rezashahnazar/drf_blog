from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin


urlpatterns = [
    path('blog/', include('blog.urls')),
    path('auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
