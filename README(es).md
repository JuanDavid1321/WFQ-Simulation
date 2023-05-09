[Readme in English](README.md)

# Simulación Agendador de paquetes WFQ
Este repositorio contiene una simulación de Weighted Fair Queuing (WFQ) implementada en Python. WFQ es un algoritmo de planificación de colas utilizado en enrutadores y conmutadores para asignar ancho de banda a diferentes flujos de tráfico de red en función de sus pesos asignados.

## Descripción del código
El código simula el proceso de WFQ en cuatro componentes principales:

* Generación de paquetes: Genera paquetes de forma aleatoria para simular el tráfico de red. Los paquetes tienen características como dirección de origen y destino, tamaño y tipo de tráfico.

* Clasificación de paquetes: Clasifica los paquetes en varias colas según sus pesos asignados. Cada cola tiene una prioridad relativa basada en su peso.

* Envío de paquetes: Envía los paquetes clasificados según un algoritmo de envío específico. El orden y la cantidad de paquetes enviados de cada cola pueden variar según la implementación.

* Recepción y ordenamiento de paquetes: Simula la recepción de paquetes y los ordena en función de algún criterio, como la prioridad de la cola o el tiempo de llegada.

El código se ejecuta a partir de la función simular_wfq(num_paquetes), donde num_paquetes es la cantidad de paquetes a generar y simular.

## Requisitos
El código requiere Python 3 y las siguiente biblioteca:

* random: Utilizada para generar números aleatorios.
## Uso
* Clona el repositorio o descarga los archivos en tu sistema local.

* Asegúrate de tener Python 3 instalado en tu sistema.

* Abre una terminal o línea de comandos y navega hasta el directorio del repositorio.

* Ejecuta el siguiente comando para iniciar la simulación:
```
python app.py
```
* Ingresa el número de paquetes que deseas generar cuando se te solicite.

* Observa la salida que muestra la recepción de paquetes.

## Contribución
Este proyecto ha sido desarrollado como parte de un curso académico y no aceptamos contribuciones externas. Sin embargo, si encuentra algún error o problema en la aplicación, puede informarlo a través de los issues en este repositorio.
