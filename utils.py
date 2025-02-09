import pandas as pd

def convertir_a_anios(row):
    if row["tipo_edad"] == "A":
        return row["edad"] #Mantener la edad
    elif row["tipo_edad"] == "M":
        return row["edad"] / 12 # Convertir meses a años
    elif row["tipo_edad"] == "D":
        return row["edad"] / 365 # Convertir días a años
    else:
        return None

def clasificar_grupo_edad(edad):
    if edad < 1:
        return "bebe"
    elif edad < 5:
        return "pequeño"
    elif edad < 13:
        return "mayor"

import pandas as pd
import geojson as gj
import json

def csv_a_geojson(csv_file, geojson_file, lat_col="latitud", lon_col="longitud"):
    #Leer archivo csv
    df = pd.read_csv(csv_file)
    #Crear un diccionario con la información del archivo csv
    features = []
    for _, row in df.iterrows():
        feature = gj.Feature(
            geometry=gj.Point((row[lon_col], row[lat_col])),
            properties=row.drop([lat_col, lon_col]).to_dict()
        )
        features.append(feature)
    #Crear el objeto GeoJson
    feature_collection = gj.FeatureCollection(features)
    #Escribir el archivo geojson
    with open(geojson_file, "w", encoding="utf-8") as f:
        json.dump(feature_collection, f, ensure_ascii=False, indent=4, allow_nan=False)