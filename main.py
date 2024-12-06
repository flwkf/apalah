import streamlit as st
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, ConfigurationError

# Ambil Mongo URI dari secrets
def get_database():
    CONNECTION_STRING = st.secrets["MONGO_URI"]
    client = MongoClient(CONNECTION_STRING)
    return client['coba']

try:
    db = get_database()
    collection = db['cobaa']
    data = collection.find_one()
    if data:
        st.write(data)
    else:
        st.write("Tidak ada data yang ditemukan.")
except ServerSelectionTimeoutError:
    st.error("Tidak dapat terhubung ke database. Periksa URI dan koneksi internet Anda.")
except ConfigurationError as e:
    st.error(f"Terjadi kesalahan konfigurasi: {e}")
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
