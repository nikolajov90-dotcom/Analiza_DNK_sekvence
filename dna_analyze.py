import tkinter as tk

# ==== tvoje funkcije ====

def gc_sadrzaj(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100

def complement(seq):
    comp = {"A":"T","T":"A","G":"C","C":"G"}
    return "".join(comp[b] for b in seq)

def reverse(seq):
    return seq[::-1]

def reverse_complement(seq):
    return reverse(complement(seq))

# ==== GUI funkcija ====

def analyze():
    seq = entry.get().upper()

    result = f"Dužina: {len(seq)}\n"
    result += f"GC: {gc_sadrzaj(seq):.2f} %\n"
    result += f"Complement: {complement(seq)}\n"
    result += f"Reverse: {reverse(seq)}\n"
    result += f"RevComp: {reverse_complement(seq)}\n"

    output.config(text=result)

# ==== GUI ====

root = tk.Tk()
root.title("DNA Analyzer")

tk.Label(root, text="Unesite DNK sekvencu:").pack()
entry = tk.Entry(root, width=60)
entry.pack()

tk.Button(root, text="Analiziraj", command=analyze).pack()

output = tk.Label(root, text="", justify="left")
output.pack()

root.mainloop()
