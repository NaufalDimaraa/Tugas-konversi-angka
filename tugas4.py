angka_input = input("Masukkan angka: ")

try:
    angka = int(angka_input)
    print("Angka Desimal:", angka)

    angkabiner = angka
    biner = ""
    for _ in range(angka.bit_length()):
        sisa = angkabiner % 2
        biner = str(sisa) + biner
        angkabiner //= 2
    print("Angka Biner:", biner)

    oktal_angka = angka
    oktal = ""
    for _ in range(angka.bit_length()):
        sisa = oktal_angka % 8
        oktal = str(sisa) + oktal
        oktal_angka //= 8
    print("Angka Oktal:", oktal)

    heksadesimal_angka = angka
    heksa_digit = "0123456789ABCDEF"
    heksadesimal = ""  
    for _ in range(angka.bit_length()):
        sisa = heksadesimal_angka % 16
        heksadesimal = heksa_digit[sisa] + heksadesimal
        heksadesimal_angka //= 16
    print("Angka Heksadesimal:", heksadesimal)

except ValueError:
    print("Masukkan bukan angka yang valid.")