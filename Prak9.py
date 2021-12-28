# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 20:43:31 2021
@author: Abdullah
"""


# ELEMEN KOMPETENSI 1
def reverse(list):
    return tuple(i for i in list)


list_abdul = [5, 10, 7, 4, 15, 3]
print("List:", list_abdul, "\n" + "Hasil reverse list menjadi tuple:", reverse(list_abdul))
