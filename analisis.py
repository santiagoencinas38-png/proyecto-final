import random
import string
from utilidades import escribir_log

# --- Analizador de Fuerza ---

def analizar_fuerza(contrasena):
    """Analiza la calidad de una contrasena y clasifica su fuerza."""
    puntaje = 0
    longitud = len(contrasena)
    
    tiene_mayus = any(c.isupper() for c in contrasena)
    tiene_num = any(c.isdigit() for c in contrasena)
    # Comprobar si tiene simbolos (no alfanumericos ni espacios)
    tiene_simbolo = any(not c.isalnum() and not c.isspace() for c in contrasena)
    
    # 1. Longitud
    if longitud >= 12: puntaje += 15
    elif longitud >= 8: puntaje += 10
    else: puntaje += 5

    # 2. Tipos de caracteres
    if tiene_mayus: puntaje += 15
    if tiene_num: puntaje += 15
    if tiene_simbolo: puntaje += 15
    
    # 3. Patrones prohibidos (penalizacion)
    patrones_prohibidos = ["password", "123", "qwerty", "admin"]
    for patron in patrones_prohibidos:
        if patron in contrasena.lower():
            puntaje -= 20
            break

    # Clasificacion
    if puntaje >= 50:
        print(f"   -> Clasificacion: MUY FUERTE (Puntaje: {puntaje})")
    elif puntaje >= 35:
        print(f"   -> Clasificacion: Fuerte (Puntaje: {puntaje})")
    elif puntaje >= 20:
        print(f"   -> Clasificacion: Media (Puntaje: {puntaje})")
    else:
        print(f"   -> Clasificacion: Debil (Puntaje: {puntaje}). ¡Mejorela!")

# --- Generador de Contraseñas ---

def generar_contrasena(longitud, mayus, numeros, simbolos):
    """Genera una contrasena aleatoria basada en criterios."""
    
    caracteres_min = string.ascii_lowercase
    caracteres_pool = caracteres_min
    
    # Agrega a la pool segun las opciones, usando arreglos de Python (string.x)
    if mayus:
        caracteres_pool += string.ascii_uppercase
    if numeros:
        caracteres_pool += string.digits
    if simbolos:
        caracteres_pool += string.punctuation
        
    if not caracteres_pool:
        return ""

    # Usar random.choice() para seleccionar caracteres aleatorios del pool
    contrasena = ''.join(random.choice(caracteres_pool) for _ in range(longitud))
    return contrasena

def generar_contrasena_interfaz():
    """Interfaz para generar contrasena."""
    try:
        longitud = int(input("Longitud deseada (min 8): "))
        if longitud < 8:
            longitud = 8
        
        opt_mayus = input("Incluir Mayusculas (S/N): ").upper() == 'S'
        opt_num = input("Incluir Numeros (S/N): ").upper() == 'S'
        opt_simbolos = input("Incluir Simbolos (S/N): ").upper() == 'S'
        
        nueva_contrasena = generar_contrasena(longitud, opt_mayus, opt_num, opt_simbolos)
        
        print(f"\n>> Contrasena Generada: {nueva_contrasena}")
        analizar_fuerza(nueva_contrasena)
        escribir_log("Se genero una contrasena segura.")
    except ValueError:
        print("[!] Entrada invalida para la longitud.")
