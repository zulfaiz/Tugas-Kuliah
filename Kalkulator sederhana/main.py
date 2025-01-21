def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    while True:
        print("\nKalkulator Sederhana")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        choice = input("Pilih operasi (1/2/3/4/5): ")

        if choice == "5":
            print("Keluar dari kalkulator. Terima kasih!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Masukkan angka pertama: "))
                num2 = float(input("Masukkan angka kedua: "))

                if choice == "1":
                    print(f"Hasil: {add(num1, num2)}")
                elif choice == "2":
                    print(f"Hasil: {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Hasil: {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Hasil: {divide(num1, num2)}")
            except ValueError:
                print("Error: Masukkan angka yang valid.")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")