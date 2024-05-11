from funciones import *


def menu():
    cadena = 'Menu de Opciones\n' + \
             '1. Cargar eventos.\n' + \
             '2. Mostrar eventos.\n' + \
             '3. Generar archivo binario.\n' + \
             '4. Mostrar archivo binario.\n' + \
             '5. Crear arreglo de montos por archivo binario.\n' + \
             '6. Busqueda de un codigo.\n' + \
             '7. Generar una matriz de contadores de codigos y segmentos.\n' + \
             '8. Analizar la descripcion.\n' + \
             '0. Salir. \n' + \
             'Ingrese la opcion que desea realizar: '

    return int(input(cadena))


def main():
    opcion = -1
    eventos = []
    archivo = ''
    descrip_buscada = ''

    while opcion != 0:

        opcion = menu()

        if opcion == 1:
            eventos = crear_vector(eventos)

        elif len(eventos) != 0:

            if opcion == 2:
                mostrar_vector(eventos)

            elif opcion == 3:
                # archivo = input('Ingrese el nombre que desea para el archivo: ')
                # archivo += '.aed'
                archivo = 'eventos.aed'
                generar_archivo_bin(archivo, eventos)

            elif opcion == 6:
                descrip_buscada = busqueda(eventos)

            elif opcion == 7:
                generar_matriz(eventos)

            elif opcion == 8:
                if descrip_buscada != '':
                    analisis_descripcion(descrip_buscada)
                else:
                    print('No se almaceno ninguna descripcion en el opcion 6.')

            elif os.path.exists(archivo):

                if opcion == 4:
                    mostrar_archivo_bin(archivo)

                elif opcion == 5:
                    vector_montos_bin(archivo)

            else:
                print('Todavia no se creo el archivo en la opcion 3.')

        else:
            print('Todavia no se cargo ningun dato en la opcion 1.')


if __name__ == '__main__':
    main()
