# ZESTAW 3 - JAKUB PAWLUSEK
# W zadaniach budujemy całe napisy, a nie wyświetlamy po kawałku.

#========================
# ZADANIE 3.1
# Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?
#========================

#* 1. TAK, ale średniki i nawiasy są niepotrzebne
# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;

#! 2. NIE, poniewaz po for nowy blok instrukcji ( tutaj if ) musi być w nowej linii.
# for i in "axby": if ord(i) < 100: print (i)

#* 3. TAK, poniewaz tutaj jest wyrazenie warunkowe ( if jest w srodku wyrazenia print, a nie jest instrukcja po for: )
# for i in "axby": print (ord(i) if ord(i) < 100 else i)

#========================
# ZADANIE 3.2
# Co jest złego w kodzie:
#========================

# L = [3, 5, 4] ; L = L.sort()
# .sort() zwraca None. bo lista jest modyfikowana w miejscu, więc przypisanie niszczy listę
L = [3, 5, 4]
L.sort()
print(L)

# x, y = 1, 2, 3
# z lewej są 2 zmienne, z prawej 3 wartości
x, y, z = 1, 2, 3

# X = 1, 2, 3 ; X[1] = 4
# Tuple jest niemodyfikowalny więc pojawia się błąd
X = [1, 2, 3]
X[1] = 4

# X = [1, 2, 3] ; X[3] = 4
# Indeks 3 nie istnieje
X.append(4)

# X = "abc" ; X.append("d")
# Stringi nie mają metody append()
X = "abc" + "d"

# L = list(map(pow, range(8)))
# pow() wymaga 2 lub 3 argumentów (np. pow(a, b))
# np.
L = list(map(lambda x: pow(x, 2), range(8)))
print(L)

#========================
# ZADANIE 3.3
# Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3. Użyć pętli for lub while.
#========================

for i in range(31):
    if i % 3 != 0:
        print(i, end=" ")

#========================
# ZADANIE 3.4
# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x. 
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program
# ma wypisać komunikat o błędzie i kontynuować pracę.
#========================

while True:
    x = input("Give number (type 'stop' to stop): ")
    if x.lower() == "stop":
        break
    try:
        x = float(x)
        print(f"x = {x}, x^3 = {x ** 3}")
    except ValueError:
        print(f"Error: {x} is not a number")

#========================
# ZADANIE 3.5
# Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się 
# z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

# |....|....|....|....|....|....|....|....|....|....|....|....|
# 0    1    2    3    4    5    6    7    8    9   10   11   12
#========================

def measure(lenght):
    top = "|"
    for _ in range(lenght):
        top += "....|"
    numbers = "0"
    for i in range(1, lenght + 1):
        numbers += str(i).rjust(5)
    return top + "\n" + numbers

print(measure(12))

#========================
# ZADANIE 3.6
# Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. 
# Przykładowy prostokąt składający się 2 × 4 pól ma postać:

# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   | 
# +---+---+---+---+
#========================

def rectangle(height, width):
    level = "+---" * width + "+\n"
    vert = "|   " * width + "|\n"
    result = ""
    for _ in range(height):
        result += level + vert
    result += level
    return result

print(rectangle(2, 4))


#========================
# ZADANIE 3.8
# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
#========================

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = list(set(a) & set(b))
all_unique = list(set(a) | set(b))

print("Wspólne:", common)
print("Wszystkie:", all_unique)

#========================
# ZADANIE 3.9
# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. 
# Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], 
# spodziewany wynik [0,4,3,7,18].
#========================

seq = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
sums = [sum(s) for s in seq]
print(sums)

#========================
# ZADANIE 3.10
# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie 
# (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
#========================

roman_dict1 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

roman_dict2 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
roman_dict3 = dict(zip(['I','V','X','L','C','D','M'], [1,5,10,50,100,500,1000]))

def roman2int(roman):
    roman = roman.upper()
    values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    prev = 0
    for ch in reversed(roman):
        value = values[ch]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total

print(roman2int("XIV"))   # 14
print(roman2int("MCMXCIV"))  # 1994