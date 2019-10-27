from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ClubVR/', include('ClubVR.urls')),
    path('admin/', admin.site.urls),
]