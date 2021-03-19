"""."""

# Django
from wds_store.extras.models import Imagenes
from django.urls import (
    reverse_lazy,
    reverse
)
from django.views.generic import (
    TemplateView,
    DeleteView,
    CreateView,
    UpdateView
)

# Models
from wds_store.shirts.models import (
    Celebration, 
    Item,
    Producto,
    Color, Talla
)

class Menu(TemplateView):
    """."""
    template_name = "menu/index&listados.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        context['celebraciones'] = Celebration.objects.all()
        context['colores'] = Color.objects.all()
        context['items'] = Item.objects.all()
        return context

# ------------------------------------------ end category -----------------------------------------

class ItemList(TemplateView):
    """."""
    template_name = "menu/filtrar_items.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['options'] = False
        if kwargs['modelo'] == 'producto':
            producto = Producto.objects.get(nombre=kwargs['objeto'])
            context['tallas'] = Talla.objects.filter(producto=producto)
            context['items'] = Item.objects.filter(producto=producto)
            context['imagenes'] = Imagenes.objects.filter(imagen_principal='SI')
            context['objeto'] = kwargs['objeto']
        if kwargs['modelo'] == 'celebracion':
            celebracion = Celebration.objects.get(nombre=kwargs['objeto'])
            context['items'] = Item.objects.filter(celebracion=celebracion)
            context['imagenes'] = Imagenes.objects.filter(imagen_principal='SI')
        if kwargs['modelo'] == 'color':
            color = Color.objects.get(nombre=kwargs['objeto'])
            context['imagenes'] = Imagenes.objects.filter(color=color, orden=0)
            context['modelo'] = 'imagen'
        if kwargs['modelo'] == 'talla':
            talla = Talla.objects.get(talla=kwargs['objeto'])
            context['items'] = Item.objects.filter(talla=talla)
            context['imagenes'] = Imagenes.objects.filter(imagen_principal='SI')
            context['modelo'] = 'Item'
            context['objeto'] = kwargs['objeto']
        return context

# ------------------------------------------ end category -----------------------------------------

class DeleteView(DeleteView):
    """."""
    template_name = "menu/confirm_delete.html"

    def get_object(self):
        if self.kwargs['modelo'] == 'producto':
            objeto = Producto.objects.get(nombre=self.kwargs['objeto'])
        if self.kwargs['modelo'] == 'celebracion':
            objeto = Celebration.objects.get(nombre=self.kwargs['objeto'])
        if self.kwargs['modelo'] == 'color':
            objeto = Color.objects.get(nombre=self.kwargs['objeto'])
        if self.kwargs['modelo'] == 'talla':
            objeto = Talla.objects.get(talla=self.kwargs['objeto'])
        return objeto
    
    def get_success_url(self):
        if self.kwargs['modelo'] == 'producto':
            modelo = 'productos'
        if self.kwargs['modelo'] == 'celebracion':
            modelo = 'celebraciones'
        if self.kwargs['modelo'] == 'color':
            modelo = 'colores'
        if self.kwargs['modelo'] == 'talla':
            modelo = 'tallas'
        return reverse('items:menu')

# ------------------------------------------ end category -----------------------------------------

class UpdateView(UpdateView):
    """."""
    template_name = "menu/create&update.html"

    def get_object(self):
        if self.kwargs['modelo'] == 'producto':
            objeto = Producto.objects.get(nombre=self.kwargs['objeto'])
        if self.kwargs['modelo'] == 'celebracion':
            objeto = Celebration.objects.get(nombre=self.kwargs['objeto'])
        if self.kwargs['modelo'] == 'color':
            objeto = Color.objects.get(nombre=self.kwargs['objeto'])
        if self.kwargs['modelo'] == 'talla':
            objeto = Talla.objects.get(talla=self.kwargs['objeto'])
        return objeto
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['modelo'] == 'producto':
            context['modelo'] = 'Producto'
        if self.kwargs['modelo'] == 'celebracion':
            context['modelo'] = 'Celebracion'
        if self.kwargs['modelo'] == 'color':
            context['modelo'] = 'Color'
        if self.kwargs['modelo'] == 'talla':
            context['modelo'] = 'Talla'
            context['productos_checked'] = [producto.nombre for producto in self.object.producto.all()]
            context['slugname'] = self.kwargs['slugname']
            context['list'] = Producto.objects.all()
        return context
    
    def get_form_class(self):
        if self.kwargs['modelo'] == 'talla':
            fields = ['talla','orden','producto']
            self.fields = fields
        else:
            fields = ['nombre']
            self.fields = fields
        return super().get_form_class()
    
    def get_success_url(self):
        if self.kwargs['modelo'] in ['producto', 'celebracion', 'color', 'talla']:
            if self.kwargs['modelo'] == 'producto':
                modelo = 'productos'
                slugname = self.kwargs['objeto']
            if self.kwargs['modelo'] == 'celebracion':
                modelo = 'celebraciones'
                slugname = self.kwargs['objeto']
            if self.kwargs['modelo'] == 'color':
                modelo = 'colores'
                slugname = self.kwargs['objeto']
            if self.kwargs['modelo'] == 'talla':
                modelo = 'tallas'
                slugname = self.kwargs['slugname']
            return reverse('items:menu')

# ------------------------------------------ end category -----------------------------------------

class CreateView(CreateView):
    """."""
    template_name = "menu/create&update.html"

    def get_queryset(self):
        if self.kwargs['modelo'] == 'producto':
            queryset = Producto.objects.all()
        if self.kwargs['modelo'] == 'celebracion':
            queryset = Celebration.objects.all()
        if self.kwargs['modelo'] == 'color':
            queryset = Color.objects.all()
        if self.kwargs['modelo'] == 'item':
            queryset = Item.objects.all()
        if self.kwargs['modelo'] == 'talla':
            queryset = Talla.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['modelo'] == 'producto':
            context['modelo'] = 'Producto'
        if self.kwargs['modelo'] == 'celebracion':
            context['modelo'] = 'Celebracion'
        if self.kwargs['modelo'] == 'color':
            context['modelo'] = 'Color'
        if self.kwargs['modelo'] == 'talla':
            context['modelo'] = 'Talla'
            context['slugname'] = self.kwargs['slugname']
            context['list'] = Producto.objects.all()
        if self.kwargs['modelo'] == 'item':
            context['modelo'] = 'Item'
            context['slugname'] = Producto.objects.get(nombre=self.kwargs['slugname'])
            context['tallas'] = Talla.objects.filter(producto=context['slugname'])
            context['celebraciones'] = Celebration.objects.all()
        return context
    
    def get_form_class(self):
        if self.kwargs['modelo'] == 'talla':
            fields = ['talla', 'orden', 'producto']
            self.fields = fields
        if self.kwargs['modelo'] in ['producto', 'celebracion', 'color']:
            fields = ['nombre']
            self.fields = fields
        if self.kwargs['modelo'] == 'item':
            fields = ['producto', 'publico', 'talla', 'celebracion']
            self.fields = fields
        return super().get_form_class()

    def get_success_url(self):
        if self.kwargs['modelo'] in ['producto', 'celebracion', 'color', 'talla']:
            if self.kwargs['modelo'] == 'producto':
                modelo = 'productos'
                slugname = self.kwargs['slugname']
            if self.kwargs['modelo'] == 'celebracion':
                modelo = 'celebraciones'
                slugname = self.kwargs['slugname']
            if self.kwargs['modelo'] == 'color':
                modelo = 'colores'
                slugname = self.kwargs['slugname']
            if self.kwargs['modelo'] == 'talla':
                modelo = 'tallas'
                slugname = self.kwargs['slugname']
            return reverse('items:menu')
        if self.kwargs['modelo'] in ['item', 'imagen']:
            return reverse('items:menu')


# ------------------------------------------ end category -----------------------------------------