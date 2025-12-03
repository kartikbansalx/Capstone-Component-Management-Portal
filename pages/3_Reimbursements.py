import streamlit as st
import pandas as pd
from database.queries import (
    get_components,
    get_teams,
    submit_reimbursement,
    get_reimbursements
)

st.title("🧾 Reimbursement Management")

menu = ["View Reimbursements", "Submit Reimbursement"]
choice = st.sidebar.selectbox("Menu", menu)


if choice == "View Reimbursements":

    data = get_reimbursements()

    df = pd.DataFrame(data, columns=[
        "ReimID", "Component", "Team", "Status",
        "RequestedAmt", "ApprovedAmt", "Method", "Approver"
    ])

    st.table(df)

elif choice == "Submit Reimbursement":

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

    req_amt = st.number_input("Requested Amount (₹)", min_value=0.0)
    method = st.selectbox("Payment Method", ["UPI", "Bank Transfer", "Cash"])
    approver = st.text_input("Approval Authority")

    if st.button("Submit Request"):
        submit_reimbursement(comp_id, team_id, req_amt, method, approver)
        st.success("Reimbursement Request Submitted!")
