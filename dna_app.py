import streamlit as st
import io
import sys
import builtins
import base64
from dna_core import seq_analiza
from dna_core import seq_cleaner

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

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stMainBlockContainer"] {
    background-color: rgba(255,255,255,0.85);
    box-shadow: 0px 0px 30px rgba(0,0,0,0.3);
}
[data-testid="stMainBlockContainer"] * {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Default: light panel */
[data-testid="stMainBlockContainer"] {
    background-color: rgba(255,255,255,0.85);
}
[data-testid="stMainBlockContainer"] * {
    color: black !important;
}

/* Dark mode adaptive */
@media (prefers-color-scheme: dark) {
  [data-testid="stMainBlockContainer"] {
    background-color: rgba(30,30,30,0.85);
  }
  [data-testid="stMainBlockContainer"] * {
    color: white !important;
  }
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
# DNA Analyzer
***Alat za analizu i konverziju DNK sekvence***
 
Laboratorija za Molekularnu biologiju

Departman za Biologiju i Ekologiju

Prirodno-matematički fakultet

Univerzitet u Nišu
""")

st.markdown("""
<style>
label {
    margin-bottom: 0.1rem !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("***Uneti sekvencu u fasta ili raw formatu:***")
seq_input = st.text_area("", height=120)

if seq_input:
    seq_input = seq_cleaner(seq_input)
    st.markdown("**Prečišćena sekvenca:**")
    st.code(seq_input.upper())


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

