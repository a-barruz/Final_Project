import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import json



header = st.container()
dataset = st.container()
interaccion_usuario = st.container()
graficos = st.container()
    
    
with header:

    image = Image.open('logo.png')

    st.image(image, caption='Encuentra la Gasolinera  más económico ')

    


with dataset:
    
    gasolineras = pd.read_csv("./df_sample.csv", dtype={"C.P.":str})

  
with interaccion_usuario:

    st.header('GASOLINERAS EN ESPAÑA')

    gasolineras = pd.DataFrame(gasolineras)
    

    # Radio Buttons   
    
    st.sidebar.header("PRECIO MÍNIMO FILTRANDO POR:")
    
    pages_names = ['Código Postal', 'Provincia', 'Localidad', 'Proveedor de Servicio']

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
#try:   
    #if page == 'Municipio':
    
        #Filtros para operaciones en cajas
        #filtro_combustible = ['Gasoleo A', 'Gasoleo B','Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        #filtro_municipio = gasolineras["Municipio"].unique()
    
        # Cajas Sidebar
        #caja_municipio = st.sidebar.selectbox("Seleccione Municipio", filtro_municipio)
        #combustible = st.sidebar.selectbox("Seleccione tipo de combustible", filtro_combustible)

        #def cp_minimo(caja_municipio, combustible):
            #municipio = gasolineras[(gasolineras["Municipio"] == caja_municipio)]
            #filtro_df_n_2= municipio.loc[municipio[[combustible]].idxmin()]
            #return(filtro_df_n_2) 

    

        #if st.sidebar.button('Buscar'):
            #st.write(cp_minimo(caja_municipio, combustible))
        
            #st.subheader('Comparación por tipo de combustible respecto a la Media por Código Postal y Nacional')

            #def mean_CP(combustible):
                #if combustible == 'Gasoleo A':
                    #var = 'Media C.P. Gasoleo A'        
                #if combustible == 'Gasoleo B':
                    #var = 'Media C.P. Gasoleo B'      
                #if combustible == 'Gasoleo Premium':
                    #var = 'Media C.P. Gasoleo P'
                #if combustible == 'Gasolina 95 E5':
                    #var = 'Media C.P. Gasolina 95'
                #if combustible == 'Gasolina 98 E5':
                    #var = 'Media C.P. Gasolina 98'             
                #return var

            #def mean(combustible):
                #if combustible == 'Gasoleo A':
                    #var ='Media Nacional Gasoleo A'        
                #if combustible == 'Gasoleo B':
                    #var = 'Media Nacional Gasoleo B'        
                #if combustible == 'Gasoleo Premium':
                    #var = 'Media Nacional Gasoleo P'
                #if combustible == 'Gasolina 95 E5':
                    #var = 'Media Nacional Gasolina 95'
                #if combustible == 'Gasolina 98 E5':
                    #var = 'Media Nacional Gasolina 98'
                #return var

            #graphic = pd.DataFrame(cp_minimo(caja_municipio, combustible), columns=[combustible, mean_CP(combustible), mean(combustible)]).T
            #st.bar_chart(graphic)
    
            #if st.sidebar.button('Limpiar'):
                #st.write(gasolineras)


                
        #else:
            #st.write(gasolineras)
        
            #caja_general = st.checkbox('Todas las Gasolineras por Municipio')
            #if caja_general:        
                #filtro_municipio = gasolineras["Municipio"].unique()
                #caja_municipio=st.selectbox('Filtro por Municipio', filtro_municipio)
                #def cp_minimo(caja_municipio):
                    #municipio = gasolineras[(gasolineras["Municipio"] == caja_municipio)]
                    #return municipio 
                
                #st.write(cp_minimo(caja_municipio))
#except:
    #st.error('No hay suministro para el combustible seleccionado', icon="🚨")
    
    #peligro = Image.open('sin_combustible.png')
    #st.image(peligro)
      



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
            
       
 
# Fin
# Radio Buttons   
    
        #calculadora = st.sidebar.checkbox('Calculadora de combustible por kilómetros')

if st.sidebar.checkbox('Calculadora de combustible por kilómetros'):
    
    kilometros = st.number_input('Km a recorrer', 0, 10000000000)

    consumo = st.number_input('Introduzca el gasto medio en litros de su coche por cada 100km recorridos', 0.0, 10000.5)
        
    resultado = (kilometros * consumo) / 100
        
    st.write('Litros consumidos', resultado)

    precio_litro=st.number_input('Indique el precio mínimo, por litro de combustible', 0.0, 100.9)

    calculo_precio_litro = precio_litro * resultado

    st.write ('El importe total de su viaje en € es: ', calculo_precio_litro)


















        

