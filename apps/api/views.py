from rest_framework.viewsets import ModelViewSet

from apps.api.models import Infographic
from apps.api.serializers import InfographicSerializer


class InfographicViewSet(ModelViewSet):
    queryset = Infographic.objects.all()
    serializer_class = InfographicSerializer
