import streamlit as st

from utils.predictor import predict_solubility
from utils.molecule_utils import get_molecule_info

st.set_page_config(
    page_title="CO₂ Solubility Predictor",
    layout="wide"
)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        180deg,
        #F4F7FC 0%,
        #E8EEF9 100%
    );
}

header{
    visibility:hidden;
}

[data-testid="stHeader"]{
    background:transparent;
}

.block-container{
    padding-top:0.5rem !important;
}

.main-title{
    text-align:center;
    font-size:54px;
    font-weight:800;
    color:#0B3C5D;
    margin-bottom:0px;
}

.subtitle{
    text-align:center;
    font-size:24px;
    color:#5B6475;
    margin-top:5px;
}

.section-title{
    font-size:34px;
    font-weight:700;
    color:#0B3C5D;
    margin-top:25px;
    margin-bottom:15px;
}

div[data-testid="stForm"]{
    background:white;
    padding:30px;
    border-radius:22px;
    border:1px solid #DCE3F1;
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
}

label{
    color:#102A43 !important;
    font-size:18px !important;
    font-weight:600 !important;
}

.stTextInput input{
    background:#F8FAFC !important;
    color:black !important;
    border:2px solid #D1D9E6 !important;
    border-radius:12px !important;
}

.stNumberInput input{
    background:#F8FAFC !important;
    color:black !important;
    border:2px solid #D1D9E6 !important;
    border-radius:12px !important;
}

input{
    color:black !important;
}

.stFormSubmitButton > button{

    width:100%;
    height:60px;

    background:linear-gradient(
        90deg,
        #2563EB,
        #1D4ED8
    );

    color:black !important;
    font-size:20px;
    font-weight:700;

    border:none;
    border-radius:14px;

    box-shadow:0px 6px 15px rgba(37,99,235,0.35);
}

.info-card{
    background:white;
    padding:25px;
    border-radius:20px;
    text-align:center;
    border:1px solid #DCE3F1;
    box-shadow:0px 8px 20px rgba(0,0,0,0.06);
    margin-top:15px;
    margin-bottom:30px;
}
h1 a,
h2 a,
h3 a,
h4 a,
h5 a,
h6 a {
    display: none !important;
}


.result-card{
    background:white;
    padding:35px;
    border-radius:20px;
    text-align:center;
    border:1px solid #DCE3F1;
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
}
.result-card{
    color:#0B3C5D !important;
}

.result-card h1{
    color:#0B3C5D !important;
}

.result-card h2{
    color:#0B3C5D !important;
}

.result-card h3{
    color:#0B3C5D !important;
}

.result-card p{
    color:#475569 !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

left, center, right = st.columns([1.5,5,1.5])

with left:
    st.image(
        "assets/Birla_Institute_of_Technology_Mesra.png",
        width=120
    )

with center:

    st.markdown(
        """
        <div class="main-title">
        CO₂ Solubility Prediction Platform
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
        Machine Learning Framework for Ionic Liquids
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    st.image(
        "assets/IIT_Kharagpur_Logo.svg.png",
        width=120
    )

# ==========================================================
# INFO CARD
# ==========================================================

st.markdown("""
<div class="info-card">

<h3 style="
color:#1E3A8A;
margin-bottom:10px;
font-size:30px;
">
Predict CO₂ Solubility in Ionic Liquids
</h3>

<p style="
font-size:18px;
color:#4B5563;
margin-bottom:0px;
">
Enter cation and anion SMILES along with operating conditions.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# INPUT SECTION
# ==========================================================

st.markdown(
    '<div class="section-title">Input Parameters</div>',
    unsafe_allow_html=True
)

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        cation_smiles = st.text_input(
            "Cation SMILES"
        )

        temperature = st.number_input(
            "Temperature (°C)",
            value=25.0
        )

    with col2:

        anion_smiles = st.text_input(
            "Anion SMILES"
        )

        pressure = st.number_input(
            "Pressure (bar)",
            value=1.0
        )

    predict = st.form_submit_button(
        "Predict CO₂ Solubility"
    )

# ==========================================================
# RESULTS
# ==========================================================

if predict:

    try:

        prediction, feature_df = predict_solubility(
            cation_smiles,
            anion_smiles,
            temperature,
            pressure
        )

        cat_info = get_molecule_info(
            cation_smiles
        )

        an_info = get_molecule_info(
            anion_smiles
        )

        st.success("Prediction Successful")

        # ==================================================
        # PREDICTION CARD
        # ==================================================

        st.markdown(
            f"""
            <div class="result-card">

            <h3 style="
            color:#1E3A8A;
            margin-bottom:20px;
            ">
            Predicted CO₂ Solubility
            </h3>

            <h1 style="
            font-size:72px;
            color:#0B3C5D;
            margin-bottom:10px;
            ">
            {prediction:.4f}
            </h1>

            <p style="
            color:#64748B;
            font-size:24px;
            ">
            mol CO₂ / mol Ionic Liquid
            </p>

            <hr>

            <p style="
            color:#475569;
            font-size:18px;
            ">
            Temperature = {temperature} °C
            <br>
            Pressure = {pressure} bar
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # ==================================================
        # MODEL PERFORMANCE
        # ==================================================

        st.markdown(
            """
            <div class="result-card">

            <h3 style="
            color:#0B3C5D;
            ">
            Model Performance
            </h3>

            <h2>
            Train R² : 0.9980
            </h2>

            <h2>
            Test R² : 0.98460
            </h2>

            <p>
            XGBoost Regressor using Top 20 Random Forest Features
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # ==================================================
        # MOLECULE STRUCTURES
        # ==================================================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Cation")

            if cat_info["image"] is not None:
                 st.image(
                 cat_info["image"],
                use_container_width=True
    )

            st.metric(
                "Molecular Weight",
                f"{cat_info['molwt']:.2f}"
            )
            

        with col2:

            st.subheader("Anion")



            if an_info["image"] is not None:
                 st.image(
                 an_info["image"],
                 use_container_width=True
    )
            st.metric(
                "Molecular Weight",
                f"{an_info['molwt']:.2f}"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # ==================================================
        # FEATURE TABLE
        # ==================================================

        st.markdown(
            """
            <div class="section-title">
            Top 20 Features Used By Model
            </div>
            """,
            unsafe_allow_html=True
        )

        feature_display = feature_df.T

        feature_display.columns = ["Value"]

        st.dataframe(
            feature_display,
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )
