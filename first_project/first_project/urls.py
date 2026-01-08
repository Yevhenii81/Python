from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('hw_18_12.urls')),

    path('hw20/', include('hw_20_12.urls')),
    path('old/', include('hw_13_12.urls')),
    path('city/', include('hw_11_12.urls')),
    path('hw16/', include('hw_16_12.urls')),
]
