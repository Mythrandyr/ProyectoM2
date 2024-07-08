#proyecto m2
#este programa es para definir en que cuadrantes se localizan lo valores x & y
#este es para pedir los valores en x & y
while True:
  try:
    x = int (input ('Ingresa el valor de x: '))
    y = int (input ('Ingresa el valor de y: '))
    break #sale del bucle si se introducen los datos correctos
  except ValueError:
    print ('Datos incorrectos, por favor introduce informacion correcta (numeros enteros).')
#esta es para el origen
if x==0 and y==0:
    print ('Origen')
#esta es para eje y
elif x==0:
    print ('Eje Y')
#esta para eje x
elif y==0:
    print ('Eje X')
#esta es para cuadrantre 1
elif x>0 and y>0:
    print ('Cuadrante I')
#esta es para cuadrante 2
elif x<0 and y>0:
    print ('Cuadrante II')
#esta es para cuadrante 3
elif x<0 and y<0:
    print ('Cuadrante III')
#esta es para cuadrante 4
elif x>0 and y<0:
    print ('Cuadrante IV')
print ()
