
import os

arquivo = input('Digite o nome de algum executável na área de trabalho')
print(arquivo)
os.system("notepad "+arquivo+".txt")

#Obs: o arquivo precisa estar na mesma pasta
