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
        # Manejar casos de valores desconocidos o NaN
        calle = resultado.iloc[0]['CALLE'] if pd.notna(resultado.iloc[0]['CALLE']) else "Desconocido"
        jaula = int(resultado.iloc[0]['JAULA']) if pd.notna(resultado.iloc[0]['JAULA']) else "Desconocido"        
        cajon = int(resultado.iloc[0]['CAJON']) if pd.notna(resultado.iloc[0]['CAJON']) else "Desconocido"
        stock = int(resultado.iloc[0]['STOCK']) if pd.notna(resultado.iloc[0]['STOCK']) else "Desconocido"
        
        # Mostrar la información en diferentes párrafos
        st.success(f"El producto {producto} con número de lote {numero_lote_buscar} se encuentra en:")
        st.write(f"Calle: {calle}")
        st.write(f"Jaula: {jaula}")
        st.write(f"Cajón: {cajon}")
        st.write(f"Stock: {stock} pcs.")

        # Mostrar plano del almacén
        foto_almacen = "PLANO.png"
        st.image(foto_almacen, caption="Plano del almacén", use_column_width=True)
        
        # Verificar si la columna de imagen está vacía antes de intentar mostrarla
        enlace_imagen = resultado.iloc[0]['PNG']
        if pd.notna(enlace_imagen):
            st.image(enlace_imagen, caption=f"Imagen del producto {producto}", use_column_width=True)
        else:
            st.warning("No hay imagen disponible para este producto.")

