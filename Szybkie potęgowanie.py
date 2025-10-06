# Autor: Jakub Piskorowski
# Data: 27.02.2025
# Program: Szybkie potęgowanie + wyszukiwanie binarne

# --- Funkcja: szybkie potęgowanie (iteracyjne)
def szybkie_potegowanie_iteracyjne(a, n):
    wynik = 1
    while n > 0:
        if n % 2 == 1:
            wynik *= a
        a *= a
        n //= 2
    return wynik

# --- Funkcja: szybkie potęgowanie (rekurencyjne)
def szybkie_potegowanie_rekurencyjne(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return szybkie_potegowanie_rekurencyjne(a * a, n // 2)
    else:
        return a * szybkie_potegowanie_rekurencyjne(a, n - 1)

# --- Funkcja: wyszukiwanie binarne
def wyszukiwanie_binarne(tablica, szukana):
    lewy = 0
    prawy = len(tablica) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if tablica[srodek] == szukana:
            return srodek
        elif tablica[srodek] < szukana:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1

# --- Główna część programu
def main():
    print("=== SZYBKIE POTĘGOWANIE ===")
    a = int(input("Podaj bazę (a): "))
    n = int(input("Podaj wykładnik (n): "))

    wynik_iter = szybkie_potegowanie_iteracyjne(a, n)
    wynik_rek = szybkie_potegowanie_rekurencyjne(a, n)

    print(f"Iteracyjne: {a}^{n} = {wynik_iter}")
    print(f"Rekurencyjne: {a}^{n} = {wynik_rek}")

    print("\n=== WYSZUKIWANIE BINARNE ===")
    tablica = [2, 4, 6, 8, 10, 12, 14, 16]
    print(f"Tablica: {tablica}")
    szukana = int(input("Podaj liczbę do wyszukania: "))

    indeks = wyszukiwanie_binarne(tablica, szukana)
    if indeks != -1:
        print(f"Liczba {szukana} znaleziona na indeksie {indeks}.")
    else:
        print(f"Liczba {szukana} nie została znaleziona.")

if __name__ == "__main__":
    main()
