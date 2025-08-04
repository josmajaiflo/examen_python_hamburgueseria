import json

def cargar_hamburguesas():
    with open('data/hamburguesas.json','r', encoding='utf-8') as f:
        return json.load(f)
    
def guardar_hambueguesas(lista):
    with open('data/hamburguesas.json','w', encoding='utf-8') as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

def mostrar_hamburguesa():
    lista = cargar_hamburguesas()
    for h in lista:
        print("Nombre:", h["nombre"])
        print("Categoría:", h["categoria"])
        print("Ingredientes:", ", ".join(h["ingredientes"]))
        print("Precio:", h["precio"])
        print("Chef:", h["chef"])
        print("-" * 30)

def agregar_ambuerguesa():
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    ingredientes = input("Ingredientes separados por coma: ").split(",")
    precio = float(input("Precio: "))
    chef = input("Chef: ")
    lista = cargar_hamburguesas()
    lista.append({
        "nombre": nombre,
        "categoria": categoria,
        "ingredientes": [i.strip() for i in ingredientes],
        "precio": precio,
        "chef": chef
    })
    guardar_hambueguesas(lista)
    print("Hamburguesa agregada.")

def actualizar_hamburguesa():
    nombre = input("Nombre de la hamburguesa: ")
    lista = cargar_hamburguesas()
    for h in lista:
        if h["nombre"].lower() == nombre.lower():
            h["precio"] = float(input("Nuevo precio: "))
            guardar_hambueguesas(lista)
            print("Actualizada.")
            return
    print("No encontrada.")

def eliminar_hamburguesa():
    nombre = input("Nombre a eliminar: ")
    lista = cargar_hamburguesas()
    nueva = [h for h in lista if h["nombre"].lower() != nombre.lower()]
    guardar_hambueguesas(nueva)
    print("Eliminada si existía.")
