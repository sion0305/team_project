from django.contrib import admin
from django.urls import path, include
import blogapp.urls
import blogapp.views
import account.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.welcome, name='welcome'),
    path('blog/', include('blogapp.urls')),
    path('account/', include('account.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)