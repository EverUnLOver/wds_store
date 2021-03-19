"""Models shirts."""

# Django
from django.db import models

class Celebration(models.Model):
    """."""
    nombre = models.CharField(max_length=100)

    class Meta:
        """."""
        verbose_name = 'celebracion'
        verbose_name_plural = 'celebraciones'
        ordering = ['nombre']

    def __str__(self):
        """."""
        return '%s' % (self.nombre)

# ----------------------------------------------------- end ------------------------------------------

class Color(models.Model):
    """."""
    nombre = models.CharField(
        max_length=15,
        unique=True,
        error_messages={
            'unique': 'Este color ya esta registrado.'
        }
    )
    class Meta:
        """."""
        verbose_name = 'color'
        verbose_name_plural = 'colores'
        ordering = ['nombre']

    def __str__(self):
        return '%s' % (self.nombre)
    
    def clean(self):
        nombre = self.nombre.capitalize()
        self.nombre = nombre
        return super().clean()

# ------------------------------------------------------- end -----------------------------------------

class Producto(models.Model):
    """Modelo para guardar los tipos de productos."""
    nombre = models.CharField(
        max_length=20, 
        unique=True, 
        error_messages={
            'unique': 'Ya esta registrado este tipo de producto.'
        }
    )
    class Meta:
        """Meta class."""
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['nombre']

    def __str__(self):
        return '%s' % (self.nombre)

    def clean(self):
        nombre = self.nombre.capitalize()
        self.nombre = nombre
        return super().clean()

# --------------------------------------------------- end ---------------------------------------------

class Talla(models.Model):
    """Modelo para guardar las tallas."""
    talla = models.CharField(
        max_length=15,
        unique=True,
        error_messages={
            'unique': 'Esta talla ya esta registrada.'
        }
    )
    orden = models.PositiveIntegerField(default=0)
    producto = models.ManyToManyField(Producto)
    class Meta:
        """."""
        verbose_name = 'talla'
        verbose_name_plural = 'tallas'
        ordering = ['orden']

    def __str__(self):
        return '%s' % (self.talla)
    
    def clean(self):
        talla = self.talla.upper()
        self.talla = talla
        return super().clean()

# ------------------------------------------------------ end ------------------------------------------

class Item(models.Model):
    """Camisas basicas."""
    TIPO = (
        ('HOMBRE','Hombre'),
        ('MUJER','Mujer'),
        ('NIÑA','Niña'),
        ('NIÑO','Niño')
    )

    id = models.AutoField(auto_created=True, primary_key=True, unique=True, error_messages={'unique': 'Ya esta esa id.'})
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    publico = models.CharField(max_length=7, choices=TIPO, null=True, blank=True)
    talla = models.ManyToManyField(Talla, related_name='Tallas', blank=False, null=False)
    celebracion = models.ForeignKey(Celebration, on_delete=models.SET_NULL, null=True, blank=True)
    colores = models.ManyToManyField(Color, related_name='Colores', editable=False)

    class Meta:
        """Meta class."""
        ordering = ['producto', 'publico', 'celebracion', '-id']

    def __str__(self):
        """."""
        return '%s' % (self.id)