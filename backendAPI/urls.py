from django.contrib import admin
from django.urls import path, include
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customerApp.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    path('openid/', include('oidc_provider.urls', namespace='oidc_provider')),
]
