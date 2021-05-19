# Nota de talleres
print('notas talleres')
taller1 = float(input('Inserte la primer nota-:'))
taller2 = float(input('Inserte la segunda nota-:'))
taller3 = float(input('Inserte la tercera nota nota-:'))
NotaTaller = ((taller1+taller2+taller3)/3)*0.30

#  Nota evaluaciones
print('notas evaluaciones')
evaluacion1 = float(input('Inserte la primer nota-:'))
evaluacion2 = float(input('Inserte la segunda nota-:'))
NotaEvalua = ((evaluacion1+evaluacion2)/2)*0.30

#  Nota trabajo final
print('notas trabajo final')
trabajo = float(input('Inserte la primer nota-:'))
sustentacion = float(input('Inserte la segunda nota-:'))
notaTraFinal = ((trabajo+sustentacion)/2)*0.40

# Calcular nota final
notaFinal = round(notaTraFinal+NotaTaller+NotaEvalua, 2)
print(notaFinal)
