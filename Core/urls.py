from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from graphql_jwt.decorators import jwt_cookie
from django.views.decorators.csrf import csrf_exempt
import debug_toolbar

from graphene_django.views import GraphQLView
from Api.views import friends, friends_redis


urlpatterns = [
   path('friends/', friends),
    path('redis/', friends_redis),
    path('admin/', admin.site.urls),
    path("graphql/", csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True)))),
    path("", csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True)))),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
