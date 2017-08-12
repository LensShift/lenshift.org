from django.conf.urls import url

from apps.frontend.views import DisplayInfographic

urlpatterns = [
    url(
        r'^$',
        DisplayInfographic.as_view(),
        name='display_infographic'
    ),
]
