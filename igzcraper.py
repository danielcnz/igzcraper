import streamlit as st
import yt_dlp
import os
import io

# 1. Configuración estética de la interfaz
st.set_page_config(page_title="IG Downloader Pro", page_icon="📲", layout="centered")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #E1306C;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📸 Instagram Media Downloader")
st.subheader("Descarga Reels, Videos y Fotos al instante")

# 2. Entrada de usuario
url = st.text_input("Pega el enlace de Instagram aquí:", placeholder="https://www.instagram.com/reels/...")

# 3. Lógica de descarga
if url:
    if "instagram.com" not in url:
        st.error("Por favor, introduce una URL válida de Instagram.")
    else:
        try:
            # Configuramos yt-dlp para que no guarde archivos permanentemente
            # Usamos un nombre genérico para procesarlo
            ydl_opts = {
                'format': 'best',
                'quiet': True,
                'no_warnings': True,
                'outtmpl': 'file_to_download.%(ext)s',
            }

            with st.spinner("🕵️ Analizando y preparando el archivo..."):
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # Extraer info sin descargar primero para verificar
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                    
                    # Determinar el tipo de archivo (MIME type)
                    extension = filename.split('.')[-1]
                    mime_type = "video/mp4" if extension == "mp4" else "image/jpeg"

                    # 4. Crear el botón de descarga real para el navegador
                    with open(filename, "rb") as f:
                        file_data = f.read()
                        
                    st.success("¡Archivo listo!")
                    st.download_button(
                        label="⬇️ Hacer clic para Guardar Archivo",
                        data=file_data,
                        file_name=f"instagram_download.{extension}",
                        mime=mime_type
                    )
                    
                    # 5. Limpieza: Borrar el archivo del servidor de Streamlit
                    os.remove(filename)

        except Exception as e:
            st.error(f"Ups! Algo salió mal. Es posible que el perfil sea privado o el link haya expirado.")
            st.info("Tip: Asegúrate de que el post sea de una cuenta pública.")

# Pie de página
st.markdown("---")
st.caption("Desarrollado con Python & Streamlit • Recuerda respetar los derechos de autor.")