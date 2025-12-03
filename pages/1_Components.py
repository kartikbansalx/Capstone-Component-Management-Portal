import streamlit as st
import pandas as pd
from database.queries import get_components, add_component

st.title("Manage Components")

menu = ["View Components", "Add Component"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "View Components":
    data = get_components()
    df = pd.DataFrame(data, columns=["ComponentID", "Component Name", "Quantity"])
    st.table(df)

elif choice == "Add Component":
    name = st.text_input("Component Name")
    category = st.text_input("Category")
    desc = st.text_area("Description")
    spec = st.text_input("Specification")
    qty = st.number_input("Quantity", min_value=0)
    cond = st.text_input("Condition")
    cost = st.number_input("Unit Cost", min_value=0.0)
    vendor = st.number_input("Vendor ID", min_value=0)
    minstock = st.number_input("Minimum Stock", min_value=0)
    consumable = st.selectbox("Is Consumable?", ["Y", "N"])

    if st.button("Add Component"):
        add_component(name, category, desc, spec, qty, cond, cost, vendor, minstock, consumable)
        st.success("Component added successfully!")
        
