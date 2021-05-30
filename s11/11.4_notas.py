# "Un alumno desea saber cual será su calificación final en la materia de
# Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 40% del promedio de sus tres calificaciones parciales, 50% de la
# calificación del examen final y 10% de la calificación de un trabajo final."


# PORCENTAJE_CALIFICACIONES = 0.40
# PORENTAJE_EXAMEN = 0.50
# PORCENTAJE_TRABAJO = 0.10

# cal1, cal2, cal3 = input("ingrese las calificaciones parciales").split()

# examen_final, trabajo_final = input(
#     "Ingrese la nota del examen final seguida de la nota del trabajo final separada por un espacio").split()

# nota_calificaciones = (
#     (float(cal1)+float(cal2) + float(cal3))/3)*PORCENTAJE_CALIFICACIONES
# nota_exam_final = float(examen_final)*PORENTAJE_EXAMEN
# nota_Trab_final = float(trabajo_final)*PORCENTAJE_TRABAJO
# nota_Definitiva = nota_calificaciones + nota_exam_final + nota_Trab_final

# print(f"su calificacion final es: {nota_Definitiva}")

# Ejercico de fecha de nacimiento
fechaNacimiento, fechaActual = input(
    "ingrese su fecha de nacimiento y su fecha actual de cumpleaños").split()

años = float(fechaActual) - float(fechaNacimiento)
print("tienes", int(años), "años")
