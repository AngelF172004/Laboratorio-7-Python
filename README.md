Laboratorio 7: Python
Paradigmas de la programación
![image](https://github.com/user-attachments/assets/41dde63c-fb79-4dfa-a7a0-59bde870d0ca)

Daniel Enrique Cortes Santos   
Edson Fragoso Manjarrez     
Emilio García López    
Ángel Fernando Morán Hernández  
Jorge Eduardo Vázquez Villagrán

Introducción:
El código trabajado en la practica consiste en un registro de estudiantes que consta de 3 partes principales.
La primera es el guardado de su nombre.
La segunda es el guardado de 3 calificaciones diferentes.
La tercera es hacer un promedio en base a las calificaciones, mismo dato que se usará para concluir si el alumno está aprobado o reprobado.
Este es un sistema que ayuda a observar que estudiantes necesitaran de apoyos extras para pasar sus materias, como lo pueden ser los cursos de estudio o el uso de exámenes extraordinarios o ETS.
El código fue hecho en Python y es el siguiente:
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def evaluar_aprobacion(promedio):
    return "Aprobado" if promedio >= 6.0 else "Reprobado"

def main():
    estudiantes = []
    aprobados = 0
    reprobados = 0

    cantidad = int(input("¿Cuántos estudiantes quieres registrar? "))

    for i in range(cantidad):
        print(f"\nEstudiante {i + 1}")
        nombre = input("Nombre del estudiante: ")
        calificaciones = []
        for j in range(3):
            nota = float(input(f"Calificación {j + 1}: "))
            calificaciones.append(nota)

        promedio = calcular_promedio(calificaciones)
        estado = evaluar_aprobacion(promedio)

        if estado == "Aprobado":
            aprobados += 1
        else:
            reprobados += 1

        estudiante = {
            "nombre": nombre,
            "calificaciones": calificaciones,
            "promedio": promedio,
            "estado": estado
        }

        estudiantes.append(estudiante)

    print("\n--- Resultados ---")
    for est in estudiantes:
        print(f"Nombre: {est['nombre']}")
        print(f"  Calificaciones: {est['calificaciones']}")
        print(f"  Promedio: {est['promedio']:.2f}")
        print(f"  Estado: {est['estado']}\n")

    print(f"Total Aprobados: {aprobados}")
    print(f"Total Reprobados: {reprobados}")

# Ejecutar el programa
main()

Descripción general del código:
Una de las funciones principales es el solicitar información de uno o varios estudiantes.
Esto se hace con funciones como int o float.
Estos datos se guardan en el nombre, las calificaciones, el promedio y el estado de cada alumno para luego ser mostrados.
Como se menciono anteriormente, el promedio es una simple operación que consiste en la suma de las 3 calificaciones, que más tarde se divide entre 3.
La condición para que un alumno apruebe, es que su promedio sea igual o mayor a 6, caso contrario el alumno estará reprobado.
Finalmente, los datos serán mostrados en pantalla para su lectura.
Un dato que será mostrado es la cantidad de alumnos aprobados y reprobados, como algo extra y que no entra en el arreglo de cada estudiante.

Explicación paso a paso:
Función calcular_promedio: Recibe una lista de calificaciones numéricas, mismas que suma y al resultado lo divide entre la cantidad de números que recibió. Devuelve como salida el promedio de las calificaciones.
Función evaluar_aprobación: Recibe el promedio de la función anterior, y usa un operador ternario para decidir si el alumno aprueba. El alumno aprueba si el promedio es mayor o igual a 6, devolviendo ese estado. En caso contrario, devuelve el estado reprobado. Ambos se hacen a través de una cadena de texto.
Función main:
Primero inicia las listas y contadores (Estudiantes; junto a su información y cuantos aprobados/reprobados hay).
Al hacer eso pide al usuario la cantidad de estudiantes que habrá, para así reservar el espacio pertinente.
Con ese número, inicia un bucle de registros de los datos (Nombre y calificaciones).
De paso calcula el promedio y el estado llamando a las funciones anteriores.
Finalmente actualiza la información, la guarda y la muestra en pantalla.
Ejemplo de ejecución:
 
Traducción del código a lenguaje C++:
#include <iostream>
#include <vector>
#include <string>
#include <iomanip> // para std::setprecision

using namespace std;

// Función para calcular el promedio
float calcular_promedio(const vector<float>& calificaciones) {
    float suma = 0.0;
    for (float nota : calificaciones) {
        suma += nota;
    }
    return suma / calificaciones.size();
}

// Función para evaluar la aprobación
string evaluar_aprobacion(float promedio) {
    return (promedio >= 6.0) ? "Aprobado" : "Reprobado";
}

// Función principal
int main() {
    vector<struct Estudiante> estudiantes;
    int aprobados = 0, reprobados = 0;
    int cantidad;

    cout << "¿Cuántos estudiantes quieres registrar? ";
    cin >> cantidad;

    // Definición de la estructura Estudiante
    struct Estudiante {
        string nombre;
        vector<float> calificaciones;
        float promedio;
        string estado;
    };

    for (int i = 0; i < cantidad; ++i) {
        cout << "\nEstudiante " << (i + 1) << endl;

        Estudiante est;
        cout << "Nombre del estudiante: ";
        cin.ignore(); // Limpiar el buffer antes de getline
        getline(cin, est.nombre);

        est.calificaciones.resize(3);
        for (int j = 0; j < 3; ++j) {
            cout << "Calificación " << (j + 1) << ": ";
            cin >> est.calificaciones[j];
        }

        est.promedio = calcular_promedio(est.calificaciones);
        est.estado = evaluar_aprobacion(est.promedio);

        if (est.estado == "Aprobado")
            aprobados++;
        else
            reprobados++;

        estudiantes.push_back(est);
    }

    // Mostrar resultados
    cout << "\n--- Resultados ---\n";
    for (const auto& est : estudiantes) {
        cout << "Nombre: " << est.nombre << endl;
        cout << "  Calificaciones: ";
        for (float nota : est.calificaciones) {
            cout << nota << " ";
        }

        cout << "\n  Promedio: " << fixed << setprecision(2) << est.promedio << endl;
        cout << "  Estado: " << est.estado << "\n" << endl;
    }

    cout << "Total Aprobados: " << aprobados << endl;
    cout << "Total Reprobados: " << reprobados << endl;

    return 0;
}

Conclusiones:
El uso de arreglos y vectores en el lenguaje Python es mucho más sencillo.
Afortunadamente no hubo dificultades, sin embargo:
El código podría mejorar limitando los valores de las calificaciones (No tomando valores menores a 0 o mayores a 10).
Otra implementación importante es dar limitaciones al programa para que no devuelva errores en caso de recibir caracteres no válidos.
La lectura del lenguaje Python es muy sencilla, ya que es demasiado parecida al lenguaje ingles donde puedes hacer instrucciones sin llamar a muchas funciones.
Es una buena práctica para iniciar.


