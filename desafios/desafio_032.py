# from datetime import date
"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
"""

num = int(input("Descubra se um ano é bissexto: \n"))

if num % 4 == 0:
    str_num = str(num)
    if str_num[-2:] == "00":  
        if num % 400 == 0:
            print(f'{num} é bissexto.')
        else:
            print(f'{num} não é bissexto.')
    else:
        print(f'{num} é bissexto.')
else:
    print(f'{num} não é bissexto.')
