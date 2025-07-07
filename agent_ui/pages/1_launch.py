import streamlit as st

st.title("CNAP Agent")

multi = ''' **CNAP** Agent helps you.
Manage life cycle of the clusters Here is the list of features offered by an CNAP AGENT.

- **Create Cluster**: Create a new cluster with the desired configuration.
- **Delete Cluster**: Delete an existing cluster.
- **Status of the Cluster**: Knew the Real time status of cluster.        
'''
st.markdown(multi)

value  = st.radio(
    "What actions do you want to perform?",
    [":Create", ":Staus", ":Delete"],
    captions=[
        "Create a new cluster.",
        "Status of the cluster.",
        "Delete the cluster.",
    ],
)


if value == ":Create":
    st.write("You selected Create Cluster")
    st.write("Please provide the details to create a cluster.")
    cluster_name = st.text_input("Cluster Name")
    cluster_type = st.selectbox("Cluster Type", ["WORKLOAD", "MESH", "CONTROLPLANE"])
    if st.button("Create Cluster"):
        st.success(f"Cluster '{cluster_name}' of type '{cluster_type}' created successfully!")
