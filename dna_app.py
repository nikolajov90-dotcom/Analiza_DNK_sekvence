import streamlit as st
import io
import sys
import builtins
import base64
from dna_core import seq_analiza
# Učitavanje pozadine
def set_bg(img_file):
    with open(img_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("background.jpg")

st.markdown("""
<style>

/* Pozadina aplikacije */
[data-testid="stAppViewContainer"] {
    background: transparent;
}

/* Glavni content panel */
[data-testid="stMainBlockContainer"] {
    background-color: rgba(255,255,255,0.85);
    padding: 2rem;
    border-radius: 20px;
}

/* Sidebar (ako postoji) */
[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.9);
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
# DNA Analyzer
 
**Osnovi bioinformatike - Departman za Biologiju i Ekologiju**

**Prirodno-matematički fakultet, Univezitet u Nišu**

""")

st.write("Alat za analizu i konverziju DNK sekvence")

# input polja
seq_input = st.text_input("Unesite raw DNK sekvencu (bez FASTA zaglavlja i razmaka):")


if st.button("Analiziraj"):

    # simulacija input() poziva
    inputs = iter([seq_input])

    def fake_input(prompt=""):
        return next(inputs)

    # patch input()
    old_input = builtins.input
    builtins.input = fake_input

    # hvatanje print output-a
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    try:
        seq_analiza()
    except StopIteration:
        pass

    # restore input/print
    builtins.input = old_input
    sys.stdout = old_stdout

    st.text(buffer.getvalue())

