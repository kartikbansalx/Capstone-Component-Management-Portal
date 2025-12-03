import streamlit as st
import pandas as pd
from database.queries import (
    get_components,
    get_teams,
    record_lending
)

st.title("📦 Component Lending")

menu = ["View Lending Records", "Record New Lending"]
choice = st.sidebar.selectbox("Menu", menu)


if choice == "View Lending Records":
    from database.queries import get_lending_records
    
    data = get_lending_records()
    
    df = pd.DataFrame(data, columns=[
        "LendingID", "Component", "Team", "Quantity",
        "LendDate", "DueDate", "Remarks"
    ])
    
    st.table(df)

elif choice == "Record New Lending":

    components = get_components()
    teams = get_teams()

    comp_dict = {c[0]: c[1] for c in components}
    team_dict = {t[0]: t[1] for t in teams}

    comp_id = st.selectbox(
        "Component",
        list(comp_dict.keys()),
        format_func=lambda x: comp_dict[x]
    )

    team_id = st.selectbox(
        "Team",
        list(team_dict.keys()),
        format_func=lambda x: team_dict[x]
    )

    qty = st.number_input("Quantity", min_value=1)
    remarks = st.text_area("Remarks")

    if st.button("Record Lending"):
        record_lending(comp_id, team_id, qty, remarks)
        st.success("Lending successfully recorded!")
