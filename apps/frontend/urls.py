from django.conf.urls import url

from apps.frontend.views import DisplayInfographic

urlpatterns = [
    url(
        r'^(?P<pk>\d+)$',
        DisplayInfographic.as_view(),
        name='display_infographic'
    ),
]
