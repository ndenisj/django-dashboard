from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from finance.views import company_article_list, ChartData

from .views import home

urlpatterns = [
    path('home/', home, 'home'),
    path('admin/', admin.site.urls),
    path('notes/', include('notepad.urls')),
    path('companies/', company_article_list, name="companies"),
    path('api/chart/data/', ChartData.as_view(), name="api-chart-data"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)