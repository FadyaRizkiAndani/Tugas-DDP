ket='''silahkan pilih rumus luas di bawah ini
silahkan pilih
se'1'
1.untuk menghitung luas persegi
2.untuk menghitung luas lingkaran
3.untuk menghitung luas segitiga
'''

pilihan = input(ket)
match pilihan:
   case '1':
      print ('memilih rumus 1 untuk menghitung luas persegi')
      sisi = int(input("masukan sisi?"))
      luas = sisi * sisi
      print ('luas persegi yang sisinya',sisi,'adalah',luas)
   case '2':
      print ('memilih rumus 2 untuk menghitung luas lingkaran')
      jari2 = float(input("masukan sisi?"))
      luas = 3.14 * jari2 * jari2
      print ("luas lingkaran yang jari2nya")
   case '3':
      print ('memilih rumus 3 untuk menghitung luas segitiga')
      alas = int(input('masukan alas?'))
      tinggi= int(input("masukan tinggi?"))
      luas=0.5 * alas * tinggi
      print ("luas segitiga yang alasnya", alas, "tinggi", tinggi, "adalah", luas)
   case _ :
       print ("salah memilih pilihan")

       