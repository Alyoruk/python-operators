# ----------------------------------------
# Atama, Toplama ve Çıkarma Operatörleri
# ----------------------------------------

# Bu dosya, Python'da kullanılan üç temel operatörü açıklar:
# 1. Atama (=)
# 2. Toplama (+)
# 3. Çıkarma (-)

# ----------------------------------------
# 1️⃣ Atama Operatörü (=)
# ----------------------------------------

# '=' operatörü, bir değeri bir değişkene atamak için kullanılır.
# Sağdaki değer, soldaki değişkene yerleştirilir.

x = 10          # x değişkenine 10 değeri atanır
isim = "Ali"    # isim değişkenine "Ali" stringi atanır

print("x:", x)          # Çıktı: x: 10
print("isim:", isim)    # Çıktı: isim: Ali

# ----------------------------------------
# 2️⃣ Toplama Operatörü (+)
# ----------------------------------------

# '+' operatörü, sayılar arasında toplama yapar.
a = 5
b = 3
toplam = a + b  # 5 + 3 = 8
print("Toplam (sayı):", toplam)  # Çıktı: 8

# '+' operatörü, metin (string) değerleri birleştirir.
ad = "Ali"
soyad = "Can"
tam_isim = ad + " " + soyad  # "Ali" + " " + "Can" = "Ali Can"
print("Tam isim:", tam_isim)  # Çıktı: Ali Can

# ----------------------------------------
# 3️⃣ Çıkarma Operatörü (-)
# ----------------------------------------

# '-' operatörü, sayılar arasında çıkarma yapar.
x = 10
y = 4
fark = x - y  # 10 - 4 = 6
print("Fark:", fark)  # Çıktı: 6

# ❗ Not: '-' operatörü stringlerde kullanılamaz. Aşağıdaki satır hata verir:
# hata = "Ali" - "A"  # TypeError: unsupported operand type(s) for -: 'str' and 'str'

# ----------------------------------------
# Örnek: Üç Operatörün Birlikte Kullanımı
# ----------------------------------------

sayi1 = 20
sayi2 = 8

toplam = sayi1 + sayi2       # 28
fark = sayi1 - sayi2         # 12
sonuc = toplam               # toplam değişkeninin değeri sonuc'a atanır

print("Toplam:", toplam)     # Çıktı: 28
print("Fark:", fark)         # Çıktı: 12
print("Sonuç:", sonuc)       # Çıktı: 28

# ----------------------------------------
# Özet:
# '=' → Atama operatörü: sağdaki değeri soldaki değişkene aktarır.
# '+' → Sayıları toplar, metinleri birleştirir.
# '-' → Sayılardan birini diğerinden çıkarır.
