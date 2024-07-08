#proyecto m2
#este programa es para definir en que cuadrantes se localizan lo valores x & y
#este es para pedir los valores en x & y
x = int (input ('Ingresa el valor de x: '))
y = int (input ('Ingresa el valor de y: '))
#esta es para el origen
if x==0 and y==0:
    print ('Origen')
#esta es para eje y
if x==0:
    print ('Eje Y')
#esta para eje x
if y==0:
    print ('Eje X')
#esta es para cuadrantre 1
if x>0 and y>0:
    print ('Cuadrante I')
#esta es para cuadrante 2
if x<0 and y>0:
    print ('Cuadrante II')
#esta es para cuadrante 3
if x<0 and y<0:
    print ('Cuadrante III')
#esta es para cuadrante 4
if x>0 and y<0:
    print ('Cuadrante VI')
print ()
