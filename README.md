# Tarea 6 Algoritmos

## Descripción

En este proyecto se implementaran uno programa que resuelva el problema de cubrimiento de vértices implementando 4 algoritmos. El programa debe recibir un archivo de texto con los ejes del grafo y un número que indique el algoritmo a ejecutar. Cada linea del archivo debe contener una pareja de números que representan los dos vértices conectados, separados por tab. Los programas no pueden hacer ninguna suposición acerca del sistema operativo o del sistema de archivos del usuario. Los programas deben imprimir los vertices del cubrimiento encontrado y el tamaño del conjunto de vértices. Realizar pruebas con diferentes tipos de grafos de 100, 1000 y 10000 vértices. Calcular una tabla con los tamaños de las soluciones encontradas y los tiempos de ejecución de todos los experimentos.

## Instalación

Asegúrate de tener Python instalado en tu sistema. Luego, puedes instalar las dependencias utilizando el siguiente comando:

```bash
pip install matplotlib numpy networkx scipy
```

## Descripcion de los enunciados

### Punto 1:

Escoger arbitrariamente un eje, incluir los dos vértices conectados, descartar todos los demás ejes conectados por los vertices escogidos y repetir hasta que no queden ejes.

### Punto 2:
Escoger el vértice de mayor grado, descartar los ejes que llegan al vertice escogido y repetir hasta que no queden ejes.

### Punto 3:
Escoger arbitrariamente un eje, incluir el vértice de mayor grado de los dos vértices conectados por el eje, descartar todos los demás ejes conectados por el vértice escogido y repetir hasta que no queden ejes.

### Punto 4:
Escoger aleatoriamente un eje, incluir aleatoriamente uno de los dos vértices conectados, descartar todos los demás ejes conectados por el vértice escogido y repetir hasta que no queden ejes.

## Uso

Para cada uno de los algoritmos se debe correr de la misma manera seleccionando las diferentes opciones. Primero se corre el archivo de la siguiente manera en consola:
```bash
python "$Path_archivo_python/main.py" "$Path_archivo_datos"
```
Aqui, una vez se corra, va a salir como input lo siguiente, donde debe ser seleccionado el algoritmo que se desee:

```bash
Desea ejecutar el algoritmo 1 (1), el algoritmo (2), el algoritmo 3 (3) o el algoritmo 4 (4): 3
```

Posteriormente, se mostrara el titulo del algoritmo escogido y se procedera a preguntar si se desea correr con un archivo predeterminado o generar un grafo aleatorio:

```bash
Algoritmo 3
Subio un archivo del grafo (1) o desea generar un grafo (2): 1
```

Finalmente el resultado sera el sigueinte:

```bash
Archivo: "$Path_archivo_datos"
Vertices del cubrimiento: {4, 5, 6, 7, 8}
Tamaño del conjunto de vértices: 5
Tiempo de ejecución: 0.001294851303100586 segundos
```

Adicionalmente muestra el grafo generado, con sus vertices de recubrimiento marcados:
![Figure1](https://github.com/larodriguez22/Tarea6_algoritmos/blob/main/data/Figure1.png)
