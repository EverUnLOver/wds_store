"""Url T-Shirts"""

#Django
from django.urls import path
from wds_store.shirts import views as shirts_views

app_name = "shirts"
urlpatterns = [
    path(
        route='',
        view=shirts_views.ShirtsIndexView.as_view(),
        name='index'
    ), 
]