from django.contrib import admin
from django.urls import path, include, reverse
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='tem/home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('tem/', include('tem.urls')),
    #path('tem/', include('django.contrib.auth.urls')),
]
