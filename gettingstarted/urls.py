from django.urls import path, include
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
admin.autodiscover()
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
import hello.views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("admin/", admin.site.urls),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    url("api", include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path("get-csrf-token/", hello.views.get_csrf_token),
    path("schedules/", hello.views.schedule_list),
    path("schedules/<int:pk>/", hello.views.schedule_detail),

    path("login/", hello.views.auth_login),
    path("logout/", hello.views.auth_logout),

    path('accounts/profile/', hello.views.get_profile),
    
    path('accounts/', include('django.contrib.auth.urls')),

    path('auth/login/', auth_views.LoginView.as_view()),
    
]
