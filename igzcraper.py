import streamlit as st
import yt_dlp
import os

# Configuración de página
st.set_page_config(page_title="IG Downloader Pro - Canada Zoom", page_icon="📸", layout="wide")

# CSS Personalizado para un look moderno
st.markdown("""
    <style>
    .main {
        background-color: #fafafa;
    }
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #f09433 0%,#e6683c 25%,#dc2743 50%,#cc2366 75%,#bc1888 100%);
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 10px;
        font-weight: bold;
        width: 100%;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Layout con columnas para centrar el contenido
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("📸 IG Video & Photo Downloader by Canada Zoom Corporation")
    st.info("💡 **Instrucciones:** Pega el link de un post público o Reel y presiona el botón.")

    # Caja de entrada
    url = st.text_input("", placeholder="https://www.instagram.com/p/...")

    if st.button("🚀 Preparar mi descarga"):
        if url:
            try:
                with st.spinner("Procesando... esto puede tardar unos segundos"):
                    ydl_opts = {
                        'format': 'best',
                        'outtmpl': 'descarga_temp_%(title)s.%(ext)s',
                        'quiet': True,
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=True)
                        filename = ydl.prepare_filename(info)
                    
                    if os.path.exists(filename):
                        with open(filename, "rb") as file:
                            st.download_button(
                                label="✅ Descarga lista - Haz clic aquí",
                                data=file,
                                file_name=filename.replace("descarga_temp_", ""),
                                mime="video/mp4" if filename.endswith(".mp4") else "image/jpeg"
                            )
                        # Opcional: Borrar archivo local después de generar el botón
                        os.remove(filename)
            except Exception as e:
                st.error("No pudimos obtener el video. Verifica que el link sea de una cuenta pública.")
        else:
            st.warning("Primero debes pegar una URL.")

    st.markdown("---")
    st.caption("Creado con Python y Streamlit")
