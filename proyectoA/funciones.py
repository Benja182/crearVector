import pickle
import random
import string
import os
import uuid
from registro import Eventos as Reg
from registro import to_string as linea


def crear_vector(vector):
    n = int(input('Ingrese la cantidad de datos a cargar: '))
    for i in range(n):
        codigo = random.randint(10000, 19999)
        titulo = random.randint(100, 199)
        descripcion = ''.join(random.choices(string.ascii_letters, k = 20))
        if descripcion[-1] != '.':
            descripcion += '.'
        # descripcion = str(uuid.uuid4())
        costo = float(random.uniform(100, 200))
        tipo = random.randint(0, 19)
        segmento = random.randint(0, 9)
        if i == (n - 1):
            descripcion = input('Ingrese la descripcion: ')

        reg = Reg(codigo, titulo, descripcion, costo, tipo, segmento)
        add_in_order(vector, reg)

    return vector


def add_in_order(vector, reg):
    izq, der = 0, len(vector) - 1
    pos = -1

    while izq <= der:
        c = (izq + der) // 2
        if vector[c].codigo == reg.codigo:
            pos = c
            break

        if reg.codigo <= vector[c].codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [reg]


def mostrar_vector(vector):
    texto = '=' * 140 + '\n'
    texto += '{:<15}\t{:<15}\t{:<50}\t{:<30}\t{:<15}\t{:<15}\n'.format('Codigo', 'Titulo', 'Descripcion', 'Costo', 'Tipo', 'Segmento')
    texto += '=' * 140 + '\n'
    for reg in vector:
        texto += linea(reg)
    print(texto)


def generar_archivo_bin(nombre_archivo, vector):
    m = open(nombre_archivo, mode='wb')
    p = float(input('Ingrese el costo de produccion minimo para guardar en el archivo: '))
    for reg in vector:
        if reg.costo > p:
            pickle.dump(reg, m)

    m.close()
    print(f'El archivo binario {nombre_archivo} fue creado y cargado con exito.')


def mostrar_archivo_bin(nombre_archivo):
    texto = '=' * 140 + '\n'
    texto += '{:<15}\t{:<15}\t{:<50}\t{:<30}\t{:<15}\t{:<15}\n'.format('Codigo', 'Titulo', 'Descripcion', 'Costo', 'Tipo', 'Segmento')
    texto += '=' * 140 + '\n'
    m = open(nombre_archivo, mode='rb')
    t = os.path.getsize(nombre_archivo)
    while m.tell() < t:
        reg = pickle.load(m)
        texto += linea(reg)

    print(texto)

    m.close()


def vector_montos_bin(nombre_archivo):
    m = open(nombre_archivo, mode='rb')
    t = os.path.getsize(nombre_archivo)
    montos = []

    while m.tell() < t:
        reg = pickle.load(m)
        if reg.tipo >= 5:
            montos.append(reg.costo)

    m.close()
    print(montos)
    print(f'El promedio de montos mostrados en el vector es de {promedio(sum(montos), len(montos))}.')


def promedio(n1, n2):
    if n2 != 0:
        return n1 / n2
    return 'no hay datos'


def busqueda(vector):
    cod = int(input('Ingrese el codigo de identificacion a buscar: '))
    for reg in vector:
        if reg.codigo == cod:
            mostrar_datos(reg)
            return reg.descrip

    print(f'No se encontro un codigo registrado igual a {cod}.')
    return ''


def mostrar_datos(reg):
    print(f'Codigo: {reg.codigo}.\n'
          f'Titulo: {reg.titulo}.\n'
          f'Descripcion: {reg.descrip}.\n'
          f'Costo: {reg.costo}.\n'
          f'Tipo: {reg.tipo}.\n'
          f'Segmento: {reg.segmento}.')


def generar_matriz(vector):
    matriz = [[0] * 10 for i in range(20)]
    for reg in vector:
        fila = reg.tipo
        columna = reg.segmento
        matriz[fila][columna] += 1
    mostrar_matriz(matriz)


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print()
        for j in range(len(matriz[0])):
            # print(f'Para el segmento {j} y codigo {i} hay {matriz[i][j]} eventos.')
            print(f' {matriz[i][j]}', end= '  ')
    print()


def analisis_descripcion(texto):
    palabra = ''
    cont = 0

    for letra in texto:

        if letra != ' ' and letra != '.':
            palabra += letra

        else:
            requisitos = buscar_criterios(palabra)
            palabra = ''
            if requisitos:
                cont += 1

    print(f'La cantidad de palabras que cumplieron con los requisitos son {cont}.')


def buscar_criterios(palabra):
    s_letra = False
    t_letra = False
    mayus = False
    for letra in palabra:
        if letra.lower() == 's':
            s_letra = True

        elif letra.lower() == 't':
            t_letra = True

        if palabra[0].isupper():
            mayus = True

    if s_letra and t_letra and mayus:
        return True
    return False
