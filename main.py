import requests
import time
import os  # Importa os para acceder a las variables de entorno

# Lee la URL del webhook desde los secrets
url = os.environ['WEBHOOK_URL']  # Esto buscará el secret llamado WEBHOOK_URL

# Mensaje a enviar
message = {
    "content": "aqui tu texto "
}

# Configuración
cantidad_mensajes = 5
intervalo = 1  # segundos

# Enviar mensajes
for i in range(cantidad_mensajes):
    response = requests.post(url, json=message)
    if response.status_code == 204:
        print(f"[{i+1}] Mensaje enviado correctamente.")
    else:
        print(f"[{i+1}] Error al enviar mensaje: {response.status_code}")
    time.sleep(intervalo)
