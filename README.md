# COVID-19 Data Query System for Colombia

Este proyecto es una aplicación en Python que permite consultar datos de COVID-19 de Colombia a través de la API de Datos Abiertos (Socrata). La aplicación filtra los registros por departamento utilizando una consulta SoQL (`$where`) y muestra en pantalla un resumen con las siguientes columnas: Ciudad, Departamento, Edad, Tipo, Estado y País de procedencia.

## Características

- Consulta de datos de COVID-19 utilizando la API de [Datos Abiertos de Colombia](https://dev.socrata.com/foundry/www.datos.gov.co/gt2j-8ykr).
- Filtrado directo por departamento mediante el parámetro `$where`.
- Visualización de resultados en un formato tabular.
- Arquitectura modular dividida en tres módulos:
  - **UI**: Interfaz de usuario para ingreso de datos y presentación de resultados.
  - **API**: Módulo para la interacción con la API y procesamiento de datos.
  - **Main**: Punto de entrada que integra los módulos anteriores.

## Estructura del Proyecto

