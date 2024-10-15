grafo = {
    "Lácteos": ["Crema", "Leche", "Queso"],
    "Boquitas Diana": ["Churro", "Ceresita", "Quesito"],
    "Higiene personal": ["Jabón", "Pasta de dientes", "Enjuague bucal"]
}

for categoria, productos in grafo.items():
    print(f"Categoría: {categoria}")
    for producto in productos:
        print(f"  Producto: {producto}")

categorias = list(grafo.keys())
productos = [producto for sublist in grafo.values() for producto in sublist]

print("\nTabla de adyacencia:")
for categoria in categorias:
    conexiones = [1 if producto in grafo[categoria] else 0 for producto in productos]
    print(f"{categoria.ljust(15)}: {conexiones}")