# Gabriel Estuardo García Donis 21352
# Laboratorio 8

import time
import cProfile

def function(n):
    # cont = 0
    for i in range(1, n // 3 + 1):
        for j in range(1, n + 1, 4):
            print("Sequence")
            # cont += 1
            # print("Esta en: " + n)
            # print("Contador 1: " + cont)

# Tamaños de entrada n
input_sizes = [1, 10, 100, 1000, 5000]
 
# Medir el tiempo de ejecución y el perfil del código para cada tamaño de entrada
execution_times = []
for n in input_sizes:
    print(f"Comienza n = {n}")
    profiler = cProfile.Profile()
    profiler.enable()
    start_time = time.time()
    function(n)
    end_time = time.time()
    profiler.disable()
    print(f"Termina n = {n}")
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    print(f"Tiempo de {n} fue: {execution_time:.10f} segundos")
    profiler.print_stats(sort='cumulative')

# Imprimir los tiempos de ejecución
for i in range(len(input_sizes)):
    print(f"El tiempo de {input_sizes[i]} fue: {execution_times[i]:.10f} segundos")

# Graficar tamaño de entrada vs. tiempo de ejecución
import matplotlib.pyplot as plt

# Graficar tamaño de entrada vs. tiempo de ejecución
plt.plot(input_sizes, execution_times, marker='o')
plt.title('Tamaño de entrada vs. Tiempo de ejecución')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.grid(True)
plt.show()

