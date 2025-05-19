# atama_toplama_çıkarma_operators.py
# Python Temel Operatörler: Atama, Toplama ve Çıkarma
# Bu dosya, Python dilindeki temel operatörleri anlamanızı sağlayacaktır.

# 1. Atama Operatörü (=)

# Atama operatörü (=), bir değişkene değer atamak için kullanılır.
# Bu operatör, sağdaki değeri solundaki değişkene atar.

x = 10  # x değişkenine 10 değeri atandı
y = 5   # y değişkenine 5 değeri atandı

# Şimdi, x ve y değişkenlerinin değerlerini yazdıralım
print("x'in değeri:", x)  # Çıktı: x'in değeri: 10
print("y'nin değeri:", y)  # Çıktı: y'nin değeri: 5

# 2. Toplama Operatörü (+)

# Toplama operatörü (+), iki sayıyı toplamak için kullanılır.
# Aynı zamanda, iki metni birleştirmek için de kullanılabilir.

# Sayı toplama
toplam = x + y  # x ve y'yi topladık
print("Toplam (x + y):", toplam)  # Çıktı: 15

# Metin birleştirme
isim = "Ahmet"
soyisim = "Yılmaz"
tam_isim = isim + " " + soyisim  # isim ve soyisim'i birleştirdik
print("Tam isim:", tam_isim)  # Çıktı: Tam isim: Ahmet Yılmaz

# 3. Çıkarma Operatörü (-)

# Çıkarma operatörü (-), bir sayıyı diğerinden çıkarmak için kullanılır.
# Aynı şekilde, sayılarla yapılan işlemler üzerinde de kullanılır.

fark = x - y  # x'den y'yi çıkardık
print("Fark (x - y):", fark)  # Çıktı: 5

# Hatalara Dikkat!
# Python'da toplama ve çıkarma işlemleri yalnızca uygun veri türleri üzerinde yapılabilir.
# Örneğin, bir sayıyı bir metinle toplamak hata verir:

# Hatalı örnek:
# print("Sayı: " + 10)  # Bu satır hata verecektir çünkü 10 bir sayıdır, bir metinle toplanamaz.
