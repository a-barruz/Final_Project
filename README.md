# Proyecto Cheapest Oil


🏃 Product Description

Chepeast oil es un buscador de gasolineras a nivel Nacional, para localizar la gasolinera con el combustible más barato filtrando por:

- Códgio postal 
- Provincia
- Municipio 
- Localidad.


# 💻 Technology stack

La tecnología utilizada en Cheapest Oil ha sido:

1- 2 -El lenguaje de programación utilizado es Python, versión 3.9. 

2 - API Rest: hacemos llamada a la API del Gobierno (https://datos.gob.es/), a traves de la tecnología REST para descargar JSON con el precio de carburantes de las gasolineras españolas.

3 - Librerías utilizadas: 

- urlopen: con esta libreria nos conectamos a la API guardar y posteriormente abrir los datos a través de éste método.
- json_normalize: Al extraer el objeto, nos encontramos con que la información que nos interesa esta en un JSON, dentro de otro JSON, por lo que utilizamos dicha libreria para conseguir la información que nos interesa.
- Pandas
- Numpy
- streamlit: Para hacer reporting de la programación desarrollada en Python, utilizamos la librería streamlit, versión 1.13.0
-  Image: La utilizamos para cargar imágenes en Streamlit.


# 💥 Core 
El proyecto surge por la necesidad de anlizar la información respecto a los precios del combustible que se están viendo afectados por grandes subidas debido a los conflictos políticos y bélicos.

    
# 🔧 Configuration

La configuración de Chepest oil, está dividida en tres partes, estructuradas de la siguiente manera:

1 - MVP_Final_Project: se realiza un EDA para analizar la calidad de los datos y posteriormente realizar acciones a partir de dicho análisis.

2 - sample_project.py: es el archivo .py para ejecutar streamlit. Se carga el Dataframe diseñado en MVP_Final_Project (denominado gasolineras) y se realizan las acciones necesarias para ejecutar la herramienta de reporting (cheapest oil), en streamlit.

3 - run sreamlit sample_project.py: se ejecuta el .py en la terminal para visualizar el report en streamlit.


# 📁 Folder structure
└── https://github.com/angel-barruz/Final_Project.git
    
    ├── df_sample.csv
    
    ├── logo.png
    
    ├── MVP_Final_Project.ipynb
    
    ├── sample_project.py
    
    ├── daily data


# 💩 ToDo

1 - Con los csv guardados en daily data, se realizarán predicciones de la tendencia a futruo del prcio utilizando la tecnología forecast.

2 - Unificar configuración para que se realice el proceso automáticamente.

3 - Conexión a API de Google Maps para que a través de las direcciones se conecte directamente a través de links en Dirección.


# Resources

Los recursos utilizados para Cheapes Oil han sido:

https://pandas.pydata.org/pandas-docs/stable/ # Documentación Pandas

https://numpy.org/doc/ # Documentación Numpy

https://docs.streamlit.io/ # Documentación Streamlit

https://stackoverflow.com/

https://www.youtube.com/

https://chatgpt.com/



# 💌 Contact info
Ángel Barruz Montalvo

Tel: 680 50 57 51

email: a.barruz@gmail.com
