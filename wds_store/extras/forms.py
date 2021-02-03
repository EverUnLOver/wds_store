"""Validaciones basadas en formularios para el admin."""

# Django
from django import forms

# Utils
from collections import Counter

from django.core.exceptions import ObjectDoesNotExist, ValidationError

# Models
from .models import Colore

class InlineImageneFormSet(forms.BaseInlineFormSet):
    def clean(self):
        """Limitaciones en el orden del inline."""
        numero_bucle = 0
        numero_orden = 0
        recolector_imagen_principal = []
        # Validaciones
        try:
            for data in self.cleaned_data:
            
                # Imagen principal
                recolector_imagen_principal.append(data['imagen_principal'])
                contador_imagen_principal = Counter(recolector_imagen_principal)
                imagen_principal_error = False
                imagen_principal_error = [
                    True for afirmacion in list(contador_imagen_principal.items()) if afirmacion[0] == True and afirmacion[1] > 1
                ]
                if imagen_principal_error:
                    raise forms.ValidationError('No puedes tener dos imagenes principales.')
                
                #...
                if data == self.cleaned_data[-1]:
                    if not True in recolector_imagen_principal:
                        raise forms.ValidationError('Necesitas seleccionar al menos una imagen como principal.')
            if len(self.forms) == 0:
                raise KeyError
        except (KeyError, AttributeError):
            raise forms.ValidationError('Asegurece de completar todos los datos requeridos.')

        for primero in range(len(self.forms)):
                v = primero + 1
                for segundo_enadelante in range(len(self.forms)):
                    try:
                        if self.forms[primero].cleaned_data['imagen'] == self.forms[v].cleaned_data['imagen']:
                            raise forms.ValidationError('No puedes poner dos o mas veces la misma imagen. Por favor elige una diferente donde se encontraba alguna de las repetidas.')
                    except (IndexError):
                        continue
                    v += 1
        # Lista negra y quitar el Color
        lista_negra = []
        bucle = 0
        for form in range(len(self.forms)):
                if self.forms[form].cleaned_data['DELETE'] == True:
                    lista_negra.append(bucle)
                bucle += 1
        rango = len(self.forms) - len(lista_negra)
        # Ordenar los de la lista negra al final
        continuar = True
        while continuar:
            for posicion_actual in range(len(self.forms)):
                # Posicion actual y posterior
                if posicion_actual+1 < len(self.forms) and self.forms[posicion_actual].cleaned_data['DELETE'] == True:
                    almacenado_temporal = self.forms[posicion_actual+1].cleaned_data
                    self.forms[posicion_actual+1].cleaned_data = self.forms[posicion_actual].cleaned_data
                    self.forms[posicion_actual].cleaned_data = almacenado_temporal

                    almacenado_temporal = self.forms[posicion_actual+1].instance
                    self.forms[posicion_actual+1].instance = self.forms[posicion_actual].instance
                    self.forms[posicion_actual].instance = almacenado_temporal
            for form in range(rango):
                if self.forms[form].cleaned_data['DELETE']:
                    continuar = True
                    break
                continuar = False
        # Evaluar si hay uno o mas elementos para trabajar
        if rango >= 2:
            # Ordenar colorres
            for repetir in range(rango):
                for posicion_actual in range(rango):
                    posiciones_posteriores=posicion_actual+1
                    try:
                        if self.forms[posicion_actual].instance.color == self.forms[posiciones_posteriores].instance.color or self.forms[posiciones_posteriores].cleaned_data['DELETE'] == True:
                            continue
                    except (IndexError):
                        break

                    for posiciones_posteriores in range(rango):
                        # Posicion actual y anterior
                        try:
                            if repetir/2==0 and self.forms[posicion_actual].instance.color != self.forms[posicion_actual-1].instance.color and self.forms[posicion_actual].instance.color != self.forms[posiciones_posteriores].instance.color:
                                almacenado_temporal = self.forms[posicion_actual-1].cleaned_data
                                self.forms[posicion_actual-1].cleaned_data = self.forms[posicion_actual].cleaned_data
                                self.forms[posicion_actual].cleaned_data = almacenado_temporal

                                almacenado_temporal = self.forms[posicion_actual-1].instance
                                self.forms[posicion_actual-1].instance = self.forms[posicion_actual].instance
                                self.forms[posicion_actual].instance = almacenado_temporal
                        except (ObjectDoesNotExist):
                            pass
                        # Posicion actual y posterior
                        try:
                            if self.forms[posicion_actual].instance.color != self.forms[posiciones_posteriores].instance.color and self.forms[posicion_actual].instance.color != self.forms[posiciones_posteriores].instance.color:
                                almacenado_temporal = self.forms[posicion_actual].cleaned_data
                                self.forms[posicion_actual].cleaned_data = self.forms[posiciones_posteriores].cleaned_data
                                self.forms[posiciones_posteriores].cleaned_data = almacenado_temporal

                                almacenado_temporal = self.forms[posicion_actual].instance
                                self.forms[posicion_actual].instance = self.forms[posiciones_posteriores].instance
                                self.forms[posiciones_posteriores].instance = almacenado_temporal
                        except (ObjectDoesNotExist):
                            continue
            # Ordenar colorres 2
            for repetir in range(rango):
                for posicion_actual in range(rango):
                    posiciones_posteriores=posicion_actual+1
                    try:
                        if self.forms[posicion_actual].instance.color == self.forms[posiciones_posteriores].instance.color or self.forms[posiciones_posteriores].cleaned_data['DELETE'] == True:
                            continue
                    except (IndexError):
                        break

                    for posiciones_posteriores in range(rango):
                        # Posicion actual y anterior
                        try:
                            if self.forms[posicion_actual].instance.color != self.forms[posicion_actual-1].instance.color and self.forms[posicion_actual].instance.color != self.forms[posiciones_posteriores].instance.color:
                                almacenado_temporal = self.forms[posicion_actual-1].cleaned_data
                                self.forms[posicion_actual-1].cleaned_data = self.forms[posicion_actual].cleaned_data
                                self.forms[posicion_actual].cleaned_data = almacenado_temporal

                                almacenado_temporal = self.forms[posicion_actual-1].instance
                                self.forms[posicion_actual-1].instance = self.forms[posicion_actual].instance
                                self.forms[posicion_actual].instance = almacenado_temporal
                        except (ObjectDoesNotExist):
                            pass
                        # Posicion actual y posterior
                        try:
                            if repetir/2==0 and self.forms[posicion_actual].instance.color != self.forms[posiciones_posteriores].instance.color and self.forms[posicion_actual].instance.color != self.forms[posiciones_posteriores].instance.color:
                                almacenado_temporal = self.forms[posicion_actual].cleaned_data
                                self.forms[posicion_actual].cleaned_data = self.forms[posiciones_posteriores].cleaned_data
                                self.forms[posiciones_posteriores].cleaned_data = almacenado_temporal

                                almacenado_temporal = self.forms[posicion_actual].instance
                                self.forms[posicion_actual].instance = self.forms[posiciones_posteriores].instance
                                self.forms[posiciones_posteriores].instance = almacenado_temporal
                        except (ObjectDoesNotExist):
                            continue
            # Poner el numero del orden
            while True:
                self.forms[numero_bucle].cleaned_data['orden'] = numero_orden
                self.forms[numero_bucle].instance.orden = numero_orden
                numero_orden += 1
                try:
                    if self.forms[numero_bucle].cleaned_data['color'] != self.forms[numero_bucle+1].cleaned_data['color']:
                        numero_orden = 0
                except (IndexError):
                    break
                numero_bucle += 1
        else:
            for i in range(len(self.forms)):
                if self.forms[i].cleaned_data['DELETE'] == False:
                    self.forms[numero_bucle].cleaned_data['orden'] = numero_orden
                    self.forms[numero_bucle].instance.orden = numero_orden
        # Save New
        for form in range(rango):
            if not self.forms[form].cleaned_data['DELETE']:
                #print(self.forms[form].instance, ' : ', self.forms[form].instance.color, ' : ', self.forms[form].instance.orden, ' : ', self.forms[form].cleaned_data['DELETE']) 
                self.forms[form].instance.save()
        #print('-----')
        for form in range(len(self.forms)):
            if self.forms[form].cleaned_data['DELETE']:
                #print(self.forms[form].instance, ' : ', self.forms[form].instance.color, ' : ', self.forms[form].instance.orden, ' : ', self.forms[form].cleaned_data['DELETE']) 
                self.forms[form].instance.delete()
# ----------------------------------------------- end --------------------------------------------

# Form color
class ColorForm(forms.ModelForm):

    def clean(self):
        capitalize = self.cleaned_data['color'].capitalize()
        self.cleaned_data['color'] = capitalize
        self.instance.color = capitalize
        try:
            if Colore.objects.get(color=capitalize):
                raise forms.ValidationError('Este color ya ha sido registrado antes.')
        except (ObjectDoesNotExist):
            return super().clean()