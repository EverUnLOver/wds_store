"""Models shirts."""

# Django
from django.db import models
from django.db.models.expressions import F

# Utils
from multiselectfield import MultiSelectField # type:ignore

# Modelo secundario
class Celebration(models.Model):
    """."""
    celebracion = models.CharField(max_length=100)

    class Meta:
        """."""
        ordering = ['celebracion']

    def __str__(self):
        """."""
        return '%s' % (self.celebracion)

# Modelo secundario
class Color(models.Model):
    """."""
    color = models.CharField(max_length=15)
    class Meta:
        """."""
        ordering = ['color']
    def __str__(self):
        return '%s' % (self.color)

# Modelo secundario
class Talla(models.Model):
    """."""
    talla = models.CharField(max_length=15)
    orden = models.PositiveIntegerField(default=0)
    class Meta:
        """."""
        ordering = ['orden']
    def __str__(self):
        return '%s' % (self.talla)

# Modelo principal
class Camisa(models.Model):
    """Camisas basicas."""
    TIPO = (
        ('HOMBRE','Hombre'),
        ('MUJER','Mujer'),
        ('NIÑA','Niña'),
        ('NIÑO','Niño')
    )

    id = models.AutoField(auto_created=True, primary_key=True, unique=True, error_messages={'unique': 'Ya esta esa id.'})
    tipo = models.CharField(max_length=7, choices=TIPO, null=True, blank=True)
    talla = models.ManyToManyField(Talla, related_name='Tallas', blank=False, null=False)
    celebracion = models.ForeignKey(Celebration, on_delete=models.SET_NULL, null=True, blank=True)
    colores = models.ManyToManyField(Color, related_name='Colores', editable=False)

    class Meta:
        """Meta class."""
        ordering = ['tipo', 'celebracion', '-id']

    def __str__(self):
        """."""
        return '%s' % (self.id)