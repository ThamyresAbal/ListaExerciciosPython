

'''O método os.listdir() retorna uma lista contendo os nomes dos arquivos e diretórios encontrados, o que pode estar acontecendo é que você deve estar utilizando o método os.path.abspath() apontando para
 a lista devolvida de os.listdir() de modo errado, aplicando os.path.abspath() para cada item da lista deverá funcionar.
'''

import os

dirlist = os.listdir(".")
for i in dirlist:
    filename = os.path.abspath(i)
    print(filename)