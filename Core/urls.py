from django.contrib import admin
from django.urls import path, include
import debug_toolbar

from Web.views import friends


urlpatterns = [
    path('', friends),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]
