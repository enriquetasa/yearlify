from django.urls import path

from letters import views

app_name = 'letters'

urlpatterns = [
    path(r'_explain/', views.explain, name='explain'),
    path(r'_compose/', views.compose, name='compose'),
    path(r'_success/', views.success, name='success'),
    path(r'_list', views.list_letters, name='list')
]
