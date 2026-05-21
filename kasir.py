produk = {
    1: {"nama": "Indomie", "harga": 3000},
    2: {"nama": "Aqua", "harga": 5000},
    3: {"nama": "Teh Botol", "harga": 4000},
    4: {"nama": "Beras 10kg", "harga": 120000},
    5: {"nama": "Gula 1kg", "harga": 15000},
    6: {"nama": "Minyak Goreng 1L", "harga": 18000},
    7: {"nama": "Telur 1kg", "harga": 28000},
    8: {"nama": "Susu Ultra", "harga": 7000},
    9: {"nama": "Roti Tawar", "harga": 12000},
    10: {"nama": "Kopi Sachet", "harga": 2000},
    11: {"nama": "Sabun Mandi", "harga": 5000},
    12: {"nama": "Shampoo", "harga": 10000},
    13: {"nama": "Pasta Gigi", "harga": 8000},
    14: {"nama": "Biskuit", "harga": 9000},
    15: {"nama": "Coklat", "harga": 12000},
    16: {"nama": "Air Galon", "harga": 20000},
    17: {"nama": "Mie Cup", "harga": 6000},
    18: {"nama": "Sarden", "harga": 10000},
    19: {"nama": "Kecap", "harga": 11000},
    20: {"nama": "Saos", "harga": 9000}
}

keranjang = []
total = 0

print("=== KASIR SEDERHANA ===")

while True:
    print("\nDaftar Produk:")
    for id, item in produk.items():
        print(f"{id}. {item['nama']} - Rp {item['harga']}")

    try:
        pilih = int(input("\nPilih produk (0 untuk selesai): "))
    except ValueError:
        print("Input harus angka!")
        continue

    if pilih == 0:
        break

    if pilih not in produk:
        print("Produk tidak ada!")
        continue

    try:
        jumlah = int(input("Jumlah: "))
    except ValueError:
        print("Jumlah harus angka!")
        continue

    nama = produk[pilih]["nama"]
    harga = produk[pilih]["harga"]
    subtotal = harga * jumlah

    keranjang.append((nama, jumlah, subtotal))
    total += subtotal

print("\n=== STRUK BELANJA ===")
for item in keranjang:
    print(f"{item[0]} x{item[1]} = Rp {item[2]}")

print(f"\nTotal: Rp {total}")

try:
    bayar = int(input("Uang bayar: Rp "))
    kembalian = bayar - total

    if kembalian < 0:
        print("Uang tidak cukup!")
    else:
        print(f"Kembalian: Rp {kembalian}")
except ValueError:
    print("Input harus angka!")

print("Terima kasih!")