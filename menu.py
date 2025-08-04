import ingredientes
import categorias
import chefs
import hamburguesas
import reportes

def menu_ingredientes():
    while True:
        print("\n--- INGREDIENTES ---")
        print("1. Ver")
        print("2. Agregar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        op = input("Opción: ")
        if op == "1":
            ingredientes.mostrar_ingredientes()
        elif op == "2":
            ingredientes.agregar_ingrediente()
        elif op == "3":
            ingredientes.actualizar_ingrediente()
        elif op == "4":
            ingredientes.eliminar_ingrediente()
        elif op == "5":
            break

def menu_categorias():
    while True:
        print("\n--- CATEGORÍAS ---")
        print("1. Ver")
        print("2. Agregar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        op = input("Opción: ")
        if op == "1":
            categorias.mostrar()
        elif op == "2":
            categorias.agregar()
        elif op == "3":
            categorias.actualizar()
        elif op == "4":
            categorias.eliminar()
        elif op == "5":
            break


def menu_chefs():
    while True:
        print("\n--- CHEFS ---")
        print("1. Ver")
        print("2. Agregar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        op = input("Opción: ")
        if op == "1":
            chefs.mostrar()
        elif op == "2":
            chefs.agregar()
        elif op == "3":
            chefs.actualizar()
        elif op == "4":
            chefs.eliminar()
        elif op == "5":
            break

def menu_hamburguesas():
    while True:
        print("\n--- HAMBURGUESAS ---")
        print("1. Ver")
        print("2. Agregar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        op = input("Opción: ")
        if op == "1":
            hamburguesas.mostrar()
        elif op == "2":
            hamburguesas.agregar()
        elif op == "3":
            hamburguesas.actualizar()
        elif op == "4":
            hamburguesas.eliminar()
        elif op == "5":
            break

def menu_reportes():
    while True:
        print("\n--- REPORTES ---")
        print("1. Ingredientes con stock < 400")
        print("2. Hamburguesas vegetarianas")
        print("3. Chefs especialistas en carnes")
        print("4. Aumentar precios ingredientes (x1.5)")
        print("5. Hamburguesas por ChefB")
        print("6. Volver")
        op = input("Opción: ")
        if op == "1":
            reportes.ingredientes_bajo_stock()
        elif op == "2":
            reportes.hamburguesas_vegetarianas()
        elif op == "3":
            reportes.chefs_carnes()
        elif op == "4":
            reportes.aumentar_precios_ingredientes()
        elif op == "5":
            reportes.hamburguesas_por_chef("ChefB")
        elif op == "6":
            break

def menu_principal():
    while True:
        print("\n====== MENÚ PRINCIPAL ======")
        print("1. ingredientes")
        print("2. categorías")
        print("3. chefs")
        print("4. hamburguesas")
        print("5. reportes")
        print("6. salir")
        op = input("Selecciona opción: ")
        if op == "1":
            menu_ingredientes()
        elif op == "2":
            menu_categorias()
        elif op == "3":
            menu_chefs()
        elif op == "4":
            menu_hamburguesas()
        elif op == "5":
            menu_reportes()
        elif op == "6":
            print("¡Chao!")
            break