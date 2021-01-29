"""."""

# Dango
from django.db import models
from django.utils.safestring import mark_safe

# Models
from wds_store.shirts.models import Camisa

class Colore(models.Model):
    """."""
    color = models.CharField(max_length=15, unique=True, error_messages={'unique': 'Ya existe ese color'})
    class Meta:
        """."""
        ordering = ['color']
    def __str__(self):
        return '%s' % (self.color)

class Imagene(models.Model):
    """."""

    # Identificador imagen
    camisa = models.ForeignKey(Camisa, on_delete=models.CASCADE)

    # Informacion principal de imagen
    imagen = models.ImageField(upload_to='camisas')
    color = models.ForeignKey(Colore, on_delete=models.CASCADE)
    orden = models.PositiveIntegerField(blank=True, editable=True)
    imagen_principal = models.BooleanField(default=False)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        """."""
        ordering = ['camisa', 'color', 'orden']