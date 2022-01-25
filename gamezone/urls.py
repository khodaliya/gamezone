from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('jignisha/', admin.site.urls),
    path('', include('app.urls'))
]

handler404 = 'app.views.error_404_view'
