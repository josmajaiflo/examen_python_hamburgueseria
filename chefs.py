import json

def cargar_chefs():
    with open("data/chefs.json", "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_chefs(lista):
    with open("data/chefs.json", "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

def mostrar_chefs():
    lista = cargar_chefs()
    for c in lista:
        print("Nombre:", c["nombre"])
        print("Especialidad:", c["especialidad"])
        print("-" * 30)

def agregar_chefs():
    nombre = input("Nombre: ")
    especialidad = input("Especialidad: ")
    lista = cargar_chefs()
    lista.append({"nombre": nombre, "especialidad": especialidad})
    guardar_chefs(lista)
    print("Chef agregado.")

def actualizar_chefs():
    nombre = input("Nombre del chef: ")
    lista = cargar_chefs()
    for c in lista:
        if c["nombre"].lower() == nombre.lower():
            c["especialidad"] = input("Nueva especialidad: ")
            guardar_chefs(lista)
            print("Actualizado.")
            return
    print("No encontrado.")

def eliminar_chefs():
    nombre = input("Nombre a eliminar: ")
    lista = cargar_chefs()
    nueva = [c for c in lista if c["nombre"].lower() != nombre.lower()]
    guardar_chefs(nueva)
    print("Eliminada si existía.")