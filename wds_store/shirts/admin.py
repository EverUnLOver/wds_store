"""."""

# Django
from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe

# Forms
from wds_store.extras.forms import (
    InlineImageneFormSet,
    ColorForm
)

# Models
from .models import Camisa, Colore
from wds_store.extras.models import Imagene

# Pagina admin
admin.site.site_title = "Camisas"
admin.site.index_title = "Administrador"

# Admin alineado con el principal
class ImageneInline(admin.TabularInline):
    """Clase Admin para administrar el modelo Camisa junto a Imagene."""
    model = Imagene
    can_delete = True
    verbose_name_plural = 'imagenes de la camisa'
    formset = InlineImageneFormSet

    def get_extra(self, request, obj, **kwargs):
        extra = 0
        return extra
    
    def get_fields(self, request, obj):
        return super().get_fields(request, obj=obj)

# Admin principal
class CamisaAdmin(admin.ModelAdmin):
    """."""
    inlines = (ImageneInline,)
    list_display = ("tipo", "ver_imagen_principal", "todos_los_colores", "fecha_de_modificacion")

    def ver_imagen_principal(self, obj):
        """."""
        imagen_principal = Imagene.objects.get(camisa__id=obj.id, imagen_principal=True)
        return mark_safe('<img src="{}" width="100" />'.format(imagen_principal.imagen.url))
    ver_imagen_principal.short_description = "ver imagen principal"
    ver_imagen_principal.allow_tags = True

    def todos_los_colores(self, obj):
        """."""
        imagenes = Imagene.objects.filter(camisa__id=obj.id, orden=0)
        colores = ''
        for imagen in imagenes:
            if imagen == imagenes[len(imagenes)-1]:
                colores += str(imagen.color)+'.'
                break
            colores += str(imagen.color)+', '
        return colores
    todos_los_colores.short_description = "colores disponibles"
    todos_los_colores.allow_tags = True
    
    def fecha_de_modificacion(self, obj):
        imagen_principal = Imagene.objects.get(camisa__id=obj.id, imagen_principal=True)
        return imagen_principal.fecha_modificacion
    fecha_de_modificacion.short_description = "modificacion"
    fecha_de_modificacion.allow_tags = True

admin.site.register(Camisa, CamisaAdmin)

# Admin secundario

class ColorAdmin(admin.ModelAdmin):
    
    form = ColorForm
    list_display = ('color',)

admin.site.register(Colore, ColorAdmin)