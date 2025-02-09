# Casos de Dengue en el Perú en niños menores de 13 años en GeoJson

Este repositorio contiene un proyecto de Jupyter Notebook que procesa datos oficiales de casos de dengue en Perú, específicamente enfocado en niños menores de 13 años, y los convierte en un archivo GeoJson para su uso en aplicaciones de mapas.

## 🚀 Descripción del Proyecto

El proyecto utiliza datos abiertos del gobierno peruano ([datosabiertos.gob.pe](https://www.datosabiertos.gob.pe/dataset/vigilancia-epidemiol%C3%B3gica-de-dengue)) que contienen información sobre casos de dengue desde el año 2000 hasta 2023. El objetivo principal es limpiar, filtrar y transformar estos datos para obtener un conjunto de datos específico que pueda ser utilizado en una aplicación de mapas.

### Pasos del Proceso

1. **Limpieza y Filtrado de Datos**:
   - Se filtran los datos para incluir solo los casos de los años 2021, 2022 y 2023.
   - Se convierten todas las edades a años y se filtran los casos de niños menores de 13 años.
   - Se categorizan las edades en:
     - **Menor a 1 año**: Bebé
     - **Menor a 5 años**: Pequeño
     - **Entre 5 y 12 años**: Mayor

2. **Obtención de Coordenadas Geográficas**:
   - Se utiliza el archivo de coordenadas geográficas de los distritos de Perú ([opendatasoft](https://data.opendatasoft.com/explore/dataset/distritos-peru%40bogota-laburbano/export/)) que contiene la latitud y longitud de cada distrito basado en su UBIGEO.
   - Se realiza un `merge` entre el dataframe filtrado de casos de dengue y el dataframe de coordenadas para obtener la ubicación geográfica de cada caso.

3. **Generación del Archivo GeoJson**:
   - Se filtran las columnas necesarias y se guarda el resultado en un archivo CSV.
   - Este CSV se convierte a formato GeoJson dentro del proyecto de Jupyter Notebook.

4. **Uso del GeoJson en una Aplicación de Mapas**:
   - El archivo GeoJson generado se utiliza en una aplicación de React con Mapbox para visualizar un mapa de calor de los casos de dengue en Perú.

## 📂 Estructura del Proyecto  
```plaintext
📦 Casos-Dengue-Peru  
├── data/ # Carpeta que contiene los datos originales y procesados
│ ├── dengue_data.csv # Datos originales de casos de dengue
│ ├── distritos_peru.csv # Datos de coordenadas de distritos de Perú
│ └── dengue_ninos.json # Archivo CSV generado
│ └── dengue_geojson.json # Archivo GeoJson generado
├── dengue_data.ipynb # Notebook principal de procesamiento de datos
├── README.md # Este archivo
└── requirements.txt # Dependencias necesarias para ejecutar el proyecto
└── utils.py # Archivo con funciones.
```

## 📊 Fuentes de Datos  
- **Casos de Dengue (2000 - 2023)**: Datos oficiales del portal de datos abiertos del Gobierno del Perú  
  - [Vigilancia Epidemiológica del Dengue](https://www.datosabiertos.gob.pe/dataset/vigilancia-epidemiol%C3%B3gica-de-dengue)  
- **Coordenadas Geográficas (UBIGEO)**: Datos abiertos de OpenDataSoft  
  - [Distritos de Perú](https://data.opendatasoft.com/explore/dataset/distritos-peru%40bogota-laburbano/export)  

## 🔍 Requisitos

Para ejecutar el proyecto, necesitas tener instalado:

- Python 3.x
- Jupyter Notebook
- Librerías de Python: `pandas`, `geojson`

Puedes instalar las dependencias necesarias ejecutando:
```bash
pip install -r requirements.txt
```
## 📚 Licencia
Este proyecto está bajo la licencia MIT.