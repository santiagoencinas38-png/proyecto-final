from utilidades import MASTER_FILE, BOVEDA_FILE, BOVEDA, escribir_log
from seguridad import cifrar_cesar, DESPLAZAMIENTO
import json
import os

def inicializar_master():
    """Solicita y guarda la Contraseña Maestra cifrada si no existe."""
    if os.path.exists(MASTER_FILE):
        return
    
    print("\n--- INICIALIZACION ---\n")
    master_plana = input(">> Primera ejecucion. Defina su Contrasena Maestra: ")
    
    master_cifrada = cifrar_cesar(master_plana, DESPLAZAMIENTO)
    
    with open(MASTER_FILE, "w") as f:
        f.write(master_cifrada)
        
    print("Contrasena Maestra guardada y cifrada.")
    escribir_log("Contrasena Maestra inicializada por primera vez.")

def guardar_boveda():
    """Guarda la lista BOVEDA en un archivo JSON."""
    # Usamos JSON para guardar estructuras de datos Python de forma legible
    try:
        with open(BOVEDA_FILE, "w") as f:
            json.dump(BOVEDA, f, indent=4)
        escribir_log("Boveda de contrasenas guardada correctamente.")
    except Exception as e:
        print(f"ERROR al guardar la boveda: {e}")

def cargar_boveda():
    """Carga la lista BOVEDA desde un archivo JSON."""
    global BOVEDA 
    try:
        with open(BOVEDA_FILE, "r") as f:
            # Sobreescribir el global BOVEDA
            BOVEDA.extend(json.load(f))
        escribir_log("Boveda de contrasenas cargada al iniciar.")
    except FileNotFoundError:
        print("INFO: Archivo de boveda no encontrado. Se iniciara una nueva boveda vacia.")
    except json.JSONDecodeError:
        print("ALERTA: El archivo de boveda esta corrupto o vacio. Iniciando boveda vacia.")
