from utilidades import BOVEDA, MAX_SERVICIOS, obtener_fecha_actual, escribir_log, buscar_indice_por_nombre
from seguridad import cifrar_cesar, descifrar_cesar, cifrar_recursivo, descifrar_recursivo, DESPLAZAMIENTO
from analisis import analizar_fuerza

# --- CRUD ---

def agregar_contrasena():
    """Agrega un nuevo registro de contrasena."""
    if len(BOVEDA) >= MAX_SERVICIOS:
        print("[!] La boveda esta llena.")
        return

    print("\n--- Agregar Nueva Contrasena ---")
    nombre_servicio = input("Ingrese Nombre del Servicio: ")
    usuario_correo = input("Ingrese Usuario/Correo: ")
    contrasena_plana = input("Ingrese la Contrasena: ")

    analizar_fuerza(contrasena_plana)

    print("\nSeleccione Metodo de Cifrado:\n1. Cifrado Cesar\n2. Cifrado Recursivo")
    try:
        opcion_cifrado = int(input(">> Opcion: "))
    except ValueError:
        opcion_cifrado = 1 # Por defecto

    if opcion_cifrado == 2:
        contrasena_cifrada = cifrar_recursivo(contrasena_plana)
        metodo_cifrado = "RECURSIVO"
    else:
        contrasena_cifrada = cifrar_cesar(contrasena_plana, DESPLAZAMIENTO)
        metodo_cifrado = "CESAR"

    nuevo_registro = {
        'nombre_servicio': nombre_servicio,
        'usuario_correo': usuario_correo,
        'contrasena_cifrada': contrasena_cifrada,
        'metodo_cifrado': metodo_cifrado,
        'fecha_registro': obtener_fecha_actual(),
        'es_valido': True # Para eliminacion logica/revision de integridad
    }

    BOVEDA.append(nuevo_registro)
    print(f"\n[OK] Contrasena de '{nombre_servicio}' agregada y cifrada con exito.")
    escribir_log(f"Anadida contrasena para \"{nombre_servicio}\".")

def consultar_contrasenas():
    """Consulta y lista las contrasenas."""
    if not BOVEDA:
        print("[!] La boveda esta vacia.")
        return

    print("\n--- Listado de Contrasenas ---")
    valid_indices = [i for i, reg in enumerate(BOVEDA) if reg.get('es_valido', True)]
    
    for i in valid_indices:
        reg = BOVEDA[i]
        print(f"{i + 1}. Servicio: {reg['nombre_servicio']} | Usuario: {reg['usuario_correo']} | Fecha: {reg['fecha_registro']}")

    try:
        indice_a_mostrar = int(input("\nIngrese el numero de registro para ver (o 0 para volver): "))
        if indice_a_mostrar == 0 or indice_a_mostrar > len(BOVEDA):
            return

        i = indice_a_mostrar - 1
        if i not in valid_indices:
            print("[!] Indice invalido o registro no valido.")
            return

        reg = BOVEDA[i]
        print(f"\nDetalles de {reg['nombre_servicio']}:")
        print(f"  - Usuario: {reg['usuario_correo']}")
        print(f"  - Cifrado usado: {reg['metodo_cifrado']}")
        print(f"  - Contrasena (Cifrada): {reg['contrasena_cifrada']}")

        if input("Desea descifrar y mostrar la contrasena (S/N)? ").upper() == 'S':
            metodo = reg['metodo_cifrado']
            cifrada = reg['contrasena_cifrada']
            
            if metodo == "CESAR":
                descifrada = descifrar_cesar(cifrada, DESPLAZAMIENTO)
            elif metodo == "RECURSIVO":
                descifrada = descifrar_recursivo(cifrada)
            else:
                descifrada = "[!] Metodo no reconocido."
                
            print(f"  - **Contrasena Descifrada**: {descifrada}")
        escribir_log("Se consulto el listado de contrasenas.")
            
    except ValueError:
        print("[!] Entrada invalida.")


# --- Busqueda Inteligente (Recursiva) ---

def buscar_recursivo_aux(texto_buscado, indice):
    """Funcion recursiva que busca coincidencias parciales."""
    # CASO BASE 1: Si se ha revisado toda la lista
    if indice >= len(BOVEDA):
        return -1
    
    registro = BOVEDA[indice]
    
    # Comprobacion de coincidencia parcial
    if registro['nombre_servicio'].lower().find(texto_buscado.lower()) != -1 or \
       registro['usuario_correo'].lower().find(texto_buscado.lower()) != -1:
        return indice # CASO BASE 2: Encontrado
        
    # PASO RECURSIVO: Llamar a la funcion para el siguiente indice
    return buscar_recursivo_aux(texto_buscado, indice + 1)

def buscar_inteligente_interfaz():
    """Interfaz para iniciar la busqueda recursiva."""
    texto_buscado = input(">> Ingrese texto a buscar (servicio/usuario): ")
    indice = buscar_recursivo_aux(texto_buscado, 0)
    
    if indice != -1:
        reg = BOVEDA[indice]
        print(f"\n[+] Coincidencia encontrada (Recursiva): {reg['nombre_servicio']} | Usuario: {reg['usuario_correo']}")
    else:
        print("[!] No se encontraron coincidencias.")
    escribir_log("Se realizo una busqueda inteligente.")

# --- Revisión de Integridad (Recursiva) ---

def revisar_integridad_aux(indice):
    """Funcion recursiva para verificar y reparar registros."""
    # CASO BASE: Se revisaron todos los registros
    if indice >= len(BOVEDA):
        print("\n[OK] Revision de integridad recursiva finalizada.")
        return

    registro = BOVEDA[indice]
    
    if registro.get('es_valido', True):
        print(f"Revisando registro {indice + 1} ({registro['nombre_servicio']})... ", end="")

        reparado = False
        
        # 1. Entradas incompletas
        if not registro.get('nombre_servicio') or not registro.get('usuario_correo'):
            print("[ADVERTENCIA] Registro incompleto. MARCANDO como invalido.")
            registro['es_valido'] = False
            reparado = True

        # 2. Contrasenas sin cifrar (o muy cortas)
        elif len(registro['contrasena_cifrada']) < 4:
             print("[ALERTA] Contrasena sin cifrar o muy corta. REPARAR: 'Vacio'.")
             registro['contrasena_cifrada'] = "Vacio"
             escribir_log("Reparada contrasena muy corta/sin cifrar en revision de integridad.")
             reparado = True
             
        # 3. Metodos no reconocidos
        elif registro.get('metodo_cifrado') not in ["CESAR", "RECURSIVO"]:
            print("[ADVERTENCIA] Metodo de cifrado no reconocido. ASIGNANDO CESAR.")
            registro['metodo_cifrado'] = "CESAR"
            escribir_log("Reparado metodo de cifrado no reconocido.")
            reparado = True
        
        if not reparado:
            print("OK.")

    # PASO RECURSIVO: Llamar para el siguiente indice
    revisar_integridad_aux(indice + 1)

def revisar_integridad_recursiva_interfaz():
    """Interfaz para iniciar la revision de integridad."""
    print("\n--- Revision de Integridad (Recursiva) ---")
    if not BOVEDA:
        print("[OK] La boveda esta vacia. No hay nada que revisar.")
        return
    revisar_integridad_aux(0)
    
def editar_contrasena():
    """Edita un registro de contrasena."""
    print("\n--- Editar Contrasena ---")
    texto_buscado = input("Ingrese nombre del servicio o usuario a buscar: ")
    indice = buscar_indice_por_nombre(texto_buscado)

    if indice != -1 and BOVEDA[indice].get('es_valido', True):
        reg = BOVEDA[indice]
        print(f"\n[+] Registro encontrado: {reg['nombre_servicio']} | Usuario: {reg['usuario_correo']}")
        
        nueva_contrasena_plana = input("Ingrese la NUEVA Contrasena: ")
        analizar_fuerza(nueva_contrasena_plana)

        # Re-cifrar con el mismo metodo
        metodo = reg['metodo_cifrado']
        if metodo == "CESAR":
            nueva_cifrada = cifrar_cesar(nueva_contrasena_plana, DESPLAZAMIENTO)
        elif metodo == "RECURSIVO":
            nueva_cifrada = cifrar_recursivo(nueva_contrasena_plana)
        else:
            print("[!] Error: Metodo de cifrado desconocido. Usando CESAR.")
            nueva_cifrada = cifrar_cesar(nueva_contrasena_plana, DESPLAZAMIENTO)
        
        reg['contrasena_cifrada'] = nueva_cifrada
        print(f"[OK] Contrasena de '{reg['nombre_servicio']}' actualizada.")
        escribir_log(f"Editada contrasena para \"{reg['nombre_servicio']}\".")
        
    else:
        print("[!] No se encontro ningun registro que coincida con la busqueda o no es valido.")

def eliminar_contrasena():
    """Elimina (logicamente) un registro de contrasena."""
    print("\n--- Eliminar Contrasena ---")
    texto_buscado = input("Ingrese nombre del servicio o usuario a ELIMINAR: ")
    indice = buscar_indice_por_nombre(texto_buscado)

    if indice != -1 and BOVEDA[indice].get('es_valido', True):
        servicio = BOVEDA[indice]['nombre_servicio']
        confirmacion = input(f"\n[!] CONFIRMACION: Desea eliminar '{servicio}' (S/N)? ").upper()

        if confirmacion == 'S':
            # Eliminacion logica
            BOVEDA[indice]['es_valido'] = False
            print(f"[OK] Contrasena de '{servicio}' eliminada logicamente.")
            escribir_log(f"Eliminada contrasena para \"{servicio}\".")
        else:
            print("[!] Eliminacion cancelada.")
    else:
        print("[!] No se encontro ningun registro que coincida con la busqueda o no es valido.")
