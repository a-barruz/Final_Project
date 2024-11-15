import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import json

# Importo libreria para conexión a API
from urllib.request import urlopen

# Definir las variables donde meto el string que contiene la URL

endpoint ='https://sedeaplicaciones.minetur.gob.es'
parametros = '/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'

# Vamos a guardar en una variable nuestros datos 

response = urlopen(endpoint+parametros)

# Vamos a extraer del obejto, los datos 
data = response.read().decode('utf-8', 'replace')
data = json.loads(data)

# Crear Dataframe

df = pd.DataFrame(data)

# Análisis de la columna Lista EESS Precio

diccionario = df['ListaEESSPrecio'].iloc[1]

# Extraigo informacion de columna EESS Precio, utilizando json normalize

df_n = pd.concat([df[['Fecha']],pd.json_normalize(df['ListaEESSPrecio'])], axis=1)

# Convertimos columna categórica a numérica
df_n['Precio Bioetanol']=df_n['Precio Bioetanol'].str.replace(',','.')
df_n[['Precio Bioetanol']]=df_n[['Precio Bioetanol']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica
df_n['Precio Gas Natural Comprimido']=df_n['Precio Gas Natural Comprimido'].str.replace(',','.')
df_n[['Precio Gas Natural Comprimido']]=df_n[['Precio Gas Natural Comprimido']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gas Natural Licuado']=df_n['Precio Gas Natural Licuado'].str.replace(',','.')
df_n[['Precio Gas Natural Licuado']]=df_n[['Precio Gas Natural Licuado']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica
df_n['Precio Gases licuados del petróleo']=df_n['Precio Gases licuados del petróleo'].str.replace(',','.')
df_n[['Precio Gases licuados del petróleo']]=df_n[['Precio Gases licuados del petróleo']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasoleo A']=df_n['Precio Gasoleo A'].str.replace(',','.')
df_n[['Precio Gasoleo A']]=df_n[['Precio Gasoleo A']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasoleo B']=df_n['Precio Gasoleo B'].str.replace(',','.')
df_n[['Precio Gasoleo B']]=df_n[['Precio Gasoleo B']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasoleo Premium']=df_n['Precio Gasoleo Premium'].str.replace(',','.')
df_n[['Precio Gasoleo Premium']]=df_n[['Precio Gasoleo Premium']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasolina 95 E10']=df_n['Precio Gasolina 95 E10'].str.replace(',','.')
df_n[['Precio Gasolina 95 E10']]=df_n[['Precio Gasolina 95 E10']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasolina 95 E5']=df_n['Precio Gasolina 95 E5'].str.replace(',','.')
df_n[['Precio Gasolina 95 E5']]=df_n[['Precio Gasolina 95 E5']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasolina 95 E5 Premium']=df_n['Precio Gasolina 95 E5 Premium'].str.replace(',','.')
df_n[['Precio Gasolina 95 E5 Premium']]=df_n[['Precio Gasolina 95 E5 Premium']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasolina 98 E10']=df_n['Precio Gasolina 98 E10'].str.replace(',','.')
df_n[['Precio Gasolina 98 E10']]=df_n[['Precio Gasolina 98 E10']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasolina 98 E5']=df_n['Precio Gasolina 98 E5'].str.replace(',','.')
df_n[['Precio Gasolina 98 E5']]=df_n[['Precio Gasolina 98 E5']].apply(pd.to_numeric)

# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Hidrogeno']=df_n['Precio Hidrogeno'].str.replace(',','.')
df_n[['Precio Hidrogeno']]=df_n[['Precio Hidrogeno']].apply(pd.to_numeric)

# Eliminiación de columnas que no interesan a nivel usuario o que no aportan datos significativos al modelo
df_n.drop(['Margen', 'Remisión', 'Tipo Venta', '% BioEtanol', '% Éster metílico', 'Precio Biodiesel',
          'Precio Bioetanol', 'Precio Gas Natural Comprimido', 'Precio Gas Natural Licuado', 
          'Precio Gas Natural Licuado', 'Precio Gases licuados del petróleo', 'Precio Gasolina 95 E10',
          'Precio Gasolina 95 E5 Premium', 'Precio Gasolina 98 E10', 'Precio Hidrogeno'], axis=1, inplace=True)

# Renombramos las columnas
df_n.rename(columns={"Precio Gasoleo A": "Gasoleo A", "Precio Gasoleo B": "Gasoleo B" ,"Precio Gasoleo Premium": "Gasoleo Premium", 
                     "Precio Gasolina 95 E5": "Gasolina 95 E5", "Precio Gasolina 98 E5": "Gasolina 98 E5",
                     "Rótulo":"Proveedor de Servicio"}, inplace=True)

# Media Nacional
df_n['Media Nacional Gasoleo A']=df_n['Gasoleo A'].mean()
df_n['Media Nacional Gasoleo B']=df_n['Gasoleo B'].mean()
df_n['Media Nacional Gasoleo P'] = df_n['Gasoleo Premium'].mean()
df_n['Media Nacional Gasolina 95']=df_n['Gasolina 95 E5'].mean()
df_n['Media Nacional Gasolina 98']=df_n['Gasolina 98 E5'].mean()

# Media Código Postal de Gasoleo A
def cp_media_A(x):
# x = Código Postal
    cod_postal = df_n[df_n['C.P.'] == x]
    media_cp_GA = cod_postal[['Gasoleo A']].mean()
    return media_cp_GA

# Media Código Postal de Gasoleo B
def cp_media_B(x):
# x = Código Postal
    cod_postal = df_n[df_n['C.P.'] == x]
    media_cp_GB = cod_postal[['Gasoleo B']].mean()
    return media_cp_GB

# Media Código Postal de Gasoleo Premium
def cp_media_P(x):
# x = Código Postal
    cod_postal = df_n[df_n['C.P.'] == x]
    media_cp_GP = cod_postal[['Gasoleo B']].mean()
    return media_cp_GP

# Media Código Postal de Gasolina 95 E5
def cp_media_95(x):
# x = Código Postal
    cod_postal = df_n[df_n['C.P.'] == x]
    media_cp_G95 = cod_postal[['Gasolina 95 E5']].mean()
    return media_cp_G95

# Media Código Postal de Gasolina 98 E5
def cp_media_98(x):
# x = Código Postal
    cod_postal = df_n[df_n['C.P.'] == x]
    media_cp_G98 = cod_postal[['Gasolina 98 E5']].mean()
    return media_cp_G98

# Aplicamos la función a la columna
df_n[['Media C.P. Gasoleo A']]= df_n['C.P.'].apply(cp_media_A)
df_n[['Media C.P. Gasoleo B']]= df_n['C.P.'].apply(cp_media_B)
df_n[['Media C.P. Gasoleo P']]= df_n['C.P.'].apply(cp_media_P)
df_n[['Media C.P. Gasolina 95']]= df_n['C.P.'].apply(cp_media_95)
df_n[['Media C.P. Gasolina 98']]= df_n['C.P.'].apply(cp_media_98)

#Ordenamos columnas
df_n = df_n[['Fecha', 'Horario', 'C.P.','Provincia','Municipio','Localidad', 'Dirección', 'Proveedor de Servicio', 
             'Gasoleo A', 'Media C.P. Gasoleo A', 'Media Nacional Gasoleo A', 
             'Gasoleo B', 'Media C.P. Gasoleo B','Media Nacional Gasoleo B', 
             'Gasoleo Premium','Media C.P. Gasoleo P', 'Media Nacional Gasoleo P', 
             'Gasolina 95 E5', 'Media C.P. Gasolina 95','Media Nacional Gasolina 95', 
             'Gasolina 98 E5', 'Media C.P. Gasolina 98','Media Nacional Gasolina 98']]

# Misma marca de gasolineras con nombres diferentes
df_n = df_n.sort_values('Proveedor de Servicio')

df_n["Proveedor de Servicio"] = df_n["Proveedor de Servicio"] .astype(str)

df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].astype('string')

# Gasolineras BP
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('.', ' ')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace(',', ' ')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP \S*', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP \S[a-zA-Z0-9_]*', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BPS \S*', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BPS \S[a-zA-Z0-9_]*', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP\w*', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP  ALOD', 'BP') 
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP AVENIDA 3 DE MAYO', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP BENICADELL', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP CA SESTRELLA', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP RAMBLA INIESTA', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP SAN LUIS', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP SANTIGA', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP TACO','BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP VENTA DEL PERAL II', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP ROMICA', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL UBEDA', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('SUTULLENA-CEPSA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('"BP"', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP ROTONDA LAS VAGUADAS S.L.', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BPBEGUR', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BPPROPERLY, S.A.', 'BP')

# Otros
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('SIN RÓTULO', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('(sin rótulo)', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('*', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('-', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('-', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('0', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('06/32718', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('12126', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('12241', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('13344', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('15909', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('1PRIMER', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('23ESO68F', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('395 2/2HS 40-80', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('41037733', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('45110020416', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('4572', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('7267', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('7345', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('96053', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('OTROS \S*', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('OTROS \S[a-zA-Z0-9_]*', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('OTROS \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('OTROSOTROSOTROSOTROSOTROSOTROS', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('OTROS\w*', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('OTROS \S*', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('\S* OTROS ', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('\S*(OTROS)\S*', 'OTROS')

# Gasolineras Varias                                                                          
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('INLOCOR S.L. "CEPSA"', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL. LOS ANGELES DE LA MANCHA, S.L.', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP OIL', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP PARGA I PETROL BAS BEL', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('Nº 7374', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NO', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP CASA JUANITO RESTAURANTE', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NO HAY', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NO TIENE', 'OTROS')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP VILLARROBLEDO', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP ALFAZ DEL PI', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP SANDOVAL MD', 'BP')                                                                        
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP SANDOVAL MI', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP BENIDORM', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP EUROBENIDORM', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP REJAS VERDES', 'BP')

# Gasolineras Cepsa
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA ELF', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA V21', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA LEO', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA TINAJO', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA AGAETE', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA CALONGE', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP REJAS VERDES', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA INGENIO', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA ANTIGUA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA BALOS 1', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA BALOS 2', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROSELF', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA CANONCHE', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA . LOHANA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA EL PEÑON', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA VILANOVAE', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA LA ALDEA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA LA CAÑADA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA TAHICHE I', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA LA MARINA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA RELAMPAGO', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA ALMERIMAR', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROSJUBERA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA EL CUBILLO', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA TAHICHE II', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA MASPALOMAS', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA LA CAZUELA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA ETXEGARATE', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA CAOTROSNCHE', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA AGUA GARCIA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA LOS ANDENES', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA LA AZADILLA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA ', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAI', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAGLTA.EL CID', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAVILAOTROSVA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAESPAÑA S.A.', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAGRAN TARAJAL', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSASIETE PALMAS', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAHOYA PARRADO', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAA4 PINTO 365', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROSALPICAT', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSALLAOTROS AZUL', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSALOS ALMENDROS', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAMUELLE GRANDE', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROSGARCIBUR', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAPUERTO ROSARIO', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSALAS ARENAS 365', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROSE.S. ROCA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROS FIERROIL', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROSE.S.JAIME I', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAPUERTO DE LA CRUZ', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAPLAZA DEL PIOTROS', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROS ANTELA E.S.', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSACOSTA DEL SILENCIO', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOPER CANARIOS S,L.', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSATAXISTAS S.AGUSTIN', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROSARROCEROS B.G.', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROS AGROJARA, SCA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSACOD DE LOS VIOTROSS', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSALAS TORRES (TEXACO)', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOPER CANARIOS S,L.', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROSLA DEHESA S.C.A.', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSALOS PORTALES (TEXACO)', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROS LOS FILABRES SCA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOTROSCOOP. SAN DIONISIO', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSACIUDAD DEL AUTOMÓVIL 365', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSALISBOA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E.S. CEPSACHIO', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSALOS LLAOTROSS OTROS GRANAD', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSALOS LLAOTROSS OTROS GRANADILLA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAVALLECASOTROSLA ATALAYUELA 365', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E.S. CEPSALA CALETA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSALAS TORRES (TEXACO)', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAILLA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOPER CANARIOS S,L.', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSALOS PORTALES (TEXACO)', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA  ', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace(' CEPSA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOPER CANARIOS S,L.', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ES EL CALEYU Nº 229OTROS5CEPSA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E.S.CEPSAPONTEBRANCA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ES VILAMARINACEPSA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('FUNDACION AIDACEPSA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ES MIRALBUEOTROSCEPSA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('EMPRESA DEL GRUPOCEPSA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSAOPER CANARIOS S,L.', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA\w*', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA \S*', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA \S[a-zA-Z0-9_]*', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('CEPSA\S*', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('LOSADACEPSA', 'CEPSA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('EE SS VENTA DEL SOLCEPSA', 'CEPSA')

# BP
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP \w[a-zA-Z0-9_]', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP\w[a-zA-Z0-9_]', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace(' BP', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('B P', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP\S*UXO', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP\w*', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP \S*w*', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BP\S*', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E S GOMEZ \S*BP', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E S ALCARAYON \S*BP', 'BP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('AREA DE SERVICIO A2BP', 'BP')

# Gasolineras Shell
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('SHELL \S*', 'SHELL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('SHELL \S[a-zA-Z0-9_]*', 'SHELL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('SHELL VIOTROSS','SHELL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('SHELL LOS VIOTROSS','SHELL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E.S SHELL','SHELL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E.S SHELL ','SHELL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace( 'E.S. SHELL','SHELL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E.S.SHELL','SHELL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('LUGO SHELL','SHELL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('SHELL.S. BELLVIS' , 'SHELL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('SHELL', 'SHELL')

# Gasolineras Alcampo
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ALCAMPO \S*', 'ALCAMPO')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ALCAMPO \S[a-zA-Z0-9_]*', 'ALCAMPO')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ALCAMPO A', 'ALCAMPO')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('C C ALCAMPO', 'ALCAMPO')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E S ALCAMPO', 'ALCAMPO')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E S  ALCAMPO', 'ALCAMPO')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ALCAMPO ', 'ALCAMPO')

# Gasolineras Repsol
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL \S* \S/()', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL \S*a-zA-Z0-9_*', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E S REPSOL', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E S  REPSOL', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL ', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL65', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOLOMAN', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOLONDA', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOLOMA', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOLTROSRIO SECO', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOLTROSE S JAIME I', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL15/OCTUBRE/2OTROSOTROS7', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOLILA HERMAOTROSS REDONDO S', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ES DULANTZI REPSOL', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('EDAN (REPSOL)', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BALSILLAS I (REPSOL)', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('HIJOS DE NAVARRO ROBLES (REPSOL)', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL L', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL AVENIDA', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL ', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace(' REPSOL', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL5\S*/OCTUBRE\S*/2OTROSOTROS7', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('EDAN \S*(REPSOL)', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('HIJOS DE NAVARRO ROBLES (REPSOL)', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOLADA  AVENIDA', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOLCTUALIZACION A 15/OCTUBR', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('EDAN (REPSOL)', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('BALSILLAS \S*I \S*(REPSOL)', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('HIJOS DE NAVARRO ROBLES \S*(REPSOL)', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL\w*', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL \S*w*', 'REPSOL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('REPSOL\S*', 'REPSOL')

# Gasolineras Disa
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('DISA \S*', 'DISA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('DISA \S[a-zA-Z0-9_]*', 'DISA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('DISA \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'DISA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('DISA         STO DOMINGO', 'DISA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E S DISA', 'DISA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E S  DISA', 'DISA')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('E S  DISA', 'DISA')

# Gasolineras Exoil
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('EXOIL \S*', 'EXOIL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('EXOIL \S[a-zA-Z0-9_]*', 'EXOIL')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('EXOIL \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'EXOIL')

# Gasolineras Energy
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ENERGY \S*', 'ENERGY')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ENERGY \S[a-zA-Z0-9_]*', 'ENERGY')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ENERGY \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'ENERGY')

#Gasolineras Naturgy
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NATURGY ', 'NATURGY')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NATURGY \S*', 'NATURGY')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NATURGY \S[a-zA-Z0-9_]*', 'NATURGY')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NATURGY \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'NATURGY')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ESNATURGY \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'NATURGY')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NATURGYES \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'NATURGY')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NATURGY\w*', 'NATURGY')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NATURGY \S*w*', 'NATURGY')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('NATURGYES \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'NATURGY')

# Gasolineras Galp
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP \S*', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP \S[a-zA-Z0-9_]*', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP\w*', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP \S*w*', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP \S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*\S[a-zA-Z0-9_]*', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP ', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP&GO', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALPENERGIA', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALPARRIONDAS', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP(E S  ANTUNEZ)', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALPOTROS3 CAMIOTROSS', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALPOTROS AMERICAN PETROL', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP/3CAMIOTROSSOTROSVALENCIA', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALPDISTRIBUCION OIL ESPAÑA  S A U ', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALP', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALPLA JUNQUERA', 'GALP')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('GALPOTROS3CAMIOTROSS UTIEL', 'GALP')

# ES CARBURANTES
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('\S* S\*ES \S*CABURANTES', 'ES CARBURANTES')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ES CARBURANTES', 'ES CARBURANTES')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('ES CARBURANTES CENTRO COMERCIAL VISTALEGRE', 'ES CARBURANTES')
df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].str.replace('\S*[+]B ENERGIAS ', '+B ENERGIAS')
df_n['Proveedor de Servicio'] 

# Guardamos df original para sucesion de tiempo
#df_n.to_csv('df_sample.csv', index=False)


header = st.container()
dataset = st.container()
interaccion_usuario = st.container()
graficos = st.container()
    
    
with header:

    image = Image.open('logo.png')

    st.image(image, caption='Encuentra tu Gasolinera con el combustible más económico ')

    


with dataset:
    
    #gasolineras = pd.read_csv("./df_sample.csv", dtype={"C.P.":str})
    gasolineras = df_n
    #st.text(pd.DataFrame(gasolineras))
    #gasolineras['Gasoleo B'] = gasolineras['Gasoleo B'].replace(np.nan, "Sin servicio")
    #f['DataFrame Column'] = df['DataFrame Column'].replace(np.nan, 0)
  
with interaccion_usuario:

    st.header('GASOLINERAS EN ESPAÑA')

    gasolineras = pd.DataFrame(gasolineras)
    

    # Radio Buttons   
    
    st.sidebar.header("ENCUENTRA LA GASOLINERA MÁS BARATA FILTRANDO POR:")
    
    pages_names = ['Código Postal', 'Provincia', 'Municipio', 'Localidad', 'Proveedor de Servicio', 'Calculadora por kilómetros']

    page = st.sidebar.radio(' ', pages_names)

    

# Slicing for Códgigo Postal
try:   
    if page == 'Código Postal':
        
        # Filtro Código Postal
        filtro_cp = gasolineras["C.P."].astype(str).unique()
        
        filtro_combustible_cp = ['Gasoleo A', 'Gasoleo B','Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']

        # Sidebar Código Postal
        caja_cp = st.sidebar.selectbox("Seleccione Código Postal", filtro_cp)
        combustible_cp = st.sidebar.selectbox("Seleccione tipo de combustible", filtro_combustible_cp)
        def p_minimo(caja_cp, combustible_cp):
            cp = gasolineras[(gasolineras["C.P."] == caja_cp)]
            filtro_df_n_2= cp.loc[cp[[combustible_cp]].idxmin()]
            return(filtro_df_n_2)


     
        if st.sidebar.button('Buscar'):
            st.write(p_minimo(caja_cp, combustible_cp))
            
      
            st.subheader('Comparación por tipo de combustible respecto a la Media por Código Postal y Nacional')

            def mean_CP(combustible_cp):
                if combustible_cp == 'Gasoleo A':
                    var = 'Media C.P. Gasoleo A'        
                if  combustible_cp == 'Gasoleo B':
                    var = 'Media C.P. Gasoleo B'      
                if combustible_cp == 'Gasoleo Premium':
                    var = 'Media C.P. Gasoleo P'
                if combustible_cp == 'Gasolina 95 E5':
                    var = 'Media C.P. Gasolina 95'
                if combustible_cp == 'Gasolina 98 E5':
                    var = 'Media C.P. Gasolina 98'             
                return var

            def mean_Nacional(combustible_cp):
                if combustible_cp == 'Gasoleo A':
                    var ='Media Nacional Gasoleo A'        
                if combustible_cp == 'Gasoleo B':
                    var = 'Media Nacional Gasoleo B'        
                if combustible_cp == 'Gasoleo Premium':
                    var = 'Media Nacional Gasoleo P'
                if combustible_cp == 'Gasolina 95 E5':
                    var = 'Media Nacional Gasolina 95'
                if combustible_cp == 'Gasolina 98 E5':
                    var = 'Media Nacional Gasolina 98'              
                return var

            
            graphic = pd.DataFrame(p_minimo(caja_cp, combustible_cp), columns=[combustible_cp, mean_CP(combustible_cp), mean_Nacional(combustible_cp)]).T
            st.bar_chart(graphic)

        
            if st.sidebar.button('Limpiar'):
                st.write(gasolineras)
        else:
            st.write(gasolineras)

            caja_general = st.checkbox('Todas las Gasolineras por Municipio')
            if caja_general:        
                filtro_municipio = gasolineras["Municipio"].unique()
                caja_municipio=st.selectbox('Filtro por Municipio', filtro_municipio)
                def cp_minimo(caja_municipio):
                    municipio = gasolineras[(gasolineras["Municipio"] == caja_municipio)]
                    return municipio 
                
                st.write(cp_minimo(caja_municipio))
except:
    st.error('No hay suministro para el combustible seleccionado', icon="🚨")
    
    peligro = Image.open('sin_combustible.png')
    st.image(peligro)


     # Slicing for Provincia

try:      
    if page == 'Provincia':
    
        #Filtros para operaciones en cajas
        filter_oil_prov = ['Gasoleo A', 'Gasoleo B','Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        filter_oil_mun = gasolineras["Provincia"].unique()
    
        # Cajas Sidebar
        box_mun = st.sidebar.selectbox("Seleccione Provincia", filter_oil_mun)
        oil_prov = st.sidebar.selectbox("Seleccione tipo de combustible", filter_oil_prov)

        def provincia_min(box_prov, oil_prov):
            prov = gasolineras[(gasolineras["Provincia"] == box_prov)]
            filtro_df_n_2= prov.loc[prov[[oil_prov]].idxmin()]
            return(filtro_df_n_2) 

    

        if st.sidebar.button('Buscar'):
            st.write(provincia_min(box_mun, oil_prov))
        
            st.subheader('Comparación por tipo de combustible respecto a la Media por Código Postal y Nacional')

            def mean_CP(oil_prov):
                if oil_prov == 'Gasoleo A':
                    var = 'Media C.P. Gasoleo A'        
                if oil_prov == 'Gasoleo B':
                    var = 'Media C.P. Gasoleo B'      
                if oil_prov == 'Gasoleo Premium':
                    var = 'Media C.P. Gasoleo P'
                if oil_prov == 'Gasolina 95 E5':
                    var = 'Media C.P. Gasolina 95'
                if oil_prov == 'Gasolina 98 E5':
                    var = 'Media C.P. Gasolina 98'             
                return var

            def mean(oil_prov):
                if oil_prov == 'Gasoleo A':
                    var ='Media Nacional Gasoleo A'        
                if oil_prov == 'Gasoleo B':
                    var = 'Media Nacional Gasoleo B'        
                if oil_prov == 'Gasoleo Premium':
                    var = 'Media Nacional Gasoleo P'
                if oil_prov == 'Gasolina 95 E5':
                    var = 'Media Nacional Gasolina 95'
                if oil_prov == 'Gasolina 98 E5':
                    var = 'Media Nacional Gasolina 98'
                return var
                
            graphic = pd.DataFrame(provincia_min(box_mun, oil_prov), columns=[oil_prov, mean_CP(oil_prov), mean(oil_prov)]).T
            st.bar_chart(graphic)
    
            if st.sidebar.button('Limpiar'):
                st.write(gasolineras)

        else:
            st.write(gasolineras)
        
            caja_general = st.checkbox('Todas las Gasolineras por Municipio')
            if caja_general:        
                filtro_municipio = gasolineras["Municipio"].unique()
                caja_municipio=st.selectbox('Filtro por Municipio', filtro_municipio)
                def cp_minimo(caja_municipio):
                    municipio = gasolineras[(gasolineras["Municipio"] == caja_municipio)]
                    return municipio 
                
                st.write(cp_minimo(caja_municipio))

except:
    st.error('No hay suministro para el combustible seleccionado', icon="🚨")
    
    peligro = Image.open('sin_combustible.png')
    st.image(peligro)        



# Slicing for Municipio
try:   
    if page == 'Municipio':
    
        #Filtros para operaciones en cajas
        filtro_combustible = ['Gasoleo A', 'Gasoleo B','Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        filtro_municipio = gasolineras["Municipio"].unique()
    
        # Cajas Sidebar
        caja_municipio = st.sidebar.selectbox("Seleccione Municipio", filtro_municipio)
        combustible = st.sidebar.selectbox("Seleccione tipo de combustible", filtro_combustible)

        def cp_minimo(caja_municipio, combustible):
            municipio = gasolineras[(gasolineras["Municipio"] == caja_municipio)]
            filtro_df_n_2= municipio.loc[municipio[[combustible]].idxmin()]
            return(filtro_df_n_2) 

    

        if st.sidebar.button('Buscar'):
            st.write(cp_minimo(caja_municipio, combustible))
        
            st.subheader('Comparación por tipo de combustible respecto a la Media por Código Postal y Nacional')

            def mean_CP(combustible):
                if combustible == 'Gasoleo A':
                    var = 'Media C.P. Gasoleo A'        
                if combustible == 'Gasoleo B':
                    var = 'Media C.P. Gasoleo B'      
                if combustible == 'Gasoleo Premium':
                    var = 'Media C.P. Gasoleo P'
                if combustible == 'Gasolina 95 E5':
                    var = 'Media C.P. Gasolina 95'
                if combustible == 'Gasolina 98 E5':
                    var = 'Media C.P. Gasolina 98'             
                return var

            def mean(combustible):
                if combustible == 'Gasoleo A':
                    var ='Media Nacional Gasoleo A'        
                if combustible == 'Gasoleo B':
                    var = 'Media Nacional Gasoleo B'        
                if combustible == 'Gasoleo Premium':
                    var = 'Media Nacional Gasoleo P'
                if combustible == 'Gasolina 95 E5':
                    var = 'Media Nacional Gasolina 95'
                if combustible == 'Gasolina 98 E5':
                    var = 'Media Nacional Gasolina 98'
                return var

            graphic = pd.DataFrame(cp_minimo(caja_municipio, combustible), columns=[combustible, mean_CP(combustible), mean(combustible)]).T
            st.bar_chart(graphic)
    
            if st.sidebar.button('Limpiar'):
                st.write(gasolineras)


                
        else:
            st.write(gasolineras)
        
            caja_general = st.checkbox('Todas las Gasolineras por Municipio')
            if caja_general:        
                filtro_municipio = gasolineras["Municipio"].unique()
                caja_municipio=st.selectbox('Filtro por Municipio', filtro_municipio)
                def cp_minimo(caja_municipio):
                    municipio = gasolineras[(gasolineras["Municipio"] == caja_municipio)]
                    return municipio 
                
                st.write(cp_minimo(caja_municipio))
except:
    st.error('No hay suministro para el combustible seleccionado', icon="🚨")
    
    peligro = Image.open('sin_combustible.png')
    st.image(peligro)
      



 # Slicing for 'Localidad':
    
try:    
    if page == 'Localidad':
    
        #Filtros para operaciones en cajas
        filter_oil_proveedor = ['Gasoleo A', 'Gasoleo B','Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        filter_proveedor = gasolineras["Localidad"].unique()
    
        # Cajas Sidebar
        box_proveedor = st.sidebar.selectbox("Seleccione Localidad", filter_proveedor)
        oil_proveedor = st.sidebar.selectbox("Seleccione tipo de combustible", filter_oil_proveedor)

        def proveedor_min(box_proveedor, oil_proveedor):
            proveedor = gasolineras[(gasolineras["Localidad"] == box_proveedor)]
            filtro_df_n_2= proveedor.loc[proveedor[[oil_proveedor]].idxmin()]
            return(filtro_df_n_2) 

    

        if st.sidebar.button('Buscar'):
            st.write(proveedor_min(box_proveedor, oil_proveedor))
        
            st.subheader('Comparación por tipo de combustible respecto a la Media por Código Postal y Nacional')

            def mean_CP(oil_proveedor):
                if oil_proveedor == 'Gasoleo A':
                    var = 'Media C.P. Gasoleo A'        
                if oil_proveedor == 'Gasoleo B':
                    var = 'Media C.P. Gasoleo B'      
                if oil_proveedor == 'Gasoleo Premium':
                    var = 'Media C.P. Gasoleo P'
                if oil_proveedor == 'Gasolina 95 E5':
                    var = 'Media C.P. Gasolina 95'
                if oil_proveedor == 'Gasolina 98 E5':
                    var = 'Media C.P. Gasolina 98'             
                return var

            def mean(oil_proveedor):
                if oil_proveedor == 'Gasoleo A':
                    var ='Media Nacional Gasoleo A'        
                if oil_proveedor == 'Gasoleo B':
                    var = 'Media Nacional Gasoleo B'        
                if oil_proveedor == 'Gasoleo Premium':
                    var = 'Media Nacional Gasoleo P'
                if oil_proveedor == 'Gasolina 95 E5':
                    var = 'Media Nacional Gasolina 95'
                if oil_proveedor == 'Gasolina 98 E5':
                    var = 'Media Nacional Gasolina 98'
                return var
                
            graphic = pd.DataFrame(proveedor_min(box_proveedor, oil_proveedor), columns=[oil_proveedor, mean_CP(oil_proveedor), mean(oil_proveedor)]).T
            st.bar_chart(graphic)
    
            if st.sidebar.button('Limpiar'):
                st.write(gasolineras)
                
      
        else:
            st.write(gasolineras)
            
            caja_general = st.checkbox('Todas las Gasolineras por Municipio')
            if caja_general:        
                filtro_municipio = gasolineras["Municipio"].unique()
                caja_municipio=st.selectbox('Filtro por Municipio', filtro_municipio)
                def cp_minimo(caja_municipio):
                    municipio = gasolineras[(gasolineras["Municipio"] == caja_municipio)]
                    return municipio 
                
                st.write(cp_minimo(caja_municipio))

except:
    st.error('No hay suministro para el combustible seleccionado', icon="🚨")
    
    peligro = Image.open('sin_combustible.png')
    st.image(peligro)        

# Estaciones de servicio más baratas

try:    
    if page == 'Proveedor de Servicio':

        filtro_combustible_p = ['Gasoleo A', 'Gasoleo B','Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        filtro_Proveedor = gasolineras["Proveedor de Servicio"].astype(str).unique()
        
        
    
        # Cajas Sidebar
        caja_Proveedor = st.sidebar.selectbox("Seleccione Proveedor de Servicio", filtro_Proveedor)
    
        proveedor_ES = gasolineras[(gasolineras["Proveedor de Servicio"] == caja_Proveedor)]
        
        agree = st.sidebar.checkbox('Precio mas bajo para estación de servicio')
        
        if agree:
            oil_proveedor = st.sidebar.selectbox("Seleccione tipo de combustible", filtro_combustible_p) 

        if st.sidebar.button('Buscar'):
            st.write(proveedor_ES)
            
            if st.sidebar.button('Limpiar'):
                st.write(gasolineras)

    
            if agree: 
                st.subheader('Estación de Servicio mas barata para los filtros seleccionados') 
                df_pov_ES = proveedor_ES.loc[proveedor_ES[[oil_proveedor]].idxmin()]
                st.write (df_pov_ES)
            
            
       
        else:
            st.write(gasolineras)
            
            caja_general = st.checkbox('Todas las Gasolineras por Municipio')
            if caja_general:        
                filtro_municipio = gasolineras["Municipio"].unique()
                caja_municipio=st.selectbox('Filtro por Municipio', filtro_municipio)
                def cp_minimo(caja_municipio):
                    municipio = gasolineras[(gasolineras["Municipio"] == caja_municipio)]
                    return municipio 
                
                st.write(cp_minimo(caja_municipio))
        
        
    
except:
    st.error('No hay suministro para el combustible seleccionado', icon="🚨")
    
    peligro = Image.open('sin_combustible.png')
    st.image(peligro)
    
             
   

  # Calculadora por kilómetros

try:    
    if page == 'Calculadora por kilómetros': 

    

        filtro_combustible_p = ['Gasoleo A', 'Gasoleo B','Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        kilometros = st.number_input('str')
        consumo_a_los_100=st.number_input('str')
        calculo_litros_consumo = (kilometros * consumo_a_los_100)/100
        gasto_combustible = calculo_litros_consumo * filtro_combustible_p

except:
    st.error('No hay suministro para el combustible seleccionado', icon="🚨")
    
    peligro = Image.open('sin_combustible.png')
    st.image(peligro)



















        

