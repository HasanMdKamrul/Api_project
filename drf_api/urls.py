
from django.contrib import admin
from django.urls import path,include
from core.views import PostApiView,PostCreateView,PostListCreateApiView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('',PostApiView.as_view(), name="login"),
    path('create/',PostCreateView.as_view(), name="create"),
    path('create-api/',PostListCreateApiView.as_view(), name="create-api"),
    path('api/token/',obtain_auth_token, name='obtain-token')
]
