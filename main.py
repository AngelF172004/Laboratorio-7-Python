def main():
    """Función principal que orquesta el programa"""
    cantidad = int(input("¿Cuántos estudiantes quieres registrar? "))
    estudiantes = ingresar_estudiantes(cantidad)
    mostrar_resultados(estudiantes)

# Ejecutar el programa
if __name__ == "__main__":
    main()