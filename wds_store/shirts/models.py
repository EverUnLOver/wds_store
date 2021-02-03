"""Models shirts."""

# Django
from django.db import models

# Modelo principal
class Camisa(models.Model):
    """Camisas basicas."""
    CHOICE = (
        ('HOMBRE','Hombre'),
        ('MUJER','Mujer'),
        ('NIÑA','Niña'),
        ('NIÑO','Niño')
    )
    id = models.AutoField(auto_created=True, primary_key=True, unique=True, error_messages={'unique': 'Ya esta esa id.'})
    tipo = models.CharField(max_length=7, choices=CHOICE)

    class Meta:
        """Meta class."""
        ordering = ['tipo', '-id']

    def __str__(self):
        """."""
        return '%s' % (self.id)

# Modelo secundario
class Colore(models.Model):
    """."""
    color = models.CharField(max_length=15)
    class Meta:
        """."""
        ordering = ['color']
    def __str__(self):
        return '%s' % (self.color)

