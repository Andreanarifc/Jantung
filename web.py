import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler
import numpy as np

# Pastikan path ke scaler benar
scaler_path = 'scaler.sav'

# Memuat scaler
with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)

    # Membaca model
    jantung_model = pickle.load(open('jantung_model.sav', 'rb'))

# Judul web
st.title('Klasifikasi Penyakit Jantung')

col1, col2 = st.columns(2)

with col1:
    age = st.text_input('Usia')
    age = float(age) if age else 0

with col2:
    sex = st.selectbox(
        "Jenis Kelamin",
        ("Perempuan", "Laki-laki"),
        index=None,
        placeholder="Pilih",
        key='gender_selectbox')
    
# Lakukan transformasi berdasarkan pilihan pengguna
if sex == "Perempuan":
    sex = 0
else:
    sex = 1

with col1:
    trestbps = st.text_input('Tekanan Darah')
    trestbps = float(trestbps) if trestbps else 0

with col2:
    cp = st.selectbox(
        "Nyeri Dada",
        ("Angina yang khas", "Angina tidak khas", "Nyeri non-angina", "Tanpa gejala"),
        index=None,
        placeholder="Pilih",
        key='cp_selectbox'
    )

# Lakukan transformasi berdasarkan pilihan pengguna
if cp == "Angina yang khas":
    cp = 0
elif cp == "Angina tidak khas":
    cp = 1
elif cp == "Nyeri non-angina":
    cp = 2
else:
    cp = 3

with col1:
    chol = st.text_input('Kolesterol')
    chol = float(chol) if chol else 0

with col2:
    fbs = st.selectbox(
        "Gula Darah lebih dari 120 mg/dl",
        ("Ya", "Tidak"),
        index=None,
        placeholder="Pilih",
        key='fbs_selectbox'
    )

# Lakukan transformasi berdasarkan pilihan pengguna
if fbs == "Ya":
    fbs = 1
else:
    fbs = 0

with col1:
    thalach = st.text_input('Detak jantung')
    thalach = float(thalach) if thalach else 0

with col2:
    restecg = st.selectbox(
        "Hasil Electrodiagram istirahat",
        ("Normal", "Mengalami kelainan gelombang ST-T", "Menunjukkan hipertrofi ventrikel kiri"),
        index=None,
        placeholder="Pilih",
        key='restecg_selectbox'
    )

# Lakukan transformasi berdasarkan pilihan pengguna
if restecg == "Normal":
    restecg = 0
elif restecg == "Mengalami kelainan gelombang ST-T":
    restecg = 1
else:
    restecg = 2

with col1:
    oldpeak = st.text_input("Status Depresi")
    oldpeak = float(oldpeak) if oldpeak else 0.0

with col2:
    exang = st.selectbox(
        "Induksi angina",
        ("Ya", "Tidak"),
        index=None,
        placeholder="Pilih",
        key='exang_selectbox'
    )

if exang == "Ya":
    exang = 1
else:
    exang = 0

# Prediksi
    jantung_diagnosis = ''

# Membuat tombol diagnosis
if st.button('Test Prediksi'):
    # Membuat array input
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]])
    
    # Mengaplikasikan scaler
    scaled_input_data = scaler.transform(input_data)
    
    # Melakukan prediksi
    jantung_prediction = jantung_model.predict(scaled_input_data)
    
    if jantung_prediction[0] == 1:
        jantung_diagnosis = 'Pasien terkena Penyakit Jantung'
    else:
        jantung_diagnosis = 'Pasien tidak terkena Penyakit Jantung'
        
    st.success(jantung_diagnosis)