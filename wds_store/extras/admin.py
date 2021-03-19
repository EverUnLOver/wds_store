"""."""

# Django
from django.contrib import admin

# Models
from .models import (
    Imagenes
)
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress # type: ignore
from allauth.socialaccount.models import ( # type: ignore
    SocialApp,
    SocialAccount,
    SocialToken
)
from django_celery_beat.models import (    # type: ignore
    PeriodicTask, 
    CrontabSchedule, 
    IntervalSchedule, 
    ClockedSchedule, 
    SolarSchedule
)

# Register
admin.site.register(Imagenes)

# Unregister
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(User)
admin.site.unregister(PeriodicTask)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(SolarSchedule)
admin.site.unregister(EmailAddress)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)