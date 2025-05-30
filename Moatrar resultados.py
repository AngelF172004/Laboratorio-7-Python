def mostrar_resultados(estudiantes):
    """Muestra los resultados de todos los estudiantes"""
    print("\n--- Resultados ---")
    for est in estudiantes:
        print(f"Nombre: {est['nombre']}")
        print(f"  Calificaciones: {est['calificaciones']}")
        print(f"  Promedio: {est['promedio']:.2f}")
        print(f"  Estado: {est['estado']}\n")
    
    aprobados = sum(1 for est in estudiantes if est['estado'] == "Aprobado")
    reprobados = len(estudiantes) - aprobados
    print(f"Total Aprobados: {aprobados}")
    print(f"Total Reprobados: {reprobados}")
    