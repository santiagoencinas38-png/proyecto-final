from persistencia import inicializar_master, cargar_boveda, guardar_boveda
from seguridad import verificar_master
from gestion_datos import agregar_contrasena, consultar_contrasenas, editar_contrasena, eliminar_contrasena, buscar_inteligente_interfaz, revisar_integridad_recursiva_interfaz
from analisis import generar_contrasena_interfaz, analizar_fuerza
from utilidades import escribir_log

def mostrar_menu():
    """Muestra el menu principal."""
    print("\n========================================")
    print("     🔐 SAFEKEY VAULT+ - MENU PRINCIPAL")
    print("========================================")
    print("1. Agregar Nueva Contrasena")
    print("2. Consultar / Listar Contrasenas")
    print("3. Editar Contrasena")
    print("4. Eliminar Contrasena")
    print("---")
    print("5. Analizar Fuerza de Contrasena (Prueba)")
    print("6. Generar Contrasena Segura")
    print("---")
    print("7. Buscar (Inteligente/Recursivo)")
    print("8. Revisar Integridad (Recursiva)")
    print("9. Salir (Guardar y Cerrar)")

def main():
    opcion = 0

    # 1. INICIALIZACION Y SEGURIDAD
    inicializar_master()
    cargar_boveda()

    if not verificar_master():
        return # Salir si falla la verificacion maestra

    # 2. BUCLE PRINCIPAL DEL MENU
    while opcion != 9:
        mostrar_menu()
        try:
            opcion = int(input(">> Seleccione opcion: "))
        except ValueError:
            opcion = 0
            
        if opcion == 1:
            agregar_contrasena()
        elif opcion == 2:
            consultar_contrasenas()
        elif opcion == 3:
            editar_contrasena()
        elif opcion == 4:
            eliminar_contrasena()
        elif opcion == 5:
            contrasena = input(">> Ingrese contrasena a analizar: ")
            analizar_fuerza(contrasena)
        elif opcion == 6:
            generar_contrasena_interfaz()
        elif opcion == 7:
            buscar_inteligente_interfaz()
        elif opcion == 8:
            revisar_integridad_recursiva_interfaz()
        elif opcion == 9:
            print("\nGuardando y saliendo...\n")
        else:
            print("\n[!] Opcion invalida. Intente de nuevo.")
            
    # 3. CIERRE
    guardar_boveda()
    escribir_log("Sistema SAFEKEY VAULT+ cerrado.")
    print("¡Adios!")

if __name__ == "__main__":
    main()
