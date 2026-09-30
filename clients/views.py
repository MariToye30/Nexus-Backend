from django.http import JsonResponse
from .models import Client

def client_list_view(request):
    # 1. Buscamos solo los clientes activos
    active_clients = Client.objects.filter(is_active=True).values('id', 'name', 'contact_email', 'is_active', 'created_at')
    
    # 2. Convertimos el resultado a una lista de Python
    data = list(active_clients)
    
    # 3. Devolvemos la respuesta en formato JSON
    return JsonResponse(data, safe=False)