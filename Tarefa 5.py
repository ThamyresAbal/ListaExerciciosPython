
import os
pasta = input("digite um nome da pasta que vc deseja procurar : ")
if os.path.exists(pasta):
    print("a pasta", pasta, 'existe!')
else:
    print("a pasta", pasta, 'não existe!')