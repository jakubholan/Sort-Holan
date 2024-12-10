import random

#1. Vytvořte pole s 10 přeházenými hodnotami od 0-100.
array = random.sample(range(101), 10)
print("Původní pole:", array)

#2. Vytvořte bubble sort.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #Provádí výměnu
    return arr

#3. Vytvořte bogo sort.
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]: #Pokudbude prvek větší než následující
            return False
    return True

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr) #Přehazuje
    return arr

#4. Vytvořte selection sort.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j #Nachází minimální hodnoty
        arr[i], arr[min_idx] = arr[min_idx], arr[i] #Vyměňuje
    return arr

#5. Vytvořte Insertion sort.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j] #Posun hodnot
            j -= 1
        arr[j+1] = key #Vložení klíče
    return arr

#Tetsování algoritmů
print("Seřazené pole pomocí Bubblesort:", bubble_sort(array.copy()))
print("Seřazené pole pomocí Bogosort:", bogo_sort(array.copy()))
print("Seřazené pole pomocí Selectionsort:", selection_sort(array.copy()))
print("Seřazené pole pomocí Insertionsort:", insertion_sort(array.copy()))
