"""."""

# Django
from django.contrib import admin
from django.utils.safestring import mark_safe

# Forms
from wds_store.extras.forms import (
    InlineImageneFormSet,
    ColorForm,
    CamisaForm,
    TallaForm
)

# Models
from .models import Item, Celebration, Color, Talla, Producto
from wds_store.extras.models import Imagenes

# Pagina admin
admin.site.site_title = "Camisas"
admin.site.index_title = "Administrador"

# Admin alineado con el principal
class ImageneInline(admin.TabularInline):
    """Clase Admin para administrar el modelo Camisa junto a Imagene."""
    model = Imagenes
    can_delete = True
    verbose_name_plural = 'imagenes de la camisa'
    formset = InlineImageneFormSet
    extra = 0

# Admin principal
class CamisaAdmin(admin.ModelAdmin):
    """."""
    
    inlines = (ImageneInline,)
    #list_display = ("tipo", 'Celebracion', "ver_imagen_principal", 'Talla', "todos_los_colores", "fecha_de_modificacion")
    #list_filter = ("tipo", 'celebracion', 'colores', 'talla')
    form = CamisaForm
    #fieldsets = (
     #   ('DETALLES CAMISA', {
      #      'fields': (('tipo','talla','celebracion'),),
       #     'classes': ('inline'),
    #    }),
    #)

    def Celebracion(self, obj):
        """."""
        return '%s' % (obj.celebracion.celebracion)
    Celebracion.short_description = 'celebracion'

    def Talla(self, obj):
        """."""
        return ', '.join([talla.talla for talla in obj.talla.all().order_by("orden")])
    Talla.short_description = 'talla(s)'

    def todos_los_colores(self, obj):
        """."""
        imagenes = Imagenes.objects.filter(camisa__id=obj.id, orden=0).order_by('color')
        return ', '.join([imagen.color.color for imagen in imagenes])
    todos_los_colores.short_description = "color(es) disponible(s)"

    def ver_imagen_principal(self, obj):
        """."""
        imagen_principal = Imagenes.objects.get(camisa__id=obj.id, imagen_principal='SI')
        return mark_safe('<img src="{}" width="100" />'.format(imagen_principal.imagen.url))
    ver_imagen_principal.short_description = "imagen principal"
    ver_imagen_principal.allow_tags = True
    
    def fecha_de_modificacion(self, obj):
        imagen_principal = Imagenes.objects.get(camisa__id=obj.id, imagen_principal='SI')
        return imagen_principal.fecha_modificacion
    fecha_de_modificacion.short_description = "ultima modificacion"

admin.site.register(Item, CamisaAdmin)

# Admin secundario
class ColorAdmin(admin.ModelAdmin):
    
    form = ColorForm
    list_display = ('nombre',)

admin.site.register(Color, ColorAdmin)

# Admin secundario
class TallaAdmin(admin.ModelAdmin):
    
    form = TallaForm
    list_display = ('talla', 'orden',)

admin.site.register(Talla, TallaAdmin)
admin.site.register(Celebration)
admin.site.register(Producto)