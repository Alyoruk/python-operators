# ===========================
# Çarpma, Bölme ve Karşılaştırma Operatörleri
# Multiplication, Division and Comparison Operators
# ===========================

# Bu dosyada Python'da çarpma (*), bölme (/), tam bölme (//),
# modül (%) ve karşılaştırma operatörlerini öğreneceğiz.
# In this file, we will learn multiplication (*), division (/), integer division (//),
# modulus (%) and comparison operators in Python.

# -----------------------------------
# Çarpma Operatörü: *
# Multiplication Operator: *
# İki sayıyı çarpmak için kullanılır.
# Used to multiply two numbers.

a = 4
b = 5
carpim = a * b
print("Çarpma:", carpim)  # Çıktı: 20 / Output: 20

# -----------------------------------
# Bölme Operatörü: /
# Division Operator: /
# İki sayıyı böler ve ondalıklı (float) sonuç verir.
# Divides two numbers and returns a float result.

x = 10
y = 4
bolme = x / y
print("Bölme:", bolme)  # Çıktı: 2.5 / Output: 2.5

# -----------------------------------
# Tam Sayı Bölme Operatörü: //
# Integer Division Operator: //
# İki sayıyı böler ama sadece tam sayı kısmını verir.
# Divides two numbers and returns only the integer part.

tam_bolum = x // y
print("Tam Sayı Bölme:", tam_bolum)  # Çıktı: 2 / Output: 2

# -----------------------------------
# Modül (Kalan) Operatörü: %
# Modulus (Remainder) Operator: %
# Bölme işleminden kalanı verir.
# Returns the remainder after division.

kalan = x % y
print("Kalan (modül):", kalan)  # Çıktı: 2 / Output: 2

# -----------------------------------
# Karşılaştırma Operatörleri
# Comparison Operators
# Bu operatörler iki değeri karşılaştırır ve True/False döner.
# These operators compare two values and return True or False.

sayi1 = 7
sayi2 = 5

print("Eşit mi? :", sayi1 == sayi2)         # False
print("Equal? :", sayi1 == sayi2)           # False

print("Eşit değil mi? :", sayi1 != sayi2)   # True
print("Not equal? :", sayi1 != sayi2)       # True

print("Büyük mü? :", sayi1 > sayi2)         # True
print("Greater than? :", sayi1 > sayi2)     # True

print("Küçük mü? :", sayi1 < sayi2)         # False
print("Less than? :", sayi1 < sayi2)        # False

print("Büyük veya eşit mi? :", sayi1 >= sayi2)   # True
print("Greater or equal? :", sayi1 >= sayi2)     # True

print("Küçük veya eşit mi? :", sayi1 <= sayi2)   # False
print("Less or equal? :", sayi1 <= sayi2)        # False

# -----------------------------------
# Uygulamalı örnek
# Practical example

a = 8
b = 4

print("a * b =", a * b)      # 32
print("a / b =",
