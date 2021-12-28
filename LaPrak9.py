# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 20:43:31 2021
@author: Abdullah
"""


# ELEMEN KOMPETENSI 1
def elkom1(list):
    return tuple(i for i in list)


list_abdul = [5, 10, 7, 4, 15, 3]
print("List:", list_abdul, "\n" + "Hasil reverse list menjadi tuple:", elkom1(list_abdul))


# ELEMEN KOMPETENSI 2
def elkom2(tuple_abdul):
    print("Tuple1:\n" + str(tuple_abdul) + "\n")
    return [sum(i) / len(i) for i in zip(*tuple_abdul)]


print("Rerata nilai pada masing-masing tuple:\n" + str(
    elkom2(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))))


# ELEMEN KOMPETENSI 3
def elkom3(list_abdul):
    hasil = 1
    for x in list_abdul:
        hasil = hasil * x
    print("List:", list_abdul)
    print("Hasil kali value list:", hasil)


elkom3([5, 3, -8])

# ELEMEN KOMPETENSI 4
memenuhi = 0


def elkom4(list_abdul):
    print("List string:", str(list_abdul))
    global memenuhi
    for indeks in list_abdul:
        awal = indeks[0]
        akhir = indeks[len(indeks) - 1]

        if awal == akhir:
            print("-", indeks)
            memenuhi += 1


elkom4(['abc', 'xyz', 'cac', '54325', ])
print("Terdapat {} string yang memenuhi kriteria".format(memenuhi))
