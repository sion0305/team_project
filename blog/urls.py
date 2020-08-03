from django.contrib import admin
from django.urls import path, include
import blogapp.urls
import blogapp.views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.welcome, name='welcome'),
    path('blog/', include('blogapp.urls')),
    path('account/', include('account.urls')),
]