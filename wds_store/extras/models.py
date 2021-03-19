"""."""

# Dango
from django.db import models
from django.utils.safestring import mark_safe

# Models
from wds_store.shirts.models import Item, Color, Talla


# Modelo no visible
class Imagenes(models.Model):
    """."""
    CHOICES = (
        ('NO','No'),
        ('SI','Si'),
    )

    # Identificador imagen
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    # Informacion principal de imagen
    imagen = models.ImageField(upload_to='camisas')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    orden = models.PositiveIntegerField(blank=True, editable=True)
    imagen_principal = models.CharField(max_length=2, choices=CHOICES, default=CHOICES[0][0])
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        """."""
        ordering = ['item', 'color', 'orden']
        verbose_name = "Imagenes"
        verbose_name_plural = "Imagenes"