from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/home/', include('apps.home.urls')), 
    path('api/accommodation/', include('apps.accommodation.urls')), 
    path('api/gallery/', include('apps.gallery.urls')), 
    path('api/notice/', include('apps.notice.urls')), 
    path('api/about/', include('apps.about.urls')), 
    path('api/contact/', include('apps.contact.urls')), 
    path('api/events/', include('apps.events.urls')), 
    path('api/footer/', include('apps.footer.urls')), 
    path('api/facilities/', include('apps.facilities.urls')), 
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
