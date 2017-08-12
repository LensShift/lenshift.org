from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.api.models import Infographic, Section


class InfographicSerializer(ModelSerializer):
    sections = SerializerMethodField()

    class Meta:
        model = Infographic
        fields = (
            'sections',
            'name',
            'url',
            'status',
        )

    def get_sections(self, obj):
        return SectionSerializer(obj.section_set.all(), many=True).data


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
