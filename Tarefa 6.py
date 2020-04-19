
import os

lista = os.listdir('C:\\Users\\Matheus\\Desktop\\psp')
print(lista)

for x in lista:
    lista = os.path.getsize('C:\\Users\\Matheus\\Desktop\\psp\\' + x)
    total = lista / 1024
    print(total, 'KB')

