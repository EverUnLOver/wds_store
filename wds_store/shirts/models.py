"""Models shirts."""

# Django
from django.db import models

class Colore(models.Model):
    """."""
    color = models.CharField(max_length='15', unique=True, error_messages={'unique': 'Ya existe ese color'})
    class Meta:
        """."""
        ordering = ['color']
    def __str__(self):
        return '%s' % (self.color)

class Camisa(models.Model):
    """Camisas basicas."""
    CHOICE = (
        ('HOMBRE','Hombre'),
        ('NIÑO','Niño'),
        ('MUJER','Mujer'),
        ('NIÑA','Niña')
    )
    id = models.AutoField(primary_key=True, unique=True, error_messages={'unique': 'Ya esta esa id.'})
    tipo = models.CharField(max_length='7', choices=CHOICE)
    

    class Meta:
        """Meta class."""
        ordering = ['color']

    def __str__(self):

        return '%s' % (self.id)

class Imagene(models.Model):
    """."""
    camisa = models.ForeignKey(Camisa, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='/camisas/')
    color = models.ForeignKey(Colore, on_delete=models.CASCADE)

    class Meta:
        """."""
        ordering = ['camisa', 'color']


