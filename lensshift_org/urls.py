from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from apps.api.views import InfographicViewSet

router = DefaultRouter()
router.register(r'infographics', InfographicViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^', include('apps.frontend.urls')),
]
