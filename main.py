import streamlit as st

# Tuboo Tailoring Management System
st.title("Tuboo Tailoring Management System")

store_name = "Tuboo Men Tailoring"
version = "1.0.0"

st.write("Store Name: " + store_name)
st.write("Version: " + version)

# Session state to store clients
if 'clients' not in st.session_state:
    st.session_state.clients = []

st.subheader("Add New Client")
client_name = st.text_input("Client Name")
client_phone = st.text_input("Phone Number")

if st.button("Save Client"):
    if client_name and client_phone:
        st.session_state.clients.append({"name": client_name, "phone": client_phone})
        st.success("Client added successfully: " + client_name)
    else:
        st.warning("Please fill in all fields")

st.write("Total Clients:", len(st.session_state.clients))
