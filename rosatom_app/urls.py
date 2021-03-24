from django.urls import path

from . import views

app_name = 'rosatom_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('edit_task', views.edit_task, name='edit_task'),
    path('add_task', views.add_task, name='add_task'),
    path('useful_materials', views.useful, name='useful'),
    path('add_useful', views.add_useful, name='add_useful'),
    path('collective', views.collective, name='collective'),
]