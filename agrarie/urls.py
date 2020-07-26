from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns as doc_urls
<<<<<<< HEAD
urlpatterns = [
                  path('jet/', include('jet.urls', 'jet')),
                  path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                  path('admin/', admin.site.urls),
                  # path('api-auth/', include('rest_framework.urls')),
                  path('api/', include('users.urls')),
                  path('api/', include('forums.urls')),
                  path('api/', include('article.urls')),
                  path('api/auth/', include('djoser.urls')),
                  path('api/', include('informations.urls')),
                  path('auth/', include('rest_framework_social_oauth2.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include('users.urls')),
    path('api/', include('forums.urls')),
    path('api/', include('article.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/', include('informations.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> origin/second

urlpatterns += doc_urls
