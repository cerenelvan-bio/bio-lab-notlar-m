# Basit GC orani hesaplayici
dna = input("DNA dizisini gir: ").upper()
gc = dna.count("G") + dna.count("C")
oran = (gc / len(dna)) * 100
print(f"Uzunluk: {len(dna)}")
print(f"GC orani: %{oran:.1f}")
