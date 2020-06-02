from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ratingapp.views import index, post, search
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ratingapp.urls')),
    # path('post/<id>/', post, name='post-detail'),
    # path('search/', search, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)