def hitung_miring(a, b):
    hipotenusa = (a**2 + b**2)**0.5
    return hipotenusa

# Contoh penggunaan
sisi_a = float(input("Masukkan panjang sisi a: "))
sisi_b = float(input("Masukkan panjang sisi b: "))

hasil_miring = hitung_miring(sisi_a, sisi_b)

print(f"Panjang sisi miring (hipotenusa): {hasil_miring}")
