import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



header = st.container()
dataset = st.container()
interaccion_usuario = st.container()
graficos = st.container()
    
    
with header:

    image = Image.open('logo.png')

    st.image(image, caption='Encuentra tu Gasolinera con el combustible más económico ')

    


with dataset:
    
    gasolineras = pd.read_csv("./df_sample.csv")
    #st.text(pd.DataFrame(gasolineras))

  
with interaccion_usuario:

    st.header('GASOLINERAS EN ESPAÑA')

    gasolineras = pd.DataFrame(gasolineras)
    gasolineras['C.P.'] = gasolineras[['C.P.']].astype(str)

   
    # Radio Buttons   
    
    st.sidebar.header("ENCUENTRA EL COMBUSTIBLE MÁS ECONÓMICO FILTRANDO POR:")
    
    pages_names = ['Código Postal', 'Municipio', 'Provincia', 'Localidad']

    page = st.sidebar.radio(' ', pages_names)

    

# Slicing for Códgigo Postal
    if page == 'Código Postal':
        
        # Filtro Código Postal
        filtro_cp = gasolineras["C.P."].unique()
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
        
            st.title('Comparación de precio respecto la media Nacional')
            def mean(combustible_cp):
                if combustible_cp == 'Gasoleo A':
                    var = 'Media_Gasoleo A'          
                if combustible_cp == 'Gasoleo B':
                    var = 'Media_Gasoleo B'        
                if combustible_cp == 'Gasoleo Premium':
                    var = 'Media_Gasoleo Prem'
                if combustible_cp == 'Gasolina 95 E5':
                    var = 'Media_Gasolina 95'
                if combustible_cp == 'Gasolina 98 E5':
                    var = 'Media_Gasolina 98'              
                return var
            
            graphic = pd.DataFrame(p_minimo(caja_cp, combustible_cp), columns=[combustible_cp, mean(combustible_cp)]).T
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

# Slicing for Municipio
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
        
            st.title('Comparación de precio respecto la media Nacional')
            def mean(combustible):
                if combustible == 'Gasoleo A':
                    var = 'Media_Gasoleo A'          
                if combustible == 'Gasoleo B':
                    var = 'Media_Gasoleo B'        
                if combustible == 'Gasoleo Premium':
                    var = 'Media_Gasoleo Prem'
                if combustible == 'Gasolina 95 E5':
                    var = 'Media_Gasolina 95'
                if combustible == 'Gasolina 98 E5':
                    var = 'Media_Gasolina 98'              
                return var

            graphic = pd.DataFrame(cp_minimo(caja_municipio, combustible), columns=[combustible, mean(combustible)]).T
            st.bar_chart(graphic)
    
            if st.sidebar.button('Limpiar'):
                st.write(gasolineras)

        else:
            st.write(gasolineras)

        caja_general = st.checkbox('Todas las Gasolineras por Municpio ')
        if caja_general:        
            filtro_municipio_gen = gasolineras["Municipio"].unique()
            caja_municipio_gen=st.selectbox('Filtro por Municipio', filtro_municipio_gen)
            def cp_minimo(caja_municipio_gen):
                municipio = gasolineras[(gasolineras["Municipio"] == caja_municipio_gen)]
                return municipio 
                
            st.write(cp_minimo(caja_municipio_gen))


 # Slicing for Provincia
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
        
            st.title('Comparación de precio respecto la media Nacional')
            def mean(oil_prov):
                if oil_prov == 'Gasoleo A':
                    var = 'Media_Gasoleo A'          
                if oil_prov == 'Gasoleo B':
                    var = 'Media_Gasoleo B'        
                if oil_prov == 'Gasoleo Premium':
                    var = 'Media_Gasoleo Prem'
                if oil_prov == 'Gasolina 95 E5':
                    var = 'Media_Gasolina 95'
                if oil_prov == 'Gasolina 98 E5':
                    var = 'Media_Gasolina 98'              
                return var
                
            graphic = pd.DataFrame(provincia_min(box_mun, oil_prov), columns=[oil_prov, mean(oil_prov)]).T
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
        

 # Slicing for 'Proveedor de Servicio':
    if page == 'Localidad':
    
        #Filtros para operaciones en cajas
        filter_oil_proveedor = ['Gasoleo A', 'Gasoleo B','Gasoleo Premium', 'Gasolina 95 E5', 'Gasolina 98 E5']
        filter_proveedor = gasolineras["Localidad"].unique()
    
        # Cajas Sidebar
        box_proveedor = st.sidebar.selectbox("Seleccione Proveedor de Servicio", filter_proveedor)
        oil_proveedor = st.sidebar.selectbox("Seleccione tipo de combustible", filter_oil_proveedor)

        def proveedor_min(box_proveedor, oil_proveedor):
            proveedor = gasolineras[(gasolineras["Localidad"] == box_proveedor)]
            filtro_df_n_2= proveedor.loc[proveedor[[oil_proveedor]].idxmin()]
            return(filtro_df_n_2) 

    

        if st.sidebar.button('Buscar'):
            st.write(proveedor_min(box_proveedor, oil_proveedor))
        
            st.title('Comparación de precio respecto la media Nacional')
            def mean(oil_provedor):
                if oil_provedor == 'Gasoleo A':
                    var = 'Media_Gasoleo A'          
                if oil_provedor == 'Gasoleo B':
                    var = 'Media_Gasoleo B'        
                if oil_provedor == 'Gasoleo Premium':
                    var = 'Media_Gasoleo Prem'
                if oil_provedor == 'Gasolina 95 E5':
                    var = 'Media_Gasolina 95'
                if oil_provedor == 'Gasolina 98 E5':
                    var = 'Media_Gasolina 98'              
                return var
                
            graphic = pd.DataFrame(proveedor_min(box_proveedor, oil_proveedor), columns=[oil_proveedor, mean(oil_proveedor)]).T
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


     
    
        
   

   




















        

