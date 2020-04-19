
import os

lista = os.listdir('C:\\Users\\Matheus\\Desktop\\psp')
print(lista)
print('Data criação e alteração em segundos')
for x in lista:
    listaC = os.path.getctime('C:\\Users\\Matheus\\Desktop\\psp\\' + x)
    listaA = os.path.getmtime('C:\\Users\\Matheus\\Desktop\\psp\\' + x)

    print(listaC)
    print(listaA)
    print('---------------------')