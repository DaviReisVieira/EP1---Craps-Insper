from random import randint

fichas_iniciais = 1000

Game_on = True
ContinuaOp = False
SomaDadosPlb = 0
PlbAposta = 0
FAposta = 0
AcAposta = 0
TAposta = 0
fase = 1

def print_dado(valor_dado):  
  if valor_dado == 1:
    print (" ------- ")
    print ("|       |") 
    print ("|   *   |")
    print ("|       |")
    print (" ------- ")
  elif valor_dado == 2:
    print (" ------- ")
    print ("| *     |") 
    print ("|       |")
    print ("|     * |")
    print (" ------- ")
  elif valor_dado == 3:
    print (" ------- ")
    print ("| *     |") 
    print ("|   *   |")
    print ("|     * |")
    print (" ------- ")
  elif valor_dado == 4:
    print (" ------- ")
    print ("| *   * |") 
    print ("|       |")
    print ("| *   * |")
    print (" ------- ")
  elif valor_dado == 5:
    print (" ------- ")
    print ("| *   * |") 
    print ("|   *   |")
    print ("| *   * |")
    print (" ------- ") 
  elif valor_dado == 6:
    print (" ------- ")
    print ("| *   * |") 
    print ("| *   * |")
    print ("| *   * |")
    print (" ------- ")

def jogar_dados():
  valor_dado = randint(1, 6)
  print_dado(valor_dado)
  return valor_dado

def PainelApostas(PlbAposta,FAposta,AcAposta,TAposta):
    print("\n------------Apostas Realizadas:------------")
    if PlbAposta>0:
      print("-Pass Line Bat: {0} Fichas" .format(str(PlbAposta)))
    if FAposta>0:
      print("-Field: {0} Fichas" .format(str(FAposta)))
    if AcAposta>0:
      print("-Any Craps: {0} Fichas" .format(str(AcAposta)))
    if TAposta>0:
      print("-Twelve: {0} Fichas" .format(str(TAposta)))
    print("---------------------------------------------")
    print("Fichas em Mão: {0} Fichas" .format(str(fichas_iniciais)))
    print("Fichas em Aposta: {0} Fichas" .format(str(PlbAposta+FAposta+AcAposta+TAposta)))

print("")
print(" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.")
print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
print("| |     ______   | || |  _______     | || |      __      | || |   ______     | || |    _______   | |")
print("| |   .' ___  |  | || | |_   __ \    | || |     /  \     | || |  |_   __ \   | || |   /  ___  |  | |")
print("| |  / .'   \_|  | || |   | |__| |   | || |    / /\ \    | || |    | |__| |  | || |  |  |__ \_|  | |")
print("| |  | |         | || |   |  __ /    | || |   / ____ \   | || |    |  ___/   | || |   '.___`-.   | |")
print("| |  \ `.___.'\  | || |  _| |  \ \_  | || | _/ /    \ \_ | || |   _| |_      | || |  |`\____| |  | |")
print("| |   `._____.'  | || | |____| |___| | || ||____|  |____|| || |  |_____|     | || |  |_______.'  | |")
print("| |              | || |              | || |              | || |              | || |              | |")
print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")
print("")

while Game_on:
  if fase == 1:
    print("Iniciando o Come Out! Fichas: {}" .format(fichas_iniciais))
  if fase == 2:
    print("Iniciando o Point! Fichas: {}" .format(fichas_iniciais))

  RespostaApostar = str(input("\nDeseja realizar uma aposta?[s|n]\nSua escolha: "))
  
  if RespostaApostar == 'n':
    Confirmacao = input("Deseja REALMENTE sair do jogo?[s|n]\nSua escolha: ")
    if Confirmacao == 's':
      print("\nVocê desistiu do jogo com {0} Fichas." .format(str(fichas_iniciais)))
      break
    if Confirmacao == 'n':
      RespostaApostarW = True
  elif RespostaApostar == 's':
    RespostaApostarW = True
  else:
    print("Escolha uma opção.")       
  
  while RespostaApostarW:
    if fase == 1:
      EscolherAposta = str(input("\nEscolha uma aposta: Pass Line Bet[plb]| Field(f)| Any Craps[ac]| Twelve[t]| Sair[x]\nSua escolha: "))
      while True:
        if EscolherAposta == 'plb' or EscolherAposta == 'f' or EscolherAposta == 'ac' or EscolherAposta == 't' or EscolherAposta == 'x':
          break
    if fase == 2:
      EscolherAposta = str(input("\nEscolha uma aposta: Field(f)| Any Craps[ac]| Twelve[t]| Cancelar[c] \nSua escolha: "))
      while True:
        if EscolherAposta == 'f' or EscolherAposta == 'ac' or EscolherAposta == 't' or EscolherAposta == 'c':
          break
    
    if fichas_iniciais == 0 and SomaDadosPlb ==0:
      print('\nJogador Expulso da Mesa por falta de Fichas!')
      Game_on = False 
      RespostaApostarW = False
      break

    while True:
      if EscolherAposta != 'c' and EscolherAposta != 'x':
        ValorAposta = int(input("\nDigite o valor da Aposta:\nValor: "))
        if ValorAposta > fichas_iniciais:
          print("\nVocê não tem Fichas suficientes para realizar esta aposta.\n\nNúmero de Fichas disponíveis: {0}" .format(fichas_iniciais))
        else:
          fichas_iniciais-=ValorAposta
          break
      else:
        break

    if EscolherAposta == 'plb':
      PlbAposta+=ValorAposta
    elif EscolherAposta == 'f':
      FAposta+=ValorAposta
    elif EscolherAposta == 'ac':
      AcAposta+=ValorAposta
    elif EscolherAposta == 't':
      TAposta+=ValorAposta
    elif EscolherAposta == 'x':
      Confirmacao = input("Deseja REALMENTE sair do jogo?[s|n]\nSua escolha: ")
      if Confirmacao == 's':
        print("\nVocê desistiu do jogo com {0} Fichas." .format(str(fichas_iniciais)))
        RespostaApostarW = False
        Game_on = False
        break
      if Confirmacao == 'n':
        RespostaApostarW = True

    if PlbAposta + FAposta + AcAposta + TAposta > 0:
      PainelApostas(PlbAposta,FAposta,AcAposta,TAposta)
      ProseguirAposta = input("\nGostaria de realizar mais alguma aposta?[s|n]\nSua escolha: ")
      if ProseguirAposta == 's':
        ContinuaOp = False
      if ProseguirAposta == 'n':
        ContinuaOp = True
    
    if ContinuaOp:
      print("Dados rolando...")
      Dado1 = jogar_dados()
      Dado2 = jogar_dados()
      SomaDados = Dado1+Dado2
      print("\nSoma: {0}" .format(SomaDados))
      if PlbAposta > 0:
        if fase == 1:
          if SomaDados == 7 or SomaDados == 11: #Win no Pass Line Bet
            fichas_iniciais+= 2*PlbAposta
            print("\nParabéns! Você ganhou {0} Fichas no Pass Line Bat!\n\nNúmero de Fichas disponíveis: {1}" .format(str(PlbAposta), str(fichas_iniciais)))
            PlbAposta = 0
          elif SomaDados == 2 or SomaDados == 3 or SomaDados == 12: #Craps
            print("\nVocê perdeu {0} Fichas no Pass Line Bat.\n\nNúmero de Fichas disponíveis: {1}" .format(str(PlbAposta), str(fichas_iniciais)))
            PlbAposta = 0
          elif SomaDados == 4 or SomaDados == 5 or SomaDados == 6 or SomaDados == 8 or SomaDados == 9 or SomaDados == 10:
            print("\nO Point foi iniciado! Fichas apostadas: {0}.\n\nNúmero de Fichas disponíveis: {1} " .format(str(PlbAposta), str(fichas_iniciais)))
            fase = 2
            SomaDadosPlb = SomaDados
        elif fase == 2:
          if SomaDadosPlb == SomaDados:
            fichas_iniciais+= 2*PlbAposta
            print("\nParabéns! Você ganhou {0} Fichas no Pass Line Bat!\n\nNúmero de Fichas disponíveis: {1}" .format(str(PlbAposta), str(fichas_iniciais)))
            fase = 1
            PlbAposta = 0
            SomaDadosPlb = 0
          elif SomaDados == 7:
            print("\nVocê perdeu {0} Fichas no Pass Line Bat.\n\nNúmero de Fichas disponíveis: {1}" .format(str(PlbAposta), str(fichas_iniciais)))
            PlbAposta = 0
            fase = 1
            PlbAposta = 0
            SomaDadosPlb = 0
          else:
            print("\nO Pass Line Bat continua na fase Point com {0} Fichas." .format(str(PlbAposta)))
      
      if FAposta > 0:
        if SomaDados == 5 or SomaDados == 6 or SomaDados == 7 or SomaDados ==8:
          print("\nVocê perdeu {0} Fichas no Field.\n\nNúmero de Fichas disponíveis: {1}" .format(str(FAposta), str(fichas_iniciais)))
        elif SomaDados == 3 or SomaDados == 4 or SomaDados == 9 or SomaDados ==10 or SomaDados ==11:
          fichas_iniciais+= 2*FAposta
          print("\nParabéns! Você ganhou {0} Fichas no Field!\n\nNúmero de Fichas disponíveis: {1}" .format(str(FAposta), str(fichas_iniciais)))
        elif SomaDados == 2:
          fichas_iniciais+= 3*FAposta
          print("\nParabéns! Você ganhou {0} Fichas no Field!\n\nNúmero de Fichas disponíveis: {1}" .format(str(FAposta), str(fichas_iniciais)))
        elif SomaDados == 12:
          fichas_iniciais+= 4*FAposta
          print("\nParabéns! Você ganhou {0} Fichas no Field!\n\nNúmero de Fichas disponíveis: {1}" .format(str(FAposta), str(fichas_iniciais)))
        FAposta = 0
      
      if AcAposta > 0:
        if SomaDados == 2 or SomaDados == 3 or SomaDados == 12:
          fichas_iniciais+= 8*AcAposta
          print("\nParabéns! Você ganhou {0} Fichas no Any Craps!\n\nNúmero de Fichas disponíveis: {1}" .format(str(AcAposta), str(fichas_iniciais)))
        else:
          print("\nVocê perdeu {0} Fichas no Any Craps.\n\nNúmero de Fichas disponíveis: {1}" .format(str(AcAposta), str(fichas_iniciais)))
        AcAposta = 0
      
      if TAposta > 0:
        if SomaDados == 12:
          fichas_iniciais+= 31*TAposta
          print("\nParabéns! Você ganhou {0} Fichas no Twelve!\n\nNúmero de Fichas disponíveis: {1}" .format(str(TAposta), str(fichas_iniciais)))
        else:
          print("\nVocê perdeu {0} Fichas no Twelve.\n\nNúmero de Fichas disponíveis: {1}" .format(str(TAposta), str(fichas_iniciais)))
        TAposta = 0   
      ContinuaOp = False 

