# Examen_Python

Sistema de gestión para una hamburguesería usando Python y JSON. realizado con operaciones CRUD sobre ingredientes, categorías, chefs y hamburguesas. Además, incluye reportes.
## 🧠 Módulos del sistema

# `main.py`
Archivo principal. Ejecuta el menú general llamando a `menu.py`.

# `menu.py`
Contiene el menú general del sistema y submenús para:
- Ingredientes
- Categorías
- Chefs
- Hamburguesas
- Reportes

# `ingredientes.py`
Gestión de ingredientes:
- Ver ingredientes
- Agregar nuevo ingrediente
- Actualizar precio y stock
- Eliminar ingrediente

# `categorias.py`
Gestión de categorías:
- Ver, agregar, actualizar y eliminar categorías

# `chefs.py`
Gestión de chefs:
- Ver, agregar, actualizar y eliminar chefs

# `hamburguesas.py`
Gestión de hamburguesas:
- Ver hamburguesas
- Agregar nueva hamburguesa (nombre, categoría, ingredientes, precio, chef)
- Actualizar precio
- Eliminar hamburguesa

# `reportes.py`
Consultas especiales solicitadas en el examen, por ejemplo:
- Ingredientes con stock menor a 400
- Hamburguesas vegetarianas
- Chefs con especialidad en carnes
- Aumento de precio de ingredientes
- Hamburguesas hechas por "ChefB"

#  Estructura de carpetas

Examen_Python_ApellidoNombre/
│
├── main.py
├── menu.py
├── ingredientes.py
├── categorias.py
├── chefs.py
├── hamburguesas.py
├── reportes.py
├── README.md
│
└── data/
├── ingredientes.json
├── categorias.json
├── chefs.json
└── hamburguesas.json