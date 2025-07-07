import streamlit as st

st.title("CLUSTER STATUS")


cluster_type = st.selectbox("SELECT MANAGMENT CLUSTER ", ["MGMT-A", "MGMT-B", "TEST-CLUSTER"])