from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('main_page.urls')),
    path('', include('sprofile.urls')),
    path('', include('publication.urls')),
]
