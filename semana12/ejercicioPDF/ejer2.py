grafo = {
    "Rock": ["Maneskin", "Queen", "Deftones"]
}

# Mostrar el grafo de manera textual
for genero, artistas in grafo.items():
    print(f"Género: {genero}")
    for artista in artistas:
        print(f"  Artista: {artista}")