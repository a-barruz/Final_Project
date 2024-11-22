import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import json
from urllib.request import urlopen

# Definir las variables donde meto el string que contiene la URL
endpoint = 'https://sedeaplicaciones.minetur.gob.es'
parametros = '/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'

# Función para cargar y procesar los datos
@st.cache_data
def load_data():
    response = urlopen(endpoint + parametros)
    data = response.read().decode('utf-8', 'replace')
    data = json.loads(data)
    df = pd.DataFrame(data)
    df_n = pd.concat([df[['Fecha']], pd.json_normalize(df['ListaEESSPrecio'])], axis=1)

    # Convertir columnas categóricas a numéricas
    cols_to_convert = [
        'Precio Bioetanol', 'Precio Gas Natural Comprimido', 'Precio Gas Natural Licuado',
        'Precio Gases licuados del petróleo', 'Precio Gasoleo A', 'Precio Gasoleo B',
        'Precio Gasoleo Premium', 'Precio Gasolina 95 E10', 'Precio Gasolina 95 E5',
        'Precio Gasolina 95 E5 Premium', 'Precio Gasolina 98 E10', 'Precio Gasolina 98 E5',
        'Precio Hidrogeno'
    ]
    df_n[cols_to_convert] = df_n[cols_to_convert].applymap(lambda x: pd.to_numeric(x.replace(',', '.'), errors='coerce'))

    # Eliminar columnas que no interesan
    cols_to_drop = [
        'Margen', 'Remisión', 'Tipo Venta', '% BioEtanol', '% Éster metílico', 'Precio Biodiesel',
        'Precio Bioetanol', 'Precio Gas Natural Comprimido', 'Precio Gas Natural Licuado',
        'Precio Gases licuados del petróleo', 'Precio Gasolina 95 E10', 'Precio Gasolina 95 E5 Premium',
        'Precio Gasolina 98 E10', 'Precio Hidrogeno'
    ]
    df_n.drop(columns=cols_to_drop, inplace=True)

    # Renombrar columnas
    df_n.rename(columns={
        "Precio Gasoleo A": "Gasoleo A", "Precio Gasoleo B": "Gasoleo B", "Precio Gasoleo Premium": "Gasoleo Premium",
        "Precio Gasolina 95 E5": "Gasolina 95 E5", "Precio Gasolina 98 E5": "Gasolina 98 E5", "Rótulo": "Proveedor de Servicio"
    }, inplace=True)

    # Calcular medias nacionales
    for col in ['Gasoleo A', 'Gasoleo B', 'Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']:
        df_n[f'Media Nacional {col}'] = df_n[col].mean()

    # Calcular medias por código postal
    def calcular_media_cp(df, col):
        return df.groupby('C.P.')[col].transform('mean')

    for col in ['Gasoleo A', 'Gasoleo B', 'Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']:
        df_n[f'Media C.P. {col}'] = calcular_media_cp(df_n, col)

    # Ordenar columnas
    df_n = df_n[[
        'Fecha', 'Horario', 'C.P.', 'Provincia', 'Municipio', 'Localidad', 'Dirección', 'Proveedor de Servicio',
        'Gasoleo A', 'Media C.P. Gasoleo A', 'Media Nacional Gasoleo A',
        'Gasoleo B', 'Media C.P. Gasoleo B', 'Media Nacional Gasoleo B',
        'Gasoleo Premium', 'Media C.P. Gasoleo Premium', 'Media Nacional Gasoleo Premium',
        'Gasolina 95 E5', 'Media C.P. Gasolina 95 E5', 'Media Nacional Gasolina 95 E5',
        'Gasolina 98 E5', 'Media C.P. Gasolina 98 E5', 'Media Nacional Gasolina 98 E5'
    ]]

    # Normalizar nombres de proveedores de servicio
    def normalizar_proveedor(proveedor):
        proveedor = proveedor.replace('.', ' ').replace(',', ' ')
        proveedor = proveedor.replace('BP \S*', 'BP').replace('BPS \S*', 'BP').replace('BP\w*', 'BP')
        proveedor = proveedor.replace('SIN RÓTULO', 'OTROS').replace('(sin rótulo)', 'OTROS')
        proveedor = proveedor.replace('*', 'OTROS').replace('-', 'OTROS').replace('0', 'OTROS')
        return proveedor

    df_n['Proveedor de Servicio'] = df_n['Proveedor de Servicio'].apply(normalizar_proveedor)

    return df_n

# Función para calcular la media por tipo de combustible
def calcular_media(df, combustible, nivel):
    if nivel == 'C.P.':
        return df.groupby('C.P.')[combustible].transform('mean')
    elif nivel == 'Nacional':
        return df[combustible].mean()

# Función para obtener el mínimo por filtro
def obtener_minimo(df, filtro, valor, combustible):
    filtrado = df[df[filtro] == valor]
    return filtrado.loc[filtrado[combustible].idxmin()]

# Función para mostrar gráficos de comparación
def mostrar_grafico(df, combustible, nivel):
    media_cp = calcular_media(df, combustible, 'C.P.')
    media_nacional = calcular_media(df, combustible, 'Nacional')
    graphic = pd.DataFrame({
        combustible: df[combustible],
        f'Media C.P. {combustible}': media_cp,
        f'Media Nacional {combustible}': media_nacional
    }).T
    st.bar_chart(graphic)

# Cargar y procesar datos
gasolineras = load_data()

# Contenido del contenedor header
header = st.container()
with header:
    image = Image.open('logo.png')
    st.image(image, caption='Encuentra tu Gasolinera con el combustible más económico')

# Contenido del contenedor interaccion_usuario
interaccion_usuario = st.container()
with interaccion_usuario:
    st.header('GASOLINERAS EN ESPAÑA')
    st.sidebar.header("ENCUENTRA LA GASOLINERA MÁS BARATA FILTRANDO POR:")
    pages_names = ['Código Postal', 'Provincia', 'Municipio', 'Localidad', 'Proveedor de Servicio', 'Calculadora por kilómetros']
    page = st.sidebar.radio(' ', pages_names)

    # Filtrado por Código Postal
    if page == 'Código Postal':
        filtro_cp = gasolineras["C.P."].unique()
        filtro_combustible_cp = ['Gasoleo A', 'Gasoleo B', 'Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        caja_cp = st.sidebar.selectbox("Seleccione Código Postal", filtro_cp)
        combustible_cp = st.sidebar.selectbox("Seleccione tipo de combustible", filtro_combustible_cp)

        if st.sidebar.button('Buscar'):
            st.write(obtener_minimo(gasolineras, 'C.P.', caja_cp, combustible_cp))
            st.subheader('Comparación por tipo de combustible respecto a la Media por Código Postal y Nacional')
            mostrar_grafico(gasolineras, combustible_cp, 'C.P.')
        else:
            st.write(gasolineras)
            if st.checkbox('Todas las Gasolineras por Municipio'):
                caja_municipio = st.selectbox('Filtro por Municipio', gasolineras["Municipio"].unique())
                st.write(gasolineras[gasolineras["Municipio"] == caja_municipio])

    # Filtrado por Provincia
    elif page == 'Provincia':
        filtro_prov = gasolineras["Provincia"].unique()
        filtro_combustible_prov = ['Gasoleo A', 'Gasoleo B', 'Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        caja_prov = st.sidebar.selectbox("Seleccione Provincia", filtro_prov)
        combustible_prov = st.sidebar.selectbox("Seleccione tipo de combustible", filtro_combustible_prov)

        if st.sidebar.button('Buscar'):
            st.write(obtener_minimo(gasolineras, 'Provincia', caja_prov, combustible_prov))
            st.subheader('Comparación por tipo de combustible respecto a la Media por Código Postal y Nacional')
            mostrar_grafico(gasolineras, combustible_prov, 'Provincia')
        else:
            st.write(gasolineras)
            if st.checkbox('Todas las Gasolineras por Municipio'):
                caja_municipio = st.selectbox('Filtro por Municipio', gasolineras["Municipio"].unique())
                st.write(gasolineras[gasolineras["Municipio"] == caja_municipio])

    # Filtrado por Municipio
    elif page == 'Municipio':
        filtro_mun = gasolineras["Municipio"].unique()
        filtro_combustible_mun = ['Gasoleo A', 'Gasoleo B', 'Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        caja_mun = st.sidebar.selectbox("Seleccione Municipio", filtro_mun)
        combustible_mun = st.sidebar.selectbox("Seleccione tipo de combustible", filtro_combustible_mun)

        if st.sidebar.button('Buscar'):
            st.write(obtener_minimo(gasolineras, 'Municipio', caja_mun, combustible_mun))
            st.subheader('Comparación por tipo de combustible respecto a la Media por Código Postal y Nacional')
            mostrar_grafico(gasolineras, combustible_mun, 'Municipio')
        else:
            st.write(gasolineras)
            if st.checkbox('Todas las Gasolineras por Municipio'):
                caja_municipio = st.selectbox('Filtro por Municipio', gasolineras["Municipio"].unique())
                st.write(gasolineras[gasolineras["Municipio"] == caja_municipio])

    # Filtrado por Localidad
    elif page == 'Localidad':
        filtro_loc = gasolineras["Localidad"].unique()
        filtro_combustible_loc = ['Gasoleo A', 'Gasoleo B', 'Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        caja_loc = st.sidebar.selectbox("Seleccione Localidad", filtro_loc)
        combustible_loc = st.sidebar.selectbox("Seleccione tipo de combustible", filtro_combustible_loc)

        if st.sidebar.button('Buscar'):
            st.write(obtener_minimo(gasolineras, 'Localidad', caja_loc, combustible_loc))
            st.subheader('Comparación por tipo de combustible respecto a la Media por Código Postal y Nacional')
            mostrar_grafico(gasolineras, combustible_loc, 'Localidad')
        else:
            st.write(gasolineras)
            if st.checkbox('Todas las Gasolineras por Municipio'):
                caja_municipio = st.selectbox('Filtro por Municipio', gasolineras["Municipio"].unique())
                st.write(gasolineras[gasolineras["Municipio"] == caja_municipio])

    # Filtrado por Proveedor de Servicio
    elif page == 'Proveedor de Servicio':
        filtro_proveedor = gasolineras["Proveedor de Servicio"].unique()
        filtro_combustible_proveedor = ['Gasoleo A', 'Gasoleo B', 'Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        caja_proveedor = st.sidebar.selectbox("Seleccione Proveedor de Servicio", filtro_proveedor)
        proveedor_ES = gasolineras[gasolineras["Proveedor de Servicio"] == caja_proveedor]
        agree = st.sidebar.checkbox('Precio mas bajo para estación de servicio')

        if st.sidebar.button('Buscar'):
            st.write(proveedor_ES)
            if agree:
                oil_proveedor = st.sidebar.selectbox("Seleccione tipo de combustible", filtro_combustible_proveedor)
                st.subheader('Estación de Servicio mas barata para los filtros seleccionados')
                st.write(obtener_minimo(proveedor_ES, 'Proveedor de Servicio', caja_proveedor, oil_proveedor))
        else:
            st.write(gasolineras)
            if st.checkbox('Todas las Gasolineras por Municipio'):
                caja_municipio = st.selectbox('Filtro por Municipio', gasolineras["Municipio"].unique())
                st.write(gasolineras[gasolineras["Municipio"] == caja_municipio])

    # Calculadora por kilómetros
    elif page == 'Calculadora por kilómetros':
        filtro_combustible_p = ['Gasoleo A', 'Gasoleo B', 'Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        kilometros = st.number_input('Kilómetros recorridos')
        consumo_a_los_100 = st.number_input('Consumo a los 100 km')
        calculo_litros_consumo = (kilometros * consumo_a_los_100) / 100
        gasto_combustible = calculo_litros_consumo * st.selectbox("Seleccione tipo de combustible", filtro_combustible_p)
        st.write(f'Gasto de combustible estimado: {gasto_combustible}')