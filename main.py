import sys
import time
import networkx as nx
import matplotlib.pyplot as plt
import random

def generar_grafo_aleatorio(num_vertices, archivo_salida, probabilidad_conexion=0.2):
    G = nx.gnp_random_graph(num_vertices, probabilidad_conexion, directed=True)

    with open(archivo_salida, 'w') as file:
        for edge in G.edges():
            file.write(f"{edge[0]}\t{edge[1]}\n")

def dibujar_grafo_con_cubrimiento(archivo, vertices_cubrimiento):
    # Crear un grafo dirigido desde el archivo
    G = nx.read_edgelist(archivo, delimiter='\t', nodetype=int)
    
    # Crear un conjunto de nodos para los vértices de cubrimiento
    nodos_cubrimiento = set(vertices_cubrimiento)
    
    # Configurar el diseño del grafo
    pos = nx.spring_layout(G)
    
    # Dibujar el grafo
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='gray')

    # Resaltar los nodos de cubrimiento en otro color
    nx.draw_networkx_nodes(G, pos, nodelist=nodos_cubrimiento, node_color='salmon')
    
    # Mostrar el grafo
    plt.show()

def cubrimiento_vertices(archivo):
    vertices_cubrimiento = set()
    
    with open(archivo, 'r') as file:
        # Leer las líneas del archivo
        lines = file.readlines()
        
        # Crear un conjunto de ejes
        ejes = set()
        for line in lines:
            v1, v2 = map(int, line.strip().split('\t'))
            ejes.add((v1, v2))
        
    while ejes:
        # Escoger arbitrariamente un eje
        v1, v2 = ejes.pop()
        
        # Incluir los dos vértices conectados en el conjunto de cubrimiento
        vertices_cubrimiento.add(v1)
        vertices_cubrimiento.add(v2)
        
        # Descartar todos los demás ejes conectados por los vértices escogidos
        ejes = {(x, y) for x, y in ejes if x != v1 and x != v2 and y != v1 and y != v2}
    
    return vertices_cubrimiento

def cubrimiento_vertices_grado(archivo):
    G = nx.read_edgelist(archivo, delimiter='\t', nodetype=int)
    vertices_cubrimiento = set()

    while G.edges():
        # Escoger arbitrariamente un eje
        eje = list(G.edges())[0]
        
        # Obtener los vértices conectados por el eje
        v1, v2 = eje
        
        # Obtener el vértice de mayor grado de los dos vértices conectados
        vertice_max_grado = v1 if G.degree(v1) > G.degree(v2) else v2
        
        # Incluir el vértice de mayor grado en el conjunto de cubrimiento
        vertices_cubrimiento.add(vertice_max_grado)
        
        # Descartar todos los demás ejes conectados por el vértice escogido
        G.remove_edges_from(list(G.edges(vertice_max_grado)))
    
    return vertices_cubrimiento

def cubrimiento_algo2(archivo):
    G = nx.read_edgelist(archivo, delimiter='\t', nodetype=int)
    vertices_cubrimiento = []
    while len(G.edges())>0:
        max_grado = 0
        vertice_max_grado = 0
        for v in G.nodes():
            if G.degree(v) > max_grado:
                max_grado = G.degree(v)
                vertice_max_grado = v
        vertices_cubrimiento.append(vertice_max_grado)
        G.remove_edges_from(list(G.edges(vertice_max_grado)))
    return vertices_cubrimiento

def main_algo1():
    archivo = ""
    num = int(input("Subio un archivo del grafo (1) o desea generar un grafo (2): "))
    if num == 1:
      archivo = sys.argv[1]
    elif num == 2:
      num_vertices = int(input("Defina el maximo de nodos que quiera para generar el grafo: ")) # 5
      archivo = 'data/grafo_aleatorio_'+str(num_vertices)+'.txt'
      generar_grafo_aleatorio(num_vertices, archivo) 
      print("Grafo aleatorio generado")

    try:
        start_time = time.time()
        vertices_cubrimiento = cubrimiento_vertices(archivo)
        end_time = time.time()
        tiempo_ejecucion = end_time - start_time
    
        print(f"\nArchivo: {archivo}")
        print(f"Vertices del cubrimiento: {vertices_cubrimiento}")
        print(f"Tamaño del conjunto de vértices: {len(vertices_cubrimiento)}")
        print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
        
        dibujar_grafo_con_cubrimiento(archivo, vertices_cubrimiento)
    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error:", e)

def main_algo2():
    archivo = ""
    num = int(input("Subio un archivo del grafo (1) o desea generar un grafo (2): "))
    if num == 1:
      archivo = sys.argv[1]
    elif num == 2:
      num_vertices = int(input("Defina el maximo de nodos que quiera para generar el grafo: ")) # 5
      archivo = 'data/grafo_aleatorio_'+str(num_vertices)+'.txt'
      generar_grafo_aleatorio(num_vertices, archivo) 

    #algorithm
    try:
        start_time = time.time()
        vertices_cubrimiento = cubrimiento_algo2(archivo)
        end_time = time.time()
        tiempo_ejecucion = end_time - start_time

        print(f"\nArchivo: {archivo}")
        print(f"Vertices del cubrimiento: {vertices_cubrimiento}")
        print(f"Tamaño del conjunto de vértices: {len(vertices_cubrimiento)}")
        print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error:", e)

def main_algo3():
    archivo = ""
    num = int(input("Subio un archivo del grafo (1) o desea generar un grafo (2): "))
    if num == 1:
      archivo = sys.argv[1]
    elif num == 2:
      num_vertices = int(input("Defina el maximo de nodos que quiera para generar el grafo: ")) # 5
      archivo = 'data/grafo_aleatorio_'+str(num_vertices)+'.txt'
      generar_grafo_aleatorio(num_vertices, archivo) 
      print("Grafo aleatorio generado")

    try:
        start_time = time.time()
        vertices_cubrimiento = cubrimiento_vertices_grado(archivo)
        end_time = time.time()
        tiempo_ejecucion = end_time - start_time
    
        print(f"\nArchivo: {archivo}")
        print(f"Vertices del cubrimiento: {vertices_cubrimiento}")
        print(f"Tamaño del conjunto de vértices: {len(vertices_cubrimiento)}")
        print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
        
        dibujar_grafo_con_cubrimiento(archivo, vertices_cubrimiento)
    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error:", e)
    

if __name__ == "__main__":
    algo = int(input("Desea ejecutar el algoritmo 1 (1), el algoritmo (2), el algoritmo 3 (3) o el algoritmo 4 (4): "))
    if algo == 1:
        print("Algoritmo 1")
        main_algo1()
    if algo == 2:
        print("Algoritmo 2")
        main_algo2()
    if algo == 3:
        print("Algoritmo 3")
        main_algo3()
    if algo == 4:
        print("Algoritmo 4")
        # main_algo4()
    
