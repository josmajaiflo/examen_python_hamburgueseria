import json

def cargar_reportes(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def ingredientes_bajo_stock():
    datos = cargar_reportes("data/ingredientes.json")
    for i in datos:
        if i["stock"] < 400:
            print(i["nombre"], "-", i["stock"])

def hamburguesas_vegetarianas():
    datos = cargar_reportes("data/hamburguesas.json")
    for h in datos:
        if h["categoria"].lower() == "vegetariana":
            print(h["nombre"])

def chefs_carnes():
    datos = cargar_reportes("data/chefs.json")
    for c in datos:
        if c["especialidad"].lower() == "carnes":
            print(c["nombre"])

def aumentar_precios_ingredientes():
    datos = cargar_reportes("data/ingredientes.json")
    for i in datos:
        i["precio"] *= 1.5
    with open("data/ingredientes.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print("Precios aumentados.")

def hamburguesas_por_chef(chef):
    datos = cargar_reportes("data/hamburguesas.json")
    for h in datos:
        if h["chef"].lower() == chef.lower():
            print(h["nombre"])