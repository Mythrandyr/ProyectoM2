#Esta funcion es para mostrar mensaje y perdirte una palabra
while True:
    palabra = input('Introduce una palabra:')
    cantidadDeletras = len(palabra)
        
#esta funcion es para definir que pasa si es menor a 4
    if cantidadDeletras < 4:
        print('le faltan letras a tu palabra')
        print(f'tu texto tiene', {cantidadDeletras}, 'letras.\n')

 #esta funcion es para definir que pasa si es mayor a 8  
    elif cantidadDeletras > 8:
        print('sobran letras')
        print(f'tu texto tiene', {cantidadDeletras}, 'letras.\n')

#esta funcion es para definir que pasa si es = a 8 y mayor a 3   
    else:
        print('palabra correcta')
        print(f'tu texto tiene', {cantidadDeletras}, 'letras.\n') 
