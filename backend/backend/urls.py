from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenViewBase,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import (
    TokenObtainSerializer,
)

import api.views as api_views
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.six import text_type


class CustomTokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = text_type(self.user.id)
        data['refresh'] = text_type(refresh)
        data['access'] = text_type(refresh.access_token)

        return data


class CustomTokenObtainPairView(TokenViewBase):
    serializer_class = CustomTokenObtainPairSerializer


token_obtain_pair = CustomTokenObtainPairView.as_view()


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    url(r'^$', generic.RedirectView.as_view(
         url='/api/', permanent=False)),
    url(r'^api/$', get_schema_view()),

    # Auth
    url(r'^api/auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/token/obtain/$', CustomTokenObtainPairView.as_view()),
    url(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),

    # Users
    url(r'^api/users/register/', api_views.users),
    url(r'^api/users/', api_views.users),

    # Cameras
    path(r'api/parents/<int:parentid>/cameras/', api_views.cameras),
    path(r'api/parents/<int:parentid>/cameras/<int:cameraid>', api_views.get_camera),

    # Children
    path(r'api/parents/<int:parentid>/children/', api_views.children),
    path(r'api/parents/<int:parentid>/children/<int:childid>', api_views.get_child),
    path(r'api/parents/<int:parentid>/children/<int:childid>/events', api_views.events),
    path(r'api/parents/<int:parentid>/children/<int:childid>/events/<int:eventid>', api_views.get_event),
]
