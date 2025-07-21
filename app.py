import streamlit as st
import cv2
import numpy as np
from PIL import Image
from utils import preprocess_image, segment_image, extract_features

st.set_page_config(page_title="Pengolahan Citra", layout="wide")
st.title("🧠 Pengolahan Citra: Preprocessing, Segmentasi & Ekstraksi Ciri")

st.markdown("Upload gambar, sistem akan memproses dan menampilkan hasil segmentasi serta ciri-cirinya.")

# Upload gambar
uploaded_file = st.file_uploader("Unggah gambar", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    img_np = np.array(image)

    st.image(image, caption='Gambar Asli', use_column_width=True)

    # Proses pengolahan citra
    preprocessed = preprocess_image(img_np)
    segmented = segment_image(preprocessed)
    features = extract_features(img_np, segmented)

    col1, col2 = st.columns(2)
    with col1:
        st.image(preprocessed, caption='Preprocessing (Grayscale & Equalization)', use_column_width=True, clamp=True, channels="GRAY")
    with col2:
        st.image(segmented, caption='Segmentasi (Otsu Thresholding)', use_column_width=True, clamp=True, channels="GRAY")

    # Tampilkan hasil ekstraksi ciri
    st.subheader("📊 Ciri-ciri Gambar")
    for key, value in features.items():
        st.write(f"**{key}**: {value:.2f}" if isinstance(value, float) else f"**{key}**: {value}")
