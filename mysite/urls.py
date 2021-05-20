from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blogging.urls')),
    path('polling/', include('polling.urls')),
    path('admin/', admin.site.urls),
]
