"""."""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShirtsConfig(AppConfig):
    """."""
    name = "wds_store.shirts"
    verbose_name = _("shirts")