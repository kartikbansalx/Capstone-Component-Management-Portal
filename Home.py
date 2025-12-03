import streamlit as st


st.set_page_config(
    page_title="Capstone Component Management System",
    page_icon="🎓",
    layout="wide"
)


st.markdown("""
<style>

    /* PAGE BACKGROUND */
    body {
        background-color: #F7F9FB;
    }

    /* TITLE STYLING */
    .title {
        text-align:center;
        font-size:42px;
        color:#D50000;  /* RED */
        font-weight:700;
        margin-top:-10px;
    }

    .subtitle {
        text-align:center;
        font-size:20px;
        color:#D50000;  /* RED */
        margin-bottom:20px;
    }

    /* SIDEBAR STYLING */
    [data-testid="stSidebar"] {
        background-color: #B71C1C !important; /* DARK RED */
    }

    [data-testid="stSidebar"] * {
        color: white !important;
        font-weight:600;
    }

    
                /* FOOTER */
  /* FOOTER */
    .footer {
        position: fixed;
        left: 175px;
        bottom: 10px;
        width: 100%;
        text-align: center;
        color: #D50000;
        font-size: 20px;
    }


</style>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo3.png", width=500)



st.markdown('<div class="title">Capstone Project Management System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Select a section from the left sidebar</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("background.png", use_column_width=True)



st.markdown("""
<div class="footer">
Developed by Kartik
</div>
""", unsafe_allow_html=True)
