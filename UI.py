import streamlit as st
from streamlit_option_menu import option_menu
import extra_streamlit_components as stx
import psycopg2

dsn = "postgresql://eh5b17:xau_h6oA2zsTsNzOhau4F6OIMc1zm5iIbRsT1@us-east-1.sql.xata.sh/hackathon:main?sslmode=require"

def obtener_proveedores():
    conn = psycopg2.connect(dsn)
    cursor = conn.cursor()
    query = "SELECT razon FROM supersociedades;"
    cursor.execute(query)
    resultados = [fila[0].upper() for fila in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados

def consultar_proveedor(razon):
    conn = psycopg2.connect(dsn)
    cursor = conn.cursor()
    query = f"SELECT * FROM supersociedades where razon = '{razon.lower()}';"
    cursor.execute(query)
    infoProveedor = cursor.fetchall()
    cursor.close()
    conn.close()
    return infoProveedor

if "proveedores" not in st.session_state:
    st.session_state.proveedores = obtener_proveedores()

proveedores = st.session_state.proveedores

iconos = ["house"] + ["building"] * (len(proveedores) - 1)

with st.sidebar:
    selected = option_menu(
        "Proveedores en construcción", 
        ["Menú"] + proveedores,
        icons=iconos,
        menu_icon="tools",
        default_index=0,
        key="menu_proveedores"
    )

st.session_state.selected_proveedor = selected

st.write(f"Opción seleccionada: {st.session_state.selected_proveedor}")

if selected != "Menú":

    st.session_state.info_selected_proveedor = consultar_proveedor(st.session_state.selected_proveedor)

    tabs = st.tabs(["Información general", 
                "Información financiera", 
                "Información judicial", 
                "Experiencia"])
    
    # Lógica para cada pestaña
    with tabs[0]:
        st.header(f"Información general de {selected}")
        st.write("Aquí va la información general del proveedor seleccionado.")
        st.write(f"Info proveedor: {st.session_state.info_selected_proveedor}")

    with tabs[1]:
        st.header(f"Información financiera de {selected}")
        st.write("Aquí va la información financiera del proveedor seleccionado.")

    with tabs[2]:
        st.header(f"Información judicial de {selected}")
        st.write("Aquí va la información judicial del proveedor seleccionado.")

    with tabs[3]:
        st.header(f"Experiencia de {selected}")
        st.write("Aquí va la experiencia del proveedor seleccionado.")
else:
    st.write("Selecciona un proveedor para ver su información.")