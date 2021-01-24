"""Models shirts."""

# Django
from django.db import models

class Basica(models.Model):
    """Camisas basicas."""

    imagen = models.ImageField(upload_to='/basicas/')
    color = models.CharField(max_length='15', unique=True, error_messages={'unique': 'Ya esta una camisa basica con ese color.'})

    class Meta:
        """Meta class."""
        ordering = ['color']

    def __str__(self):

        return '%s' % (self.color)

class Diseño(models.Model):
    """Diseño de camisas basicas."""

    nombre = models.CharField(max_length='100', unique=True, error_messages={'unique': 'Ya hay un diseño con este nonbre.'})
    imagen = models.ImageField(upload_to='/diseños/')

    class Meta:
        """Meta class."""
        ordering = ['nombre']

    def __str__(self):

        return '%s' % (self.nombre)

class Basica_Diseño(models.Model):
    """Basicas con diseño."""

    id = models.AutoField(primary_key=True, unique=True, error_messages={'unique': 'Ya existe esta id.'})
    basica = models.ImageField(upload_to='/BasicaConDiseño/')

    class Meta:
        """Meta class."""
        ordering = ['id']
