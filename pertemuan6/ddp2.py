jumlah_angka = 10  # Ganti sama angka yg mau di masukin
jumlah = 0
deret_angka = []

for i in range(1, jumlah_angka * 2, 2):
    deret_angka.append(i)
    jumlah += i

deret_teks = ' + '.join(map(str, deret_angka))
print(f"{deret_teks} = {jumlah}")