def pola_sakit_kepala(panjang, lebar):
    if panjang == lebar:
        if panjang % 2 != 0 and lebar % 2 != 0: 
            tengah = panjang / 2
            for i in range(panjang, 0, -1):
                for j in range(panjang, 0 , -1):
                    if i == int(tengah+1):
                        print(j)
        else:
            print("Harus bilangan negatif")
    else:
        print("Panjang harus sama")



pola_sakit_kepala(7,7)
