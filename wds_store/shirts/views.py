"""Views Shirts."""

#Django
from django.views.generic import TemplateView





# Shirts view
class ShirtsIndexView(TemplateView):
    template_name = 'base.html'