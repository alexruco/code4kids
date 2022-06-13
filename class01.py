from time import sleep
from datetime import datetime
import os
clear = lambda: os.system("clear")
#do stuff
now = datetime.now()

current_time = now.strftime("%H:%M:%S")


print('Olá Mundo! \n\nMeu nome é Mary, eu sou um programa de computador.\n')
yourname = input('Como você se chama?\n\n')
clear() #clear stuff

print('\nOi '+ yourname + '!\n\nVou lhe fazer um convite.\n')
print('Vamos aprender a escrever código?\n')
print('Se aceita o convite, digite 1')
print('Se não aceita o convite, digite 2\n')

for x in range(6):
  letslearn = int(input('Aceita o convite?\n'))
  if letslearn == 1:
    inp = "\nEntão vamos lá!\n"
    break
  elif letslearn == 2:
    inp = "Deixa para a próxima, não tem problema!\n"
    break
else:
    inp = "Deixa para a próxima, não tem problema!\n"

clear() #clear stuff
print(inp)

if letslearn == 1:

  print('\nNa aula de hoje, vamos aprender uma palavrinha nova:\n\nVARIÁVEL.\n')
  
  keep = input('Pressione ENTER\n')

  clear() #clear stuff

  print('\nAntes de tudo, o que é uma variável? \n\nÉ como se fosse uma resposta a uma pergunta. \n\nEssa pergunta pode ter uma resposta diferente dependendo da pessoa, da hora, do lugar...como o valor pode variar, daí o nome: VARIÁVEL!\n')
  
  keep = input('Pressione ENTER\n')

  clear() #clear stuff

  print('Sua idade, seu nome (que eu já sei que é '+yourname+', o lugar onde você mora, seu prato preferido...e todas as outras coisas que tenham ou não a ver com você, são variáveis.\n')
  
  keep = input('Pressione ENTER\n')
  
  clear() #clear stuff

  print('Cada variável têm um nome e, normalmente, tem também um valor.\n')
  
  
  keep = input('Pressione ENTER\n')

  clear() #clear stuff
  print('Por exemplo. Podemos ter uma variável chamada HORÁRIO\n')
  
  
  print('Vamos ver qual poderia ser o valor dessa variável\n')
  
  keep = input('Pressione ENTER\n')

  clear() #clear stuff

  print('O valor dessa variável poderia ser por exemplo: ' + current_time+'\n\n')

  keep = input('Pressione ENTER\n')

  clear() #clear stuff
  print('Em programação podemos escrever algo assim:\n')

  print('HoraAtual = ' + current_time)

  keep = input('\nPressione ENTER\n')

  clear() #clear stuff
  print('Agora vamos brincar com as variáveis\n')

  keep = input('Pressione ENTER\n')

  clear() #clear stuff

  print('Proponho uma variável para o nosso PRATO PREDILETO. O valor vai ser o nome do seu prato preferido, OK?\nVamos lá!\n')

  prato = input('Qual o seu prato predileto?\n')

  print('\n\nDelicia! \nEm programação, poderíamos escrever assim:\n\n')

  
  print('PratoPredileto = ' + prato+'\n')

  keep = input('Pressione ENTER\n')

  clear() #clear stuff
  print('Agora vamos inverter. Você define a variável e eu digo o valor\n')

  nomevariavel = input('Como vai chamar a sua variável? (Não vale nome feiooo!!!!)\n\nEscreva o nome da sua variável:\n\n\n')

  valorvariavel = '123'
  print('\nVou definir um valor para a variável '+nomevariavel+': ' + valorvariavel + ' (lembrando que as variáveis podem ter valor texto, número, data e outros tipos).')

  keep = input('Pressione ENTER\n')

  clear() #clear stuff
  print('Em programação podemos escrever assim:\n\n')

  print(nomevariavel +'='+valorvariavel)

  
  print('\nGostou? Te vejo na próxima aula!')
