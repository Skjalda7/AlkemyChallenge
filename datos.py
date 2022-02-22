import pandas as pd
import requests
import os
from datetime import date
import numpy as np

### Establecer la URL de descarga de los csv con fecha actualizada

hoooy=date.today()
dia=hoooy.day
mes=hoooy.month
anio=hoooy.year
meses_nom = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
meses_num = np.arange(1,13)
meses_d=dict(zip(meses_num,meses_nom))

def nombre(mes):
    for key, value in meses_d.items():
         if mes == key:
             return value
este_mes=nombre(mes)

os.makedirs(f'museos\{anio}-{este_mes}', exist_ok=True)
os.makedirs(f'salas_de_cine\{anio}-{este_mes}', exist_ok=True)
os.makedirs(f'bibliotecas\{anio}-{este_mes}', exist_ok=True)

### Descargar los .csv

url1 = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv'
r_museos = requests.get(url1)
open(f'museos\{anio}-{este_mes}\museos-{dia}-{mes}-{anio}.csv', 'wb').write(r_museos.content)
museum = pd.read_csv(f'museos\{anio}-{este_mes}\museos-{dia}-{mes}-{anio}.csv')
url2 = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
r_salas = requests.get(url2)
open(f'salas_de_cine\{anio}-{este_mes}\salas_de_cine-{dia}-{mes}-{anio}.csv', 'wb').write(r_salas.content)
cinema = pd.read_csv(f'salas_de_cine\{anio}-{este_mes}\salas_de_cine-{dia}-{mes}-{anio}.csv')
url3 = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
r_bibl = requests.get(url3)
open(f'bibliotecas\{anio}-{este_mes}\ bibliotecas-{dia}-{mes}-{anio}.csv', 'wb').write(r_bibl.content)
library = pd.read_csv(f'bibliotecas\{anio}-{este_mes}\ bibliotecas-{dia}-{mes}-{anio}.csv')

### Actualizar reemplazando el archivo .csv si ya fue descargado ese mismo día

if os.path.isfile('museos-{dia}-{mes}-{anio}.csv') == True:
    remove('museos-{dia}-{mes}-{anio}.csv')
if os.path.isfile('salas_de_cine-{dia}-{mes}-{anio}.csv') == True:
    remove('salas_de_cine-{dia}-{mes}-{anio}.csv')
if os.path.isfile(' bibliotecas-{dia}-{mes}-{anio}.csv') == True:
    remove(' bibliotecas-{dia}-{mes}-{anio}.csv')








##### DATAFRAME MUSEOS NORMALIZADO #####

# Dejar solo las columnas que piden
tabla1_museo=museum.drop(['Observaciones', 'categoria', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'fuente', 'jurisdiccion', 'año_inauguracion', 'IDSInCA'], axis='columns')

# Reemplazar los NaN por ' '
museo_nan=tabla1_museo.replace([np.nan], ' ')

# Cambio el tipo de datos de las columnas 'cod_area' y 'telefono', de ¿FLOAT? a STR para poder combinarlas con el JOIN
museo_nan[['cod_area', 'telefono']]=museo_nan[['cod_area', 'telefono']].astype(str)

# Crear columna 'tel' juntando 'cod_area' y 'telefono'
museo_nan.insert(2, 'tel', museo_nan[['cod_area','telefono']].apply(' '.join, axis=1))
museooo=museo_nan.drop(['cod_area','telefono'], axis=1)

# Crear columna 'domicilio' juntando 'direccion' y 'piso'
museooo.insert(3, 'domicilio', museooo[['direccion','piso']].apply(' '.join, axis=1))
museo_12=museooo.drop(['direccion','piso'], axis=1)

# Renombrar las columnas
museo_12.columns=['cod_localidad', 'id_provincia', 'numero_de_telefono', 'domicilio', 'id_departamento', 'categoria', 'provincia', 'localidad', 'nombre', 'codigo_postal', 'mail', 'web']

# Reorganizar columnas
museo_12=museo_12[['cod_localidad', 'id_provincia', 'id_departamento', 'categoria', 'provincia', 'localidad', 'nombre', 'domicilio', 'codigo_postal', 'numero_de_telefono', 'mail', 'web']]









##### DATAFRAME BIBLIOTECAS NORMALIZADO #####

# Dejar solo las columnas que piden
tabla1_bibl=library.drop(['Observacion','Subcategoria','Departamento','Información adicional','Latitud','Longitud','TipoLatitudLongitud','Fuente','Tipo_gestion','año_inicio','Año_actualizacion'], axis='columns')

# Reemplazar TODOS los 's/d' del dataframe por espacios en blanco, y crear la columna 'domicilio' juntando 'Domicilio' y 'Piso'
bibl_nan=tabla1_bibl.replace(['s/d', np.nan], ' ')
bibl_nan.insert(7, 'domicilio', bibl_nan[['Domicilio','Piso']].apply(' '.join, axis=1))
bibl_domicilio=bibl_nan.drop(['Domicilio','Piso'], axis=1)

bibl_domicilio.insert(9, 'telefono', bibl_nan[['Cod_tel','Teléfono']].apply(' '.join, axis=1))
bibl_12=bibl_domicilio.drop(['Cod_tel','Teléfono'], axis=1)

bibl_12.columns = ['cod_localidad', 'id_provincia', 'id_departamento', 'categoria', 'provincia', 'localidad', 'nombre', 'domicilio', 'codigo_postal', 'numero_de_telefono', 'mail', 'web']












##### DATAFRAME SALAS DE CINE NORMALIZADO #####

# Dejar solo las columnas que piden
tabla1_cine=cinema.drop(['Observaciones','Departamento','Información adicional','Latitud','Longitud','TipoLatitudLongitud','Fuente','tipo_gestion','Pantallas','Butacas','espacio_INCAA','año_actualizacion'], axis='columns')

# Reemplazar TODOS los 's/d' del dataframe por espacios en blanco, y crear la columna 'domicilio' juntando 'Dirección' y 'Piso'
cine_nan=tabla1_cine.replace(['s/d'], ' ')
cine_nan.insert(7, 'domicilio', cine_nan[['Dirección','Piso']].apply(' '.join, axis=1))
cine_domicilio=cine_nan.drop(['Dirección','Piso'], axis=1)

# Crear columna 'telefono' juntando 'cod_area' y 'Teléfono'
cine_domicilio.insert(9, 'telefono', cine_nan[['cod_area','Teléfono']].apply(' '.join, axis=1))
cine_12=cine_domicilio.drop(['cod_area','Teléfono'], axis=1)

#Finalmente, renombrar las columnas
cine_12.columns = ['cod_localidad', 'id_provincia', 'id_departamento', 'categoria', 'provincia', 'localidad', 'nombre', 'domicilio', 'codigo_postal', 'numero_de_telefono', 'mail', 'web']









##### DATAFRAME SALAS DE CINE pero con 4 columnitas #####

cin=cinema.loc[:,['Provincia','Pantallas','Butacas','espacio_INCAA']]
cin.columns=['provincia','cantidad_de_pantallas','cantidad_de_butacas','cantidad_de_espacios_INCAA']









########### UNIR LOS 3 DF ##############
datos=pd.concat([bibl_12, cine_12, museo_12], axis=0)










##### DATAFRAME DE REGISTROS #####
# Cantidad de registros totales por categoría
# Cantidad de registros totales por fuente
# Cantidad de registros por provincia y categoría

registro = datos[['categoria', 'web']]
registro.insert(2, 'provincia_y_categoria', datos[['provincia','categoria']].apply(' '.join, axis=1))
registro.columns=['categoria', 'fuente', 'provincia_y_categoria']