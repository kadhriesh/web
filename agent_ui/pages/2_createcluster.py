import streamlit as st

st.title("CLUSTER CREATION")


cluster_type = st.selectbox("Cluster Type", ["WORKLOAD", "MESH", "CONTROLPLANE"])