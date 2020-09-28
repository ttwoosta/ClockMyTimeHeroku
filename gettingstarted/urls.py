from django.urls import path, include
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
admin.autodiscover()
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from hello.views import main as main_views
from hello.views import ml

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
    path("", main_views.index, name="index"),
    path("admin/", admin.site.urls),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    url("api", include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path("get-csrf-token/", main_views.get_csrf_token),
    path("schedules/", main_views.schedule_list),
    path("schedules/<int:pk>/", main_views.schedule_detail),

    path("login/", main_views.auth_login),
    path("logout/", main_views.auth_logout),

    path('accounts/profile/', main_views.get_profile),
    
    path('accounts/login_view/', auth_views.LoginView.as_view(template_name='../hello/templates/login.html')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('auth/login/', auth_views.LoginView.as_view()),
    
    path("my-pay/", main_views.my_pay_list),

    path("predict_score", ml.predict_score),
    path("breast_cancer_fig", ml.breat_cancer_fig),
]
