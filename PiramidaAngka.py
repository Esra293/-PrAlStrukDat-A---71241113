def piramida_angka(angka):
    for i in range(1, angka+1):
        for j in range(angka+1, 1, -1):
            print(i ,end = j * " ")
piramida_angka(3)

