from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


STATUS = (
    ('d', _('Draft'),),
    ('r', _('Ready'),),
)


class Infographic(TimeStampedModel):
    name = models.CharField(max_length=200)
    url = models.URLField()
    status = models.CharField(max_length=1, choices=STATUS)


class Section(TimeStampedModel):
    class Meta:
        ordering = ('section_position', 'id',)

    background_video = models.FileField(
        upload_to='videos',
        null=True,
        blank=True
    )
    background_image = models.FileField(
        upload_to='images',
        null=True,
        blank=True
    )
    text = models.TextField()
    text_position_x = models.IntegerField(default=0)
    text_position_y = models.IntegerField(default=0)
    section_position = models.PositiveSmallIntegerField()

    infographic = models.ForeignKey(Infographic)
