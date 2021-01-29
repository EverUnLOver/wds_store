from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExtrasConfig(AppConfig):
    name = "wds_store.extras"
    verbose_name = _("extras")