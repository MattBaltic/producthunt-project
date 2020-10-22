from django.contrib import admin
from django.urls import path, include #include added
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')), #everything /accounts is moving to accounts. include added
]
