"""."""

# Django
from django.contrib import admin
from django.utils.safestring import mark_safe

# Forms
from wds_store.extras.forms import (
    InlineImageneFormSet,
    ColorForm,
    CamisaForm
)

# Models
from .models import Camisa, Celebration, Color, Talla
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
    extra = 0

# Admin principal
class CamisaAdmin(admin.ModelAdmin):
    """."""
    
    inlines = (ImageneInline,)
    list_display = ("tipo", "ver_imagen_principal", "todos_los_colores", "fecha_de_modificacion")
    list_filter = ("tipo", 'celebracion', 'colores', 'talla')
    form = CamisaForm
    #filter_horizontal = ('talla',)
    fieldsets = (
        ('DETALLES CAMISA', {
            'fields': (('tipo','talla','celebracion'),),
            'classes': ('inline'),
        }),
    )

    def ver_imagen_principal(self, obj):
        """."""
        imagen_principal = Imagene.objects.get(camisa__id=obj.id, imagen_principal='SI')
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
        imagen_principal = Imagene.objects.get(camisa__id=obj.id, imagen_principal='SI')
        return imagen_principal.fecha_modificacion
    fecha_de_modificacion.short_description = "modificacion"
    fecha_de_modificacion.allow_tags = True

admin.site.register(Camisa, CamisaAdmin)

# Admin secundario

class ColorAdmin(admin.ModelAdmin):
    
    form = ColorForm
    list_display = ('color',)

admin.site.register(Color, ColorAdmin)
admin.site.register(Talla)
admin.site.register(Celebration)