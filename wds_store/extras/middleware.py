"""Middleware para el admin."""

# Django
from django.shortcuts import redirect

class AdminPathMiddleware:
    """Nueva ruta para el admin despues del log in."""

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        """Codigo para cambiar la ruta."""
        if request.path in ['/admin/', '/admin/extras/']:
            return redirect('/admin/shirts/')
        
        response = self.get_response(request)
        return response