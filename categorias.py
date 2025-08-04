import json

def cargar_categoria():
    with open('data/categorias.json','r', encoding='utf-8') as f:
        return json.load(f)

def guardar_categoria(lista):
    with open('data/categorias.json','w', encoding='utf-8') as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

def mostrar_categoria():
    lista = cargar_categoria()
    for c in lista:
        print('nombre:', c['nombre'])
        print('descropcion:', c['descripcion'])
        print('-' * 30)

def agregar_categoria():
    nombre = input('nombre:  ')
    descripcion = input('descripcion:  ')
    lista = cargar_categoria()
    lista.append({'nombre': nombre, 'descripcion':descripcion})
    guardar_categoria(lista)
    print('categoria agregada')

def actualizar_categoria():
    nombre = input('nombre de la categoria:')
    lista = cargar_categoria()
    for categoria in lista:
        if categoria['nombre'].lower() == nombre.lower():
            categoria['descripcion'] = input('nueva descripcion:')
            guardar_categoria(lista)
            print('actualizada.')
            return
    print('no encontrada.')

def eliminar_categoria():
    nombre = input("Nombre a eliminar: ")
    lista = cargar_categoria()
    nueva = [c for c in lista if c["nombre"].lower() != nombre.lower()]
    guardar_categoria(nueva)
    print("Eliminada si existía.")
    