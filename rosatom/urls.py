from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('rosatom_users.urls')),
    path('', include('rosatom_app.urls')),
]