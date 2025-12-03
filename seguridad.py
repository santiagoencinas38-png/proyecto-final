from utilidades import MASTER_FILE, escribir_log, BOVEDA
from functools import reduce
DESPLAZAMIENTO = 3
MAX_FALLOS_MASTER = 3

# --- Cifrado Cesar ---

def cifrar_cesar(texto, desplazamiento):
    """Implementa el Cifrado César."""
    resultado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            # Mantiene el desplazamiento dentro del alfabeto (26 letras)
            resultado += chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            resultado += chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
        elif '0' <= char <= '9':
            # Mantiene el desplazamiento dentro de los digitos (10)
            resultado += chr((ord(char) - ord('0') + desplazamiento) % 10 + ord('0'))
        else:
            resultado += char
    return resultado

def descifrar_cesar(texto, desplazamiento):
    """Implementa el Descifrado César (desplazamiento negativo)."""
    return cifrar_cesar(texto, -desplazamiento)

# --- Cifrado Recursivo ---

def invertir_recursivo(cadena):
    """Invierte una cadena usando recursividad."""
    if not cadena:
        return ""
    # La funcion se llama a si misma con la subcadena, luego anade el primer caracter al final
    return invertir_recursivo(cadena[1:]) + cadena[0]

def cifrar_recursivo(texto):
    """Cifrado Recursivo: Invertir y luego César."""
    invertido = invertir_recursivo(texto)
    return cifrar_cesar(invertido, DESPLAZAMIENTO)

def descifrar_recursivo(texto):
    """Descifrado Recursivo: César inverso y luego Invertir."""
    descifrado_cesar = descifrar_cesar(texto, DESPLAZAMIENTO)
    return invertir_recursivo(descifrado_cesar)

# --- Contraseña Maestra ---

def verificar_master():
    """Verifica la Contraseña Maestra."""
    try:
        with open(MASTER_FILE, "r") as f:
            master_cifrada = f.read().strip()
    except FileNotFoundError:
        print("\nERROR: Archivo Maestro no encontrado. Ejecute la inicializacion.")
        return False
    
    master_descifrada = descifrar_cesar(master_cifrada, DESPLAZAMIENTO)
    
    intentos = 0
    while intentos < MAX_FALLOS_MASTER:
        entrada_usuario = input(">> Ingrese la Contrasena Maestra: ")
        if entrada_usuario == master_descifrada:
            print("\n--- ACCESO CONCEDIDO ---\n")
            return True
        else:
            intentos += 1
            print(f"[!] Contrasena incorrecta. Intento {intentos} de {MAX_FALLOS_MASTER}.")
    
    print("\n--- ACCESO DENEGADO. Sistema Bloqueado. ---\n")
    escribir_log("Sistema bloqueado por fallos de Contrasena Maestra.")
    return False
