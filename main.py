import requests
import os

# URL de la API de Jaqiaru (¡ESTA ES UN EJEMPLO, debes usar la real!)
API_URL = "https://api.jaqiaru.ai/v1/tts" 
API_KEY = os.getenv("JAQIARU_API_KEY", "kamisaraki") # Es mejor usar variables de entorno

def texto_a_voz(texto, nombre_archivo_salida="output.wav"):
    """
    Envía texto a la API de Jaqiaru y guarda el audio resultante.
    """
    print(f"Enviando texto a la API: '{texto}'")
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "text": texto,
        "voice": "aymara_female_1" # Parámetro de ejemplo, ajústalo según la API
    }
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        
        # Verificar si la petición fue exitosa (código 200)
        if response.status_code == 200:
            # Guardar el contenido de la respuesta (el audio) en un archivo
            with open(nombre_archivo_salida, 'wb') as f:
                f.write(response.content)
            print(f"¡Éxito! Audio guardado en: {nombre_archivo_salida}")
        else:
            print(f"Error: La API respondió con el código {response.status_code}")
            print(f"Respuesta: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

# --- Punto de entrada del script ---
if __name__ == "__main__":
    texto_para_convertir = "Kamisaraki, jilata. Aka arux aymarat arsuñatakiwa."
    texto_a_voz(texto_para_convertir)
