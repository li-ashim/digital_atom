from django.urls import path, include

from .views import login_page

app_name = 'rosatom_users'
urlpatterns = [
    path('login/', login_page, name='login'),
    path('', include('django.contrib.auth.urls')),
]
