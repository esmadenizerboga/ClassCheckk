import qrcode

# Lokal Django form sayfasının URL'si
url = "http://127.0.0.1:8000/"

# QR kodu oluştur
qr = qrcode.make("http://192.168.192.73/")  # senin IP adresin neyse onu yaz

# Dosya olarak kaydet
qr.save("ogrenci_form_qr.png")

print("QR kodu oluşturuldu ve ogrenci_form_qr.png olarak kaydedildi.")
