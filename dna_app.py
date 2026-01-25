import streamlit as st
import io
import sys
import builtins

from dna_core import seq_analiza

st.markdown("""
# DNA Analyzer
 
**Osnovi bioinformatike - Departman za Biologiju i ekologiju**

**Prirodno-matematički fakultet Univeziteta u Nišu**

""")

st.write("Alat za analizu i konverziju DNK sekvence")

# input polja
seq_input = st.text_input("Unesite DNK sekvencu:")
nastavi = st.selectbox("Nastaviti?", ["da", "ne"])

if st.button("Analiziraj"):

    # simulacija input() poziva
    inputs = iter([seq_input, nastavi])

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

