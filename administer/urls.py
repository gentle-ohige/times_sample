from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('user/', record_user_profile),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('updateIcon/', ImageUploadView.as_view(), name='useIcon')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)