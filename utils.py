{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "5bbf079a-d365-49c6-a7d3-5e6a4f9810db",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "from skimage.feature import graycomatrix, graycoprops\n",
    "\n",
    "def preprocess_image(image):\n",
    "    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)\n",
    "    blur = cv2.GaussianBlur(gray, (5, 5), 0)\n",
    "    eq = cv2.equalizeHist(blur)\n",
    "    return eq\n",
    "\n",
    "def segment_image(gray_image):\n",
    "    _, mask = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)\n",
    "    return mask\n",
    "\n",
    "def extract_features(image, mask):\n",
    "    features = {}\n",
    "\n",
    "    masked = cv2.bitwise_and(image, image, mask=mask)\n",
    "    mean_val = cv2.mean(masked, mask=mask)\n",
    "    features['Mean R'] = mean_val[0]\n",
    "    features['Mean G'] = mean_val[1]\n",
    "    features['Mean B'] = mean_val[2]\n",
    "\n",
    "    features['Area'] = cv2.countNonZero(mask)\n",
    "\n",
    "    x, y, w, h = cv2.boundingRect(mask)\n",
    "    if h != 0:\n",
    "        features['Aspect Ratio'] = round(w / h, 2)\n",
    "    else:\n",
    "        features['Aspect Ratio'] = 0\n",
    "\n",
    "    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)\n",
    "    glcm = graycomatrix(gray, [1], [0], 256, symmetric=True, normed=True)\n",
    "    features['Contrast'] = graycoprops(glcm, 'contrast')[0, 0]\n",
    "    features['Homogeneity'] = graycoprops(glcm, 'homogeneity')[0, 0]\n",
    "\n",
    "    return features\n"
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
