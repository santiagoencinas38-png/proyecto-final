from datetime import datetime
import json

# --- Constantes y Estructura Global ---
MAX_SERVICIOS = 100
# La boveda sera una lista de diccionarios
BOVEDA = [] 
MASTER_FILE = "master.pydata"
BOVEDA_FILE = "boveda.json"
LOG_FILE = "audit_log.txt"

def obtener_fecha_actual():
    """Retorna la fecha actual en formato DD/MM/AAAA."""
    return datetime.now().strftime("%d/%m/%Y")

def obtener_fecha_hora_log():
    """Retorna la fecha y hora en formato [AAAA-MM-DD HH:MM] para el log."""
    return datetime.now().strftime("[%Y-%m-%d %H:%M]")

def escribir_log(mensaje):
    """Registra una accion en el archivo de log."""
    with open(LOG_FILE, "a") as f:
        f.write(f"{obtener_fecha_hora_log()} {mensaje}\n")

def buscar_indice_por_nombre(texto_buscado):
    """Busca un servicio o usuario por coincidencia parcial."""
    texto_buscado = texto_buscado.lower()
    for i, registro in enumerate(BOVEDA):
        if texto_buscado in registro['nombre_servicio'].lower() or \
           texto_buscado in registro['usuario_correo'].lower():
            return i
    return -1
