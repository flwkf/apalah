import streamlit as st
from pymongo import MongoClient

# Ambil Mongo URI dari secrets
def get_database():
    CONNECTION_STRING = st.secrets[MONGO_URI]
    client = MongoClient(CONNECTION_STRING)
    return client['coba']

db = get_database()
collection = db['cobaa']
data = collection.find_one()
st.write(data)
