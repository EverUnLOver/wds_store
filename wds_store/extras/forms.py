"""Validaciones basadas en formularios para el admin."""

# Django
from django import forms

# Utils
from collections import Counter

from django.core.exceptions import ObjectDoesNotExist
from django.forms.forms import Form

# Models
from .models import Color

# ------------------------------------------ end ---------------------------------------------------

# Form camisa
class CamisaForm(forms.ModelForm):
    def clean(self):
        try:
            self.cleaned_data['talla']
            self.cleaned_data['tipo']
        except (KeyError):
            raise forms.ValidationError('Asegurece de completar todos los campos requeridos antes de guardar.')
        if self.instance.id == None:
            self.instance.save()

# ------------------------------------------ end ----------------------------------------------------

class InlineImageneFormSet(forms.BaseInlineFormSet):
    def clean(self):
        """Limitaciones en el orden del inline."""
        if self.instance.id == None:
            return
        recolector_imagen_principal = []
        recolector_color_imagen = []
        # Validaciones
        try:
            for data in self.cleaned_data:
            
                # Imagen principal
                if data['DELETE'] != True:
                    recolector_imagen_principal.append(data['imagen_principal'])
                    recolector_color_imagen.append(data['color'])
                contador_imagen_principal = Counter(recolector_imagen_principal)
                contador_color_imagen = Counter(recolector_color_imagen)
                imagen_principal_error = False
                imagen_principal_error = [
                    True for afirmacion in list(contador_imagen_principal.items()) if afirmacion[0] == 'SI' and afirmacion[1] > 1
                ]
                if imagen_principal_error:
                    raise forms.ValidationError('No puedes tener dos o mas imagenes principales.')
                
                #...
                if data == self.cleaned_data[-1]:
                    if not 'SI' in recolector_imagen_principal:
                        raise forms.ValidationError('Necesitas seleccionar al menos una IMAGEN que no vayas a eliminar como PRINCIPAL.')
            if len(self.forms) == 0:
                raise KeyError
        except (KeyError, AttributeError):
            raise forms.ValidationError('Asegurece de completar todos los campos requeridos antes de guardar.')
        # Validacion repetir imagen ---
        for primero in range(len(self.forms)):
                v = primero + 1
                for segundo_enadelante in range(len(self.forms)):
                    try:
                        if self.forms[primero].cleaned_data['imagen'] == self.forms[v].cleaned_data['imagen']:
                            raise forms.ValidationError('No puedes poner dos o mas veces la misma imagen. Por favor elige una diferente donde se encontraba alguna de las repetidas.')
                    except (IndexError):
                        continue
                    v += 1
        # Orden y Color (contador_color_imagen)
        lista_color_y_cantidad_imagenes = contador_color_imagen.items() # type:ignore
        for color_y_cantidad in lista_color_y_cantidad_imagenes:
            orden = 0
            for form in range(len(self.forms)):
                if orden == color_y_cantidad[1]:
                    break
                if self.forms[form].cleaned_data['color'] == color_y_cantidad[0] and self.forms[form].cleaned_data['DELETE'] == False:
                    self.forms[form].cleaned_data['orden'] = orden
                    self.forms[form].instance.orden = orden
                    orden += 1
                    
        # Delete
        for form in range(len(self.forms)):
            if self.forms[form].cleaned_data['DELETE']:
                #print(self.forms[form].instance, ' : ', self.forms[form].instance.color, ' : ', self.forms[form].instance.orden, ' : ', self.forms[form].cleaned_data['DELETE']) 
                self.forms[form].instance.delete()
                self.instance.colores.remove(self.forms[form].instance.color)
        # Save
        for form in range(len(self.forms)):
            if not self.forms[form].cleaned_data['DELETE']:
                #print(self.forms[form].instance, ' : ', self.forms[form].instance.color, ' : ', self.forms[form].instance.orden, ' : ', self.forms[form].cleaned_data['DELETE']) 
                self.forms[form].instance.save()
                self.instance.colores.add(self.forms[form].instance.color)

# ----------------------------------------------- end --------------------------------------------

# Form color
class ColorForm(forms.ModelForm):

    def clean(self):
        capitalize = self.cleaned_data['color'].capitalize()
        self.cleaned_data['color'] = capitalize
        self.instance.color = capitalize
        try:
            if Color.objects.get(color=capitalize):
                raise forms.ValidationError('Este color ya ha sido registrado antes.')
        except (ObjectDoesNotExist):
            return super().clean()