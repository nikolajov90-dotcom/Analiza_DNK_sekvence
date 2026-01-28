def gc_sadrzaj(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100

def dnk_u_rnk(seq):
    return seq.replace("T", "U")

def complement(seq):
    comp = {"A":"T","T":"A","G":"C","C":"G"}
    return "".join(comp[b] for b in seq)

def reverse(seq):
    return seq[::-1]

def reverse_complement(seq):
    return reverse(complement(seq))


def seq_analiza():
    c = "da"

    while c.lower() == "da":
        try:
            seq = input("Unesite sekvencu DNK: ").upper()

            # validacija
            for baza in seq:
                if baza not in "ATGC":
                    raise ValueError(f"Neadekvatan simbol u sekvenci: {baza}")

            print(f"Ukupna dužina sekvence: {len(seq)}")
            print(f"GC sadržaj sekvence DNK iznosi {gc_sadrzaj(seq):.2f} %")
            print(f"Sekvenca RNK: {dnk_u_rnk(seq)}")
            print(f"Sekvenca komplementarne DNK: {complement(seq)}")
            print(f"Sekvenca reverse DNK: {reverse(seq)}")
            print(f"Sekvenca reverse complement DNK: {reverse_complement(seq)}")

        except ValueError as e:
            print(f"Greška: {e}")
            print("Molim unesite sekvencu ponovo.")
            continue

