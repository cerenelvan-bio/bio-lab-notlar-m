# PCR mastermix hesaplayici
ornek_sayisi = int(input("Ornek sayisi: "))
kisi_basi = 25  # uL
toplam = ornek_sayisi * kisi_basi * 1.1  # %10 fazla
print(f"Hazirlanacak toplam mix: {toplam:.1f} uL")
