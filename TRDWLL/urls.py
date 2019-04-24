from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('about/', AboutView.as_view(), name='about_page'),

    path('blog/', include('blog.urls'), name='blog_home_page'),
    path('experiments/', include('experiments.urls'), name='experiments_home_page'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'TRDWLL AdminCP'
admin.site.site_title = 'TRDWLL AdminCP'

# admin.site.__class__ = OTPAdminSite