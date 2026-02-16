import streamlit as st
import yt_dlp
import os

# Configuración de página
st.set_page_config(page_title="IG Downloader Pro", page_icon="📸", layout="wide")

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
                    # Configuración optimizada para evitar bloqueos
                    ydl_opts = {
                        'format': 'best',
                        'outtmpl': 'descarga_temp_%(title)s.%(ext)s',
                        'quiet': True,
                        'no_warnings': True,
                        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                        'referer': 'https://www.google.com/',
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
                        # Borrar archivo local del servidor después de preparar el botón
                        os.remove(filename)
            except Exception as e:
                st.error(f"No pudimos obtener el recurso. Verifica que el link sea de una cuenta pública.")
                st.caption(f"Detalle del error: {e}")
        else:
            st.warning("Primero debes pegar una URL.")

    st.markdown("---")
    st.caption("Creado por Canada Zoom Corporation con Python y Streamlit")
