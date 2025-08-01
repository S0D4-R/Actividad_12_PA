student_compendium = {}
try:
    max_students = int(input("Cuántos estudiantes desea agregar: "))
    for student in range(max_students):
        code = input("Coloque el código del estudiante: ")
        name = input("Coloque el nombre del estudiante: ")
        #Cantidad de notas
        max_scores = int(input("Coloque cuántas notas desea agregar: "))
        counter = 0
        score_compendium = []
        for score in range(max_scores):
            counter += 1
            temp_score = int(input("Coloque la nota del curso {}: ".format(counter)))
            score_compendium.append(temp_score)
        student_compendium[code] = {
            "nombre": name,
            "score_avg": score_compendium
        }

    #promedio
    print("-----El promedio de cada alumno fue:\n\n")
    for id, student in student_compendium:
        total_scr = 0
        counter = 0
        for score in student["score_avg"]:
            counter += 1
            total_scr += score
        total_scr = total_scr/counter
        print(f"{student["nombre"]} tiene un promedio general de {total_scr} ")
except ValueError:
    print("Lo que usted colocó no es un número")
except ZeroDivisionError:
    print("No puede dividir por cero...")
except Exception as e:
    print("Hubo un error: {}".format(e))