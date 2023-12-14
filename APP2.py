#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np

# Cargar datos
df = pd.read_csv("ALMACEN.csv", delimiter=';')  
df.replace(to_replace=[None], value=np.nan, inplace=True)

# Logo y nombre de la empresa
logo_empresa = "Logo.jpg"
st.image(logo_empresa, use_column_width=False, width=100)  # Ajusta el tamaño del logo
st.title("BIOGINEFARMA")  # Usa st.title para un texto más grande

# Título de la aplicación
st.title("Búsqueda de producto por número de lote")

# Autocompletado para el número de lote
numero_lote_buscar = st.selectbox("SELECCIONA O ESCRIBE EL NÚMERO DE LOTE DEL PRODUCTO:",
                                   df['LOTE'].unique(),
                                   format_func=lambda x: f"{x}")  # Muestra las sugerencias con formato

# Verificar si se seleccionó un número de lote
if numero_lote_buscar:
    # Realizar la búsqueda basada en el número de lote
    resultado = df.loc[df['LOTE'] == numero_lote_buscar]

    if resultado.empty:
        st.warning("El número de lote no fue encontrado. Recuerda que si lleva letras deben estar en mayúsculas")
    else:
        producto = resultado.iloc[0]['PRODUCTO']
        calle = int(resultado.iloc[0]['CALLE'])
        jaula = int(resultado.iloc[0]['JAULA'])
        cajon = int(resultado.iloc[0]['CAJON'])
        stock = int(resultado.iloc[0]['STOCK'])
        
        # Mostrar la información en diferentes párrafos
        st.success(f"El producto {producto} con número de lote {numero_lote_buscar} se encuentra en:")
        st.write(f"Calle: {calle}")
        st.write(f"Jaula: {jaula}")
        st.write(f"Cajón: {cajon}")
        st.write(f"Stock: {stock} pcs.")

        # Mostrar plano del almacen
        foto_almacen = "PLANO.png"
        st.image(foto_almacen, caption="Plano del almacén", use_column_width=True)
        
        # Mostrar imagen producto
        enlace_imagen = resultado.iloc[0]['PNG']
        st.image(enlace_imagen, caption=f"Imagen del producto {producto}", use_column_width=True)

