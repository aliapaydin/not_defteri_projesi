def not_ekle(baslik, icerik):
    # Yeni bir not eklemek için kullanılır
    with open("notlar.txt", "a") as dosya:
        dosya.write(f"{baslik}: {icerik}\n")
        print("Not başarıyla eklenmiştir.")

def notlari_listele():
    # Tüm notları listelemek için kullanılır
    with open("notlar.txt", "r") as dosya:
        notlar = dosya.readlines()
    if notlar:
        for i, not_satiri in enumerate(notlar, start=1):
            print(f"ID: {i}\n{not_satiri}")
    else:
        print("Henüz hiç not eklenmemiş.")

def not_goruntule(not_id):
    # Belirli bir notu görüntülemek için kullanılır
    with open("notlar.txt", "r") as dosya:
        notlar = dosya.readlines()
    if not 1 <= not_id <= len(notlar):
        print("Geçersiz not ID.")
    else:
        print(f"Not ID {not_id}:\n{notlar[not_id - 1]}")

def not_duzenle(not_id, yeni_icerik):
    # Bir notu düzenlemek için kullanılır
    with open("notlar.txt", "r") as dosya:
        notlar = dosya.readlines()
    if not 1 <= not_id <= len(notlar):
        print("Geçersiz not ID.")
    else:
        notlar[not_id - 1] = yeni_icerik + "\n"
        with open("notlar.txt", "w") as dosya:
            dosya.writelines(notlar)

def not_sil(not_id):
    # Bir notu silmek için kullanılır
    with open("notlar.txt", "r") as dosya:
        notlar = dosya.readlines()
    if not 1 <= not_id <= len(notlar):
        print("Geçersiz not ID.")
    else:
        silinecek_not = notlar.pop(not_id - 1)
        with open("notlar.txt", "w") as dosya:
            dosya.writelines(notlar)
        print(f"Aşağıdaki not silindi:\n{silinecek_not}")