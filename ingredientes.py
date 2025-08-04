import os
import json

ruta_ingredientes = "data/ingredientes.json"

def cargar_ingredientes():
    with open('data/ingredientes.json','r',encoding='utf-8')as archivo:
        datos = json.load(archivo)
    return datos

def guardar_ingredientes(lista):
    with open('data/ingredientes.json','w',encoding='utf-8') as archivo:
        json.dump(lista,archivo, indent =4, ensure_ascii= False)

def mostrar_ingredientes():
    ingrediente = cargar_ingredientes()
    for ingrediente in ingrediente:
        print('nombre:',ingrediente['nombre'])
        print('descripcion:',ingrediente['descripcion'])
        print('presio:',ingrediente['precio'])
        print('stock:',ingrediente['stock'])
        print('-' * 30)

def agregar_ingresiente():
    nombre = input('nombre del ingrediente: ')
    descripcion = input('descripcion: ')
    presio = input(float('presio: '))
    stock = input(float('stock: '))

    nuevo = {
        'nombre':nombre,
        'descripcion':descripcion,
        'presio':presio,
        'stock':stock,
    }

    lista = cargar_ingredientes()
    lista.append(nuevo)
    guardar_ingredientes(lista)
    print('ingrediente agregado con exito')

def actualizar_ingredientes():
    nombre = input('nombre del ingrediente a actualizar')
    lista = cargar_ingredientes()
    for ingredientes in lista:
        if ingredientes['nombre'].lower()==nombre.lower():
            nuevo_precio = float(input('nuevo presio'))
            nuevo_stock = float(input('nuevo stock'))
            ingredientes ['presio'] = nuevo_precio
            ingredientes ['stock'] = nuevo_stock
            guardar_ingredientes(lista)
            print('ingrediente actualizado.')
            return
    print('ingrediente no encontrado')

def eliminar_ingrediente():
    nombre = input('nombre del ingrediente a eliminar.')
    lista = cargar_ingredientes()
    nueva_lista =[]
    for ingredientes in lista:
        if ingredientes['nombre'].lower()!= nombre.lower():
            nueva_lista.append(ingredientes)
    guardar_ingredientes(nueva_lista)
    print('ingrediente elimindao con exito')

