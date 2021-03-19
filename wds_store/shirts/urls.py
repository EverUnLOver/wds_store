"""."""

# Django
from django.urls import path 
from django.urls.exceptions import NoReverseMatch

# Views
from wds_store.shirts import views


urlpatterns = [
    # Personal_admin
    path(
        route = 'personal_admin/menu/',
        view = views.Menu.as_view(),
        name = "menu"
    ),
    path(
        route = "personal_admin/menu/crear/<str:modelo>/<str:slugname>/",
        view = views.CreateView.as_view(),
        name = "create"
    ),
    path(
        route = "personal_admin/menu/itemlist/<str:modelo>/<str:objeto>/",
        view = views.ItemList.as_view(),
        name = "itemlist"
    ),
    path(
        route = "personal_admin/menu/delete/<str:modelo>/<str:objeto>/",
        view = views.DeleteView.as_view(),
        name = "delete"
    ),
    path(
        route = "personal_admin/menu/update/<str:modelo>/<str:objeto>/<str:slugname>/",
        view = views.UpdateView.as_view(),
        name = "update"
    )
]