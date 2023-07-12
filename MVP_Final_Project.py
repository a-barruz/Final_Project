#!/usr/bin/env python
# coding: utf-8

# ## MVP (Cheapest Oil)

# In[1]:


# Imports

# Pandas
import pandas as pd 

# Importo libreria para conexión a API
from urllib.request import urlopen

# Importo libreria Json para que lea
import json

# Numpy
import numpy as np


# ---
# Step 1 (Data Extraction)

# In[2]:


# Definir las variables donde meto el string que contiene la URL

endpoint ='https://sedeaplicaciones.minetur.gob.es'
parametros = '/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'


# In[3]:


# Vamos a guardar en una variable nuestros datos 

response = urlopen(endpoint+parametros)
type(response)
response


# In[4]:


# Vamos a extraer del obejto, los datos 

data = response.read().decode('utf-8', 'replace')
data = json.loads(data)
type(data)
data


# In[5]:


# Crear Dataframe

df = pd.DataFrame(data)
df


# ---
# 
# Step 2 (Data Transformation)

# In[6]:


# Análisis de la columna Lista EESS Precio

diccionario = df['ListaEESSPrecio'].iloc[1]
type(diccionario)


# In[7]:


diccionario


# In[8]:


# Extraigo informacion de columna EESS Precio, utilizando json normalize

df_n = pd.concat([df[['Fecha']],pd.json_normalize(df['ListaEESSPrecio'])], axis=1)
df_n


# In[9]:


# Guardamos df original para sucesion de tiempo
#df_n.to_csv('2022-11-05x.csv', index=False)


# In[10]:


df_n.info()


# ---
# Step (3): EDA

#                                                     Análisis de Columnas

# # Fecha

# In[11]:


# Fecha (solo hay una fecha)
Fecha = df_n['Fecha'].unique()
print(type(Fecha))
print(len(Fecha))
Fecha


# In[12]:


# Nulos 
nulos_f = df_n['Fecha'].isnull().sum()
nulos_f


# # Código Postal

# In[13]:


# Columna C.P.
cp = df_n['C.P.'].unique()
print(type(cp))
print(len(cp))
cp
# En Esaña hay 11752 codigos postales en total


# In[14]:


# Nulos 
nulos_cp = df_n['C.P.'].isnull().sum()
nulos_cp


# # Dirección

# In[15]:


# Columna  Dirección
direccion = df_n['Dirección'].unique()
print(type(direccion))
print(len(direccion))
direccion


# In[16]:


# Nulos dirección
nulos_cp = df_n['Dirección'].isnull().sum()
nulos_cp


# # Horario

# In[17]:


# Horario
horario = df_n['Horario'].unique()
horario


# In[18]:


# Nulos horario
nulos_h = df_n['Horario'].isnull().sum()
nulos_h


# # Latitud

# In[19]:


#Latitud (Coincide Latitud y Longitud con las coordenadas en las gasolineras de Google Maps)
latitud = df_n['Latitud'].unique()
print(len(latitud ))
latitud


# In[20]:


# Nulos Latitud
nulos_l = df_n['Latitud'].isnull().sum()
nulos_l


# # Longitud

# In[21]:


# Longitud (Coincide Latitud y Longitud con las coordenadas en las gasolineras de Google Maps)
Longitud = df_n['Longitud (WGS84)'].unique()
print(len(Longitud))
Longitud


# In[22]:


# Nulos Longitud
nulos_long = df_n['Longitud (WGS84)'].isnull().sum()
nulos_long


# # Localidad

# In[23]:


#Localidad
Localidad = df_n['Localidad'].unique()
print(len(Localidad))
Localidad


# In[24]:


# Nulos Localidad
nulos_loc = df_n['Localidad'].isnull().sum()
nulos_loc


# # Municipio 

# In[25]:


# Municipio (En España hay 8131 Municipios)
Municipio = df_n['Municipio'].unique() 
print(len(Municipio))
Municipio



# In[26]:


# Nulos Municipio
nulos_loc = df_n['Municipio'].isnull().sum()
nulos_loc


# # Margen

# In[27]:


# Margen
Margen = df_n['Margen'].unique()
print(len(Margen))
Margen


# # Provincia 

# In[28]:


# Provincia (Están todas las Provinicas de España en nuestro df)
Provincia = df_n['Provincia'].unique()
print(len(Provincia))
Provincia


# In[29]:


# Nulos Provincia
nulos_prov = df_n['Provincia'].isnull().sum()
nulos_prov


# # Remision

# In[30]:


# Remisión (Sistema de envío de información de precios y de ventas a través de API)
Remision = df_n['Remisión'].unique()
print(len(Remision))
print(type(Remision))
Remision


# # Rótulo

# In[31]:


# Rótulo (En España hay 3952 marcas de Gasolineras en España según datos de Google)
Rotulo = df_n['Rótulo'].unique()
print(len(Rotulo))
print(type(Rotulo))
Rotulo


# # Tipo de Venta

# In[32]:


# Tipo Venta
tv = df_n['Tipo Venta'].unique()
print(len(tv))
print(type(tv))
tv


# # Porcentaje de Bioetanol

# In[33]:


# % BioEtanol (La diferencia entre gasolinas E5 o E10 significan el porcentaje de Etanol (5 o 10%))
bioetanol = df_n['% BioEtanol'].unique()
print(len(bioetanol))
print(type(bioetanol))
bioetanol


# # Porcentaje de Éster Metílico

# In[34]:


# % Éster metílico (solo para Biodiesel)
em = df_n['% Éster metílico'].unique()
print(len(em))
print(type(em))
em


# #  IDEESS

# In[35]:


# IDEESS (ID Estación de Servicio, los mismos que estaciones (filas))
IDEESS = df_n['IDEESS'].unique()
print(len(IDEESS))
type(IDEESS)
IDEESS 


# In[36]:


# Nulos IDEESS
nulos_IDEESS = df_n['IDEESS'].isnull().sum()
nulos_IDEESS


# # ID Municipio

# In[37]:


# IDMunicipio (un ID más que municipios)
idmun = df_n['IDMunicipio'].unique()
print(len(idmun))
type(idmun)
idmun


# In[38]:


# Nulos ID Municipio
nulos_IDMunicipio = df_n['IDMunicipio'].isnull().sum()
nulos_IDMunicipio


# # ID Provincia

# In[39]:


# IDProvincia (Los mismos ID que Provincias)
idprov = df_n['IDProvincia'].unique()
print(len(idprov))
type(idprov)
idprov


# In[40]:


nulos_IDProvincia = df_n['IDProvincia'].isnull().sum()
nulos_IDProvincia


# # ID CCAA

# In[41]:


# IDCCAA (ID Comunidades Autónomas, 17 CCAA + Ceuta + Melilla)
# IDProvincia (Los mismos ID que Provincias)
idccaa = df_n['IDCCAA'].unique()
print(len(idccaa))
type(idccaa)
idccaa


#                                                 Columnas Numéricas
#                                                 

# # Biodiesel

# In[42]:


Biodiesel = df_n['Precio Biodiesel'].unique()
print(len(Biodiesel))
print(type(Biodiesel))
Biodiesel


# In[43]:


# Convertimos columna categórica a numérica
df_n['Precio Biodiesel']=df_n['Precio Biodiesel'].str.replace(',','.')
df_n[['Precio Biodiesel']]=df_n[['Precio Biodiesel']].apply(pd.to_numeric)


# In[44]:


df_n['Precio Biodiesel'].describe()


# In[45]:


# Registros sin venta Biodiesel
sin_suministro_b = df_n['Precio Biodiesel'].isnull().sum()
sin_suministro_b


# ## Precio Bioetanol 

# In[46]:


Bioetanol = df_n['Precio Bioetanol'].unique()
print(len(Bioetanol))
print(type(Bioetanol))
Bioetanol


# In[47]:


# Convertimos columna categórica a numérica
df_n['Precio Bioetanol']=df_n['Precio Bioetanol'].str.replace(',','.')
df_n[['Precio Bioetanol']]=df_n[['Precio Bioetanol']].apply(pd.to_numeric)


# In[48]:


df_n['Precio Bioetanol'].describe()


# In[49]:


# Registros sin venta Biodiesel
sin_suministro_be = df_n['Precio Bioetanol'].isnull().sum()
sin_suministro_be


# ## Precio Gas Natural Comprimido

# In[50]:


Gas_n_c = df_n['Precio Gas Natural Comprimido'].unique()
print(len(Gas_n_c))
print(type(Gas_n_c))
Gas_n_c


# In[51]:


# Convertimos columna categórica a numérica
df_n['Precio Gas Natural Comprimido']=df_n['Precio Gas Natural Comprimido'].str.replace(',','.')
df_n[['Precio Gas Natural Comprimido']]=df_n[['Precio Gas Natural Comprimido']].apply(pd.to_numeric)


# In[52]:


df_n['Precio Gas Natural Comprimido'].describe()


# In[53]:


# Registros sin venta Biodiesel
sin_suministro_be = df_n['Precio Bioetanol'].isnull().sum()
sin_suministro_be


# # Precio Gas Natural Licuado

# In[54]:


Gas_nat_lic = df_n['Precio Gas Natural Licuado'].unique()
print(len(Gas_nat_lic))
print(type(Gas_nat_lic))
Gas_nat_lic


# In[55]:


# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gas Natural Licuado']=df_n['Precio Gas Natural Licuado'].str.replace(',','.')
df_n[['Precio Gas Natural Licuado']]=df_n[['Precio Gas Natural Licuado']].apply(pd.to_numeric)


# In[56]:


df_n['Precio Gas Natural Licuado'].describe()


# In[57]:


# Registros sin venta Gas NAtural Licuado
sin_suministro_gnl = df_n['Precio Gas Natural Licuado'].isnull().sum()
sin_suministro_gnl


# # Precio Gases licuados del petróleo

# In[58]:


Gas_nat_lic_pet = df_n['Precio Gases licuados del petróleo'].unique()
print(len(Gas_nat_lic_pet))
print(type(Gas_nat_lic_pet))
Gas_nat_lic_pet


# In[59]:


# Convertimos columna categórica a numérica
df_n['Precio Gases licuados del petróleo']=df_n['Precio Gases licuados del petróleo'].str.replace(',','.')
df_n[['Precio Gases licuados del petróleo']]=df_n[['Precio Gases licuados del petróleo']].apply(pd.to_numeric)


# In[60]:


df_n['Precio Gases licuados del petróleo'].describe()


# In[61]:


# Registros sin venta Gas NAtural Licuado del Petróleo
sin_suministro_gnlp = df_n['Precio Gases licuados del petróleo'].isnull().sum()
sin_suministro_gnlp


# In[62]:


ceros_sin_suministro_gnlp = (df_n['Precio Gases licuados del petróleo'] == 0).sum()
ceros_sin_suministro_gnlp


# # Gasoleo A

# In[63]:


Gasoleo_A = df_n['Precio Gasoleo A'].unique()
print(len(Gasoleo_A))
print(type(Gasoleo_A))
Gasoleo_A


# In[64]:


# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasoleo A']=df_n['Precio Gasoleo A'].str.replace(',','.')
df_n[['Precio Gasoleo A']]=df_n[['Precio Gasoleo A']].apply(pd.to_numeric)


# In[65]:


df_n['Precio Gasoleo A'].describe()


# In[66]:


# Registros sin venta Gasoleo A
sin_suministro_gA = df_n['Precio Gasoleo A'].isnull().sum()
sin_suministro_gA


# In[67]:


ceros_sin_suministro_gA = (df_n['Precio Gasoleo A'] == 0).sum()
ceros_sin_suministro_gA


# # Gasoleo B

# In[68]:


Gasoleo_B = df_n['Precio Gasoleo B'].unique()
print(len(Gasoleo_A))
print(type(Gasoleo_A))
Gasoleo_B


# In[69]:


# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasoleo B']=df_n['Precio Gasoleo B'].str.replace(',','.')
df_n[['Precio Gasoleo B']]=df_n[['Precio Gasoleo B']].apply(pd.to_numeric)


# In[70]:


# Registros sin venta Gasoleo B
sin_suministro_gB = df_n['Precio Gasoleo B'].isnull().sum()
sin_suministro_gB


# In[71]:


ceros_sin_suministro_gB = (df_n['Precio Gasoleo B'] == 0).sum()
ceros_sin_suministro_gB


# # Precio Gasoleo Premium 

# In[72]:


Gasoleo_P = df_n['Precio Gasoleo Premium'].unique()
print(len(Gasoleo_P))
print(type(Gasoleo_P))
Gasoleo_P


# In[73]:


# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasoleo Premium']=df_n['Precio Gasoleo Premium'].str.replace(',','.')
df_n[['Precio Gasoleo Premium']]=df_n[['Precio Gasoleo Premium']].apply(pd.to_numeric)


# In[74]:


df_n['Precio Gasoleo Premium'].describe()


# In[75]:


# Registros sin venta Gasoleo Premium
sin_suministro_gP = df_n['Precio Gasoleo Premium'].isnull().sum()
sin_suministro_gP


# In[76]:


ceros_sin_suministro_gP = (df_n['Precio Gasoleo Premium'] == 0).sum()
ceros_sin_suministro_gP


# # Precio Gasolina 95 E10 

# In[77]:


g95_E10 = df_n['Precio Gasolina 95 E10'].unique()
print(len(g95_E10))
print(type(g95_E10))
g95_E10


# In[78]:


# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasolina 95 E10']=df_n['Precio Gasolina 95 E10'].str.replace(',','.')
df_n[['Precio Gasolina 95 E10']]=df_n[['Precio Gasolina 95 E10']].apply(pd.to_numeric)


# In[79]:


df_n['Precio Gasolina 95 E10'].describe()


# In[80]:


# Registros sin venta Gasoleo Premium
sin_suministro_95E10 = df_n['Precio Gasolina 95 E10'].isnull().sum()
sin_suministro_95E10


# # Precio Gasolina 95 E5

# In[81]:


g95_E5 = df_n['Precio Gasolina 95 E5'].unique()
print(len(g95_E5))
print(type(g95_E5))
g95_E5


# In[82]:


# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasolina 95 E5']=df_n['Precio Gasolina 95 E5'].str.replace(',','.')
df_n[['Precio Gasolina 95 E5']]=df_n[['Precio Gasolina 95 E5']].apply(pd.to_numeric)


# In[83]:


df_n['Precio Gasolina 95 E5'].describe()


# In[84]:


# Registros sin venta Gasoleo Premium
sin_suministro_g95E5 = df_n['Precio Gasolina 95 E5'].isnull().sum()
sin_suministro_g95E5


# In[85]:


ceros_sin_suministro_g95E5  = (df_n['Precio Gasolina 95 E5'] == 0).sum()
ceros_sin_suministro_g95E5 


# # Precio Gasolina 95 E5 Premium

# In[86]:


g95_E5_P = df_n['Precio Gasolina 95 E5 Premium'].unique()
print(len(g95_E5_P))
print(type(g95_E5_P))
g95_E5_P


# In[87]:


# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasolina 95 E5 Premium']=df_n['Precio Gasolina 95 E5 Premium'].str.replace(',','.')
df_n[['Precio Gasolina 95 E5 Premium']]=df_n[['Precio Gasolina 95 E5 Premium']].apply(pd.to_numeric)


# In[88]:


df_n['Precio Gasolina 95 E5 Premium'].describe()


# In[89]:


# Registros sin venta Gasolina 95 E5 Premium
sin_suministro_g95E5_Prem = df_n['Precio Gasolina 95 E5 Premium'].isnull().sum()
sin_suministro_g95E5_Prem


# In[90]:


ceros_sin_suministro_g95E5_Prem  = (df_n['Precio Gasolina 95 E5 Premium'] == 0).sum()
ceros_sin_suministro_g95E5 


# # Precio Gasolina 98 E10

# In[91]:


g98_E10 = df_n['Precio Gasolina 98 E10'].unique()
print(len(g98_E10))
print(type(g98_E10))
g98_E10


# In[92]:


# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasolina 98 E10']=df_n['Precio Gasolina 98 E10'].str.replace(',','.')
df_n[['Precio Gasolina 98 E10']]=df_n[['Precio Gasolina 98 E10']].apply(pd.to_numeric)


# In[93]:


df_n['Precio Gasolina 98 E10'].describe()


# In[94]:


# Registros sin venta Gasolina 98 E10 
sin_suministro_g98E10 = df_n['Precio Gasolina 98 E10'].isnull().sum()
sin_suministro_g98E10


# # Precio Gasolina 98 E5

# In[95]:


g98_E5 = df_n['Precio Gasolina 98 E5'].unique()
print(len(g98_E5))
print(type(g98_E5))
g98_E5


# In[96]:


# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Gasolina 98 E5']=df_n['Precio Gasolina 98 E5'].str.replace(',','.')
df_n[['Precio Gasolina 98 E5']]=df_n[['Precio Gasolina 98 E5']].apply(pd.to_numeric)


# In[97]:


df_n['Precio Gasolina 98 E5'].describe()


# In[98]:


# Registros sin venta Gasolina 98 E5 
sin_suministro_g98E5 = df_n['Precio Gasolina 98 E5'].isnull().sum()
sin_suministro_g98E5


# In[99]:


ceros_sin_suministro_g98E5  = (df_n['Precio Gasolina 98 E5'] == 0).sum()
ceros_sin_suministro_g98E5 


# # Precio Hidrogeno 

# In[100]:


Hidrongeno = df_n['Precio Hidrogeno'].unique()
print(len(Hidrongeno))
print(type(Hidrongeno))
Hidrongeno


# In[101]:


# Convertimos columna categórica a numérica, primero tenemos que sustituir , por .
df_n['Precio Hidrogeno']=df_n['Precio Hidrogeno'].str.replace(',','.')
df_n[['Precio Hidrogeno']]=df_n[['Precio Hidrogeno']].apply(pd.to_numeric)


# In[102]:


df_n['Precio Hidrogeno'].describe()


# In[103]:


df_n.info()


# ---
# Setp 3
# 
# # Limpieza de Columnas

# In[104]:


# Eliminiación de columnas que no interesan a nivel usuario o que no aportan datos significativos al modelo
df_n.drop(['Margen', 'Remisión', 'Tipo Venta', '% BioEtanol', '% Éster metílico', 'Precio Biodiesel',
          'Precio Bioetanol', 'Precio Gas Natural Comprimido', 'Precio Gas Natural Licuado', 
          'Precio Gas Natural Licuado', 'Precio Gases licuados del petróleo', 'Precio Gasolina 95 E10',
          'Precio Gasolina 95 E5 Premium', 'Precio Gasolina 98 E10', 'Precio Hidrogeno'], axis=1, inplace=True)


# In[105]:


# Comprobación
df_n.iloc[15][['Precio Gasoleo B']]


# In[106]:


df_n.head()


# In[107]:


# Renombramos las columnas
df_n.rename(columns={"Precio Gasoleo A": "Gasoleo A", "Precio Gasoleo B": "Gasoleo B" ,"Precio Gasoleo Premium": "Gasoleo Premium", 
                     "Precio Gasolina 95 E5": "Gasolina 95 E5", "Precio Gasolina 98 E5": "Gasolina 98 E5",
                     "Rótulo":"Proveedor de Servicio"}, inplace=True)
df_n.head(1)


# In[108]:


# Media Nacional
df_n['Media Nacional Gasoleo A']=df_n['Gasoleo A'].mean()
df_n['Media Nacional Gasoleo B']=df_n['Gasoleo B'].mean()
df_n['Media Nacional Gasoleo P'] = df_n['Gasoleo Premium'].mean()
df_n['Media Nacional Gasolina 95']=df_n['Gasolina 95 E5'].mean()
df_n['Media Nacional Gasolina 98']=df_n['Gasolina 98 E5'].mean()


# # Media de precios respecto al código postal

# In[109]:


# Media Código Postal de Gasoleo A
def cp_media_A(x):
# x = Código Postal
    cod_postal = df_n[df_n['C.P.'] == x]
    media_cp_GA = cod_postal[['Gasoleo A']].mean()
    return media_cp_GA


# In[110]:


# Media Código Postal de Gasoleo B
def cp_media_B(x):
# x = Código Postal
    cod_postal = df_n[df_n['C.P.'] == x]
    media_cp_GB = cod_postal[['Gasoleo B']].mean()
    return media_cp_GB


# In[111]:


# Media Código Postal de Gasoleo Premium
def cp_media_P(x):
# x = Código Postal
    cod_postal = df_n[df_n['C.P.'] == x]
    media_cp_GP = cod_postal[['Gasoleo B']].mean()
    return media_cp_GP


# In[112]:


# Media Código Postal de Gasolina 95 E5
def cp_media_95(x):
# x = Código Postal
    cod_postal = df_n[df_n['C.P.'] == x]
    media_cp_G95 = cod_postal[['Gasolina 95 E5']].mean()
    return media_cp_G95


# In[113]:


# Media Código Postal de Gasolina 98 E5
def cp_media_98(x):
# x = Código Postal
    cod_postal = df_n[df_n['C.P.'] == x]
    media_cp_G98 = cod_postal[['Gasolina 98 E5']].mean()
    return media_cp_G98


# In[114]:


# Comprobación
cp_media_95('28760')


# In[115]:


# Aplicamos la función a la columna
df_n[['Media C.P. Gasoleo A']]= df_n['C.P.'].apply(cp_media_A)
df_n[['Media C.P. Gasoleo B']]= df_n['C.P.'].apply(cp_media_B)
df_n[['Media C.P. Gasoleo P']]= df_n['C.P.'].apply(cp_media_P)
df_n[['Media C.P. Gasolina 95']]= df_n['C.P.'].apply(cp_media_95)
df_n[['Media C.P. Gasolina 98']]= df_n['C.P.'].apply(cp_media_98)


# In[116]:


df_n.head()


# In[117]:


df_n.info()


# In[118]:


#Ordenamos columnas
df_n = df_n[['Fecha', 'Horario', 'C.P.','Provincia','Municipio','Localidad', 'Dirección', 'Proveedor de Servicio', 
             'Gasoleo A', 'Media C.P. Gasoleo A', 'Media Nacional Gasoleo A', 
             'Gasoleo B', 'Media C.P. Gasoleo B','Media Nacional Gasoleo B', 
             'Gasoleo Premium','Media C.P. Gasoleo P', 'Media Nacional Gasoleo P', 
             'Gasolina 95 E5', 'Media C.P. Gasolina 95','Media Nacional Gasolina 95', 
             'Gasolina 98 E5', 'Media C.P. Gasolina 98','Media Nacional Gasolina 98']]
df_n


# # Limpieza de Nombres en "Proveedores de servicio"

# In[119]:


# Misma marca de gasolineras con nombres diferentes
df_n = df_n.sort_values('Proveedor de Servicio')





# In[120]:


df_n["Proveedor de Servicio"] = df_n["Proveedor de Servicio"] .astype(str)


# In[121]:


df_n.info()


# In[122]:


df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].astype('string')


# In[123]:


df_n.info()


# In[128]:


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


# In[129]:


df_n['Proveedor de Servicio'].iloc[5700]


# # Dataframe Final de Gasolineras

# In[130]:


# Guardamos df original para sucesion de tiempo
df_n.to_csv('df_sample.csv', index=False)


# In[131]:


df_n.info()


# In[ ]:




