def ingresar_estudiantes(cantidad):
    """Recoge los datos de los estudiantes y sus calificaciones"""
    estudiantes = []
    for i in range(cantidad):
        print(f"\nEstudiante {i + 1}")
        nombre = input("Nombre del estudiante: ")
        calificaciones = []
        for j in range(3):
            nota = float(input(f"Calificación {j + 1}: "))
            calificaciones.append(nota)
        
        promedio = calcular_promedio(calificaciones)
        estado = evaluar_aprobacion(promedio)
        
        estudiante = {
            "nombre": nombre,
            "calificaciones": calificaciones,
            "promedio": promedio,
            "estado": estado
        }
        estudiantes.append(estudiante)
    return estudiantes