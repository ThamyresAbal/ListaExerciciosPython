

# Método OS jeito 1
#Ele cria um processo para o programa da calculadora nativa do Windows. Na segunda linha, o nome do arquivo executável com o caminho (path) desde a raiz é gerado através de os.environ.
import os
import subprocess
executavel_com_path = os.environ['SYSTEMROOT'] + '\\System32\\calc.exe'
os.spawnl(os.P_NOWAIT, executavel_com_path, " ")



# Método subprocess jeito 2
#Abaixo, um exemplo que chama o programa notepad (bloco de notas) do Windows para abrir um arquivo chamado “arq_texto.txt”.
print(subprocess.run(["notepad", "teste.txt"]))