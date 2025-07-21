{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "640a3556-7cd4-41e1-a692-b84c73c78a14",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import cv2\n",
    "import numpy as np\n",
    "from PIL import Image\n",
    "from utils import preprocess_image, segment_image, extract_features\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "st.set_page_config(page_title=\"Pengolahan Citra\", layout=\"wide\")\n",
    "st.title(\"🔍 Aplikasi Pengolahan Citra Digital\")\n",
    "st.markdown(\"Upload gambar, dan sistem akan melakukan **preprocessing**, **segmentasi**, serta **ekstraksi ciri**.\")\n",
    "\n",
    "# Upload gambar\n",
    "uploaded_file = st.file_uploader(\"Unggah gambar\", type=[\"jpg\", \"png\", \"jpeg\"])\n",
    "\n",
    "if uploaded_file:\n",
    "    image = Image.open(uploaded_file).convert('RGB')\n",
    "    img_np = np.array(image)\n",
    "    st.image(image, caption='Gambar Asli', use_column_width=True)\n",
    "\n",
    "    # Proses\n",
    "    preprocessed = preprocess_image(img_np)\n",
    "    segmented = segment_image(preprocessed)\n",
    "    features = extract_features(img_np, segmented)\n",
    "\n",
    "    # Tampilkan hasil\n",
    "    col1, col2 = st.columns(2)\n",
    "\n",
    "    with col1:\n",
    "        st.image(preprocessed, caption=\"Hasil Preprocessing (Grayscale + Equalized)\", use_column_width=True, clamp=True, channels=\"GRAY\")\n",
    "\n",
    "    with col2:\n",
    "        st.image(segmented, caption=\"Mask Segmentasi (Otsu Threshold)\", use_column_width=True, clamp=True, channels=\"GRAY\")\n",
    "\n",
    "    # Tampilkan ciri\n",
    "    st.subheader(\"📌 Ciri-ciri Gambar:\")\n",
    "    for key, val in features.items():\n",
    "        st.write(f\"**{key}**: {val:.2f}\" if isinstance(val, float) else f\"**{key}**: {val}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
