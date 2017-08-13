from django.conf import settings
from django.views.generic import DetailView

from apps.api.models import Infographic


class DisplayInfographic(DetailView):
    template_name = 'frontend/display.html'
    model = Infographic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['BACKEND_URL'] = settings.BACKEND_URL

        return context
