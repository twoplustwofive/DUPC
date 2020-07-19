from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainsite.urls',namespace='mainsite')),
    path('account/',include('account.urls',namespace='account')),
    
    path('publication/',include('publication.urls',namespace='publication')),
    path('news_and_updates/',include('news.urls',namespace = 'news')),
    path('outreach/',include('outreach.urls',namespace = 'outreach')),
    path('reports/',include('reports.urls',namespace='reports')),
    path('stories/',include('stories.urls',namespace='stories')),
]+  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

