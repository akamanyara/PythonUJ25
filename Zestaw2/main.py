# ZESTAW 2 - JAKUB PAWLUSEK

# ZADANIE 2.10
# Mamy dany string wielowierszowy line. Podać sposób obliczenia liczby wyrazów w stringu.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

line = "abc \n acbr\ndercty"
print(len(line.split()))

# ZADANIE 2.11
# Podać sposób wyświetlania stringu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

word = "slowo"
print("_".join(word))

# ZADANIE 2.12
# Zbudować string stworzony z pierwszych znaków wyrazów ze stringu line. 
# Zbudować napis stworzony z ostatnich znaków wyrazów ze stringu line.

first = "".join(word[0] for word in line.split())
last = "".join(word[-1] for word in line.split())
print(f"{first} {last}")

# ZADANIE 2.13
# Znaleźć łączną długość wyrazów w stringu line. Wskazówka: można skorzystać z funkcji sum().

total_lenght = sum( len(word) for word in line.split())
print(total_lenght)

# ZADANIE 2.14
# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w stringu line.

words = line.split()
longest_word = max(words, key=len)
print(f"(a)     {longest_word}")
print(f"(b)     {len(longest_word)}")

# ZADANIE 2.15
# Na liście L znajdują się liczby całkowite dodatnie. Stworzyć string będący ciągiem cyfr kolejnych liczb z listy L.

L = [1, 150, 4, 21, 8]
string = "".join(str(el) for el in L)
print(string)

# ZADANIE 2.16
# W tekście znajdującym się w stringu line zamienić ciąg znaków "GvR" na "Guido van Rossum".

line = "Python creator is GvR"
line = line.replace("GvR", "Guido van Rossum")
print(line)

# ZADANIE 2.17
# Posortować wyrazy ze stringu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().

words = line.split()
sorted_words = " ".join(sorted(words, key=str.lower)) # dodatkowy key=str.lower po to zeby sortowalo alfabetycznie ignorujac wielkosci liter
sorted_words_len = " ".join(sorted(words, key=len))
print(sorted_words)
print(sorted_words_len)


# ZADANIE 2.18
# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na string.

number = 310000130000100054000 # 14 zer 
counter = str(number).count("0")
print(counter)

# ZADANIE 2.19
# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. 
# Chcemy zbudować string z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, 
# np. 007, 024. Wskazówka: str.zfill().

L = [95, 7, 24, 356, 4, 132]
string = " ".join(str(el).zfill(3) for el in L)
print(string)