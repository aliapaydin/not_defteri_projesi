def kayit_ol(kullanici_adi, sifre):
    # Kullanıcıyı kaydetmek için kullanılır
    with open("kullanicilar.txt", "a") as dosya:
        dosya.write(f"{kullanici_adi}:{sifre}\n")
    print(f"{kullanici_adi} adlı kullanıcı başarıyla kaydedildi.")

def oturum_ac(kullanici_adi, sifre):
    # Kullanıcının oturum açmasını sağlamak için kullanılır
    with open("kullanicilar.txt", "r") as dosya:
        kullanicilar = dosya.readlines()
    
    for kullanici in kullanicilar:
        ad, parola = kullanici.strip().split(":")
        if ad == kullanici_adi and parola == sifre:
            print(f"{kullanici_adi} adlı kullanıcı oturum açtı.")
            return True

    print("Oturum açma başarısız. Kullanıcı adı veya şifre yanlış.")
    return False

def oturumu_kapat():
    # Oturumu kapamak için kullanılır
    print("Oturum kapatıldı.")

def kullanici_kontrol():
    # Kullanıcının oturum açmış olup olmadığını kontrol etmek için kullanılır
    # Burada oturum durumu basitçe bir değişkenle (örneğin, oturum_acildi_mi) simüle ediliyor.
    oturum_acildi_mi = False

    if oturum_acildi_mi:
        print("Kullanıcı oturum açmış durumda.")
    else:
        print("Kullanıcı oturum açmamış durumda.")

    return oturum_acildi_mi