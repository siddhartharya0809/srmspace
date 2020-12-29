from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *


urlpatterns = [
    path('', srm_space, name="SRM space"),
    path('go', go, name="Filters page"),
    path('contact', contact_us, name="Contact us"),
    path('navbar', navbar, name="Navigation Bar"),
    path('upload_notes', upload_notes, name="Upload notes"),
    path('view_notes', view_notes, name="View notes"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
