from Bio.SeqUtils import MeltingTemp as mt

def seq_cleaner(seq_fasta):
    seq = ""
    for line in seq_fasta.splitlines():
        line = line.strip()
        if line.startswith(">"):
            continue
        line = line.replace(" ","")
        seq += line
    return seq.upper()

def temp_topljenja(seq):
    return mt.Tm_NN(seq, Na=50, Mg=1.5)

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

def palindrome_detect(seq, min_len=4):
    n = len(seq)
    best_start = 0
    best_len = 0

    def is_comp(a, b):
        return (a == "A" and b == "T") or \
               (a == "T" and b == "A") or \
               (a == "G" and b == "C") or \
               (a == "C" and b == "G")

    for i in range(n):
        for left, right in [(i, i), (i, i+1)]:
            while left >= 0 and right < n and is_comp(seq[left], seq[right]):
                length = right - left + 1
                if length >= min_len and length > best_len:
                    best_start = left
                    best_len = length
                left -= 1
                right += 1

    if best_len > 0:
        best_end = best_start + best_len
        return {
            f"{best_start+1}:{best_end}": seq[best_start:best_end]
        }
    else:
        return {}

def seq_analiza():
    c = "da"

    while c.lower() == "da":
        try:
            seq = input("Unesite sekvencu DNK: ").upper()

            # validacija
            for baza in seq:
                if baza not in "ATGC":
                    raise ValueError(f"Neadekvatan simbol u sekvenci: {baza}")

            print(f"Dužina sekvence: {len(seq)} bp." )
            print(f"Temperatura topljenja (Tm): {temp_topljenja(seq):.2f} °C.")
            print(f"GC sadržaj sekvence DNK iznosi {gc_sadrzaj(seq):.2f} %.")
            print(f"Sekvenca RNK: {dnk_u_rnk(seq)}")
            print(f"Sekvenca komplementarne DNK: {complement(seq)}")
            print(f"Sekvenca reverse DNK: {reverse(seq)}")
            print(f"Sekvenca reverse complement DNK: {reverse_complement(seq)}")
            print(f"Najduža palindromska sekvenca: {palindrome_detect(seq, min_len=4)}")
            print("""

*Tm se izračunava pomoću Biopython biblioteke (v1.83) koristeći MeltingTemp.Tm_NN funkciju pri [Na⁺] = 50 mM i [MgCl₂] = 1,5 mM. Tm_NN model je validan prvenstveno za oligonukleotide (10-50 nt). Rezultat za duge sekvence je približan.

""")
        except ValueError as e:
            print(f"Greška: {e}")
            print("Molim unesite sekvencu ponovo.")
            continue

