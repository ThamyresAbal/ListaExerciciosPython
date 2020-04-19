

#Modulo exec
'''os.execl( caminho , arg0 , arg1 , ... )
os.execle( caminho , arg0 , arg1 , ... , env )
os.execlp( arquivo , arg0 , arg1 , ... )
os.execlpe( arquivo , arg0 , arg1 , ... , env )
os.execv( caminho , args )
os.execve( caminho , args , env )
os.execvp( arquivo , args )
os.execvpe( arquivo , args , env )
Todas essas funções executam um novo programa, substituindo o processo atual; eles não retornam. No Unix, o novo executável é carregado no processo atual e terá o mesmo id do processo que o responsável pela chamada. Erros serão relatados como OSErrorexceções.

O processo atual é substituído imediatamente. Objetos de arquivos abertos e descritores não são liberados, portanto, se houver dados armazenados em buffer nesses arquivos abertos, você deve liberá-los usando sys.stdout.flush()ou os.fsync()antes de chamar uma exec*função.

As variantes “l” e “v” das exec*funções diferem em como os argumentos da linha de comando são passados. As variantes "l" são, talvez, as mais fáceis de se trabalhar se o número de parâmetros for corrigido quando o código é escrito; os parâmetros individuais tornam-se simplesmente parâmetros adicionais para as execl*() funções. As variantes "v" são boas quando o número de parâmetros é variável, com os argumentos sendo passados ​​em uma lista ou tupla como o parâmetro args . Em ambos os casos, os argumentos para o processo filho devem começar com o nome do comando que está sendo executado, mas isso não é imposto.

As variantes que incluem um “P” próximo do fim ( execlp(), execlpe(), execvp(), e execvpe()) vai usar o PATHvariável de ambiente para localizar o arquivo do programa . Quando o ambiente está sendo substituído (usando uma das exec*evariantes, discutidas no próximo parágrafo), o novo ambiente é usado como a origem doPATHvariável. As outras variantes, execl(), execle(), execv(), e execve(), se não utilizar oPATHvariável para localizar o executável; O caminho deve conter um caminho absoluto ou relativo apropriado.

Por execle(), execlpe(), execve(), e execvpe()(note que todos estes terminam em “e”), o env parâmetro deve ser um mapeamento que é usado para definir as variáveis de ambiente para o novo processo (estes são usados em vez do atual processo ambiente); as funções execl(), execlp(), execv()e execvp()tudo fazer com que o novo processo de herdar o ambiente do processo atual.

Em execve()algumas plataformas, o caminho também pode ser especificado como um descritor de arquivo aberto. Esta funcionalidade pode não ser suportada na sua plataforma; Você pode verificar se está ou não disponível usando os.supports_fd. Se não estiver disponível, o uso aumentará a NotImplementedError.

Disponibilidade : Unix, Windows.

Novo na versão 3.3: Adicionado suporte para especificar um descritor de arquivo aberto para caminho para execve().

Alterado na versão 3.6: Aceita um objeto semelhante a um caminho .'''

#Modulo spawn

'''os.spawnl( modo , caminho , ... ) 
os.spawnle( modo , caminho , ... , env ) 
os.spawnlp( modo , arquivo , ... ) 
os.spawnlpe( mode , file , ... , env ) 
os.spawnv( modo , caminho , args ) 
os.spawnve( modo , caminho , args , env ) 
os.spawnvp( modo , arquivo , args ) 
os.spawnvpe( mode , file , args , env ) 
Execute o caminho do programa em um novo processo.

(Observe que o subprocessmódulo oferece recursos mais poderosos para gerar novos processos e recuperar seus resultados; é preferível usar esse módulo para usar essas funções. Verifique especialmente a seção Substituição de funções mais antigas com o módulo Subprocess .)

Se mode for P_NOWAIT, esta função retorna o id do processo do novo processo; se mode estiver P_WAIT, retorna o código de saída do processo se ele sair normalmente ou -signal, onde signal é o sinal que matou o processo. No Windows, o ID do processo será realmente o identificador do processo, portanto, pode ser usado com a waitpid()função.

As variantes “l” e “v” das spawn*funções diferem em como os argumentos da linha de comando são passados. As variantes "l" são, talvez, as mais fáceis de se trabalhar se o número de parâmetros for corrigido quando o código é escrito; os parâmetros individuais tornam-se simplesmente parâmetros adicionais para as spawnl*()funções. As variantes "v" são boas quando o número de parâmetros é variável, com os argumentos sendo passados ​​em uma lista ou tupla como o parâmetro args . Em ambos os casos, os argumentos para o processo filho devem começar com o nome do comando que está sendo executado.

As variantes que incluem um segundo “P” próximo do fim ( spawnlp(), spawnlpe(), spawnvp(), e spawnvpe()) vai usar o PATHvariável de ambiente para localizar o arquivo do programa . Quando o ambiente está sendo substituído (usando uma das spawn*evariantes, discutidas no próximo parágrafo), o novo ambiente é usado como a origem doPATHvariável. As outras variantes, spawnl(), spawnle(), spawnv(), e spawnve(), se não utilizar o PATHvariável para localizar o executável; O caminho deve conter um caminho absoluto ou relativo apropriado.

Por spawnle(), spawnlpe(), spawnve(), e spawnvpe() (note que todos estes terminam em “e”), o env parâmetro deve ser um mapeamento que é usado para definir as variáveis de ambiente para o novo processo (eles são usados em vez do atual processo ambiente); as funções spawnl(), spawnlp(), spawnv()e spawnvp()tudo fazer com que o novo processo de herdar o ambiente do processo atual. Observe que as chaves e valores no dicionário de env devem ser strings; chaves ou valores inválidos farão com que a função falhe, com um valor de retorno de 127.

Como exemplo, as seguintes chamadas para spawnlp()e spawnvpe()são equivalentes:'''