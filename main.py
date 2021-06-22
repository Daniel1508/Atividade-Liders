opcao = ''

while opcao != 'f':

  print('''
  [1] O que é um lider ?
  [2] Quais habilidades que um lider precisar ter ?
  [3] Quais as características que um lider precisa ter ?
  [4] Quais são os tipos de lideranças que existem ?
  [5] Que Comportamentos que um lider deve ter ?
  [F] Para Fechar o software.
  ''')

  opcao = input('O que você quer saber ? ').lower()
  
  if opcao == '1':
    print('O chefe se contenta com tarefas, mas o líder consegue entusiasmo,  interesse pelo trabalho e  cooperação. O líder deve liderar equipes de  trabalho para que consiga  comprometimento e motivação  em sua equipe.')

  elif opcao == '2':
    print('''Um lider precisar ter 3 tipos de Habilidades elas são:
    Habilidade Humana: Cooperação  com outras  pessoas.
    Habilidade Técnica: Método, Processo e Procedimento.
    Habilidade Conceitual: Conhecimento e Decições. 
     ''')

  elif opcao == '3':
    print('''Quando falamos de liderança, não basta apenas querer liderar. Para essa tarefa, são necessárias características um tanto quanto peculiares que precisam ser desenvolvidas. Geralmente, um bom líder possui as seguintes atributos:

    Dinâmico, Criativo, Carismático;
    Pró ativo, Ético, Comunicativo;
    Inspirador, Inovador, Abraçar desafios;
    Bom relacionamento, Intuitivo;
    Empático e Motivador.
    ''')

  elif opcao == '4':
    print('''
    Lider Autoritario
    Lider Democratico
    Lider Liberal
    ''')

  elif opcao == '5':
    print('''
    Empenho
    Motivação de liderança
    Integridade
    Autoconfiança
    Autocontrole
    Empatia
    Conhecimento do negócio 
    Enfrentar as tensões e conflitos
    ''')
  elif opcao == 'f':
    break
  else:
    print('ERRO, Por Favor escolha um numero das questões do menu.')
    
