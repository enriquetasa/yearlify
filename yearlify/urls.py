from django.contrib import admin
from django.urls import path, include

from yearlify import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('account', include(('accounts.urls', 'account'), namespace='account')),

    path('letters', include(('letters.urls', 'letters'), namespace='letters')),
]
