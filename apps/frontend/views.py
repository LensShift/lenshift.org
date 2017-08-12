from django.views.generic import TemplateView


class DisplayInfographic(TemplateView):
    template_name = 'templates/frontend/display.html'