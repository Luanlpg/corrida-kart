import sys

from separador import create_pilot_obj
from core import FastAndFurious

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"
REVERSE = "\033[;7m"
BIN = REVERSE+'   '+RESET+'   '
BOUT ='   '+REVERSE+'   '+RESET

racing = FastAndFurious()

def first_menu():
    """
    Método de execução de menu.
    """
    try:
        def prt():
            """
            Menu principal.
            """
            print('\t\t\t--------------------------------------------------------')
            print('\t\t\t-------------------- '+RED+'FAST & FURIOUS'+RESET+' --------------------')
            print('\t\t\t--------------------------------------------------------')
            print('\t\t\t--------- '+RED+'1'+RESET+' - '+BLUE+'Exibir resultados da corrida.'+RESET+' ------------')
            print('\t\t\t-------------- '+RED+'2'+RESET+' - '+BLUE+'Dados individuais.'+RESET+' ------------------')
            print('\t\t\t--------- '+RED+'Ctrl+C'+RESET+' - '+BLUE+'Para sair do programa.'+RESET+' --------------')
            print('\t\t\t--------------------------------------------------------')
            return '\t\t\t--------------------------------------------------------'
        # chamo o metodo prt()
        print(prt())
        # armazeno a entrada do usuario na variável opt
        opt = input(CYAN+'\t\t\t>>>'+RESET)
        classificacao, top_times = racing.race_posix()
        pilot = create_pilot_obj()
        media = racing.average_speed()
        diff = racing.difference()
        # caso a entrada seja igual a 1...
        if opt == '1':
            # mostro o panorama da corrida
            print(BIN*17)
            print(BOUT*17)
            print(BIN*17)
            print(BOUT*17)

            print(
                REVERSE+'    Posição     Código    Nome                Voltas          Tempo Total             Atraso          '+RESET
                )
            for i in range(len(classificacao)):
                obj = pilot[classificacao[i][0]]
                space = ' '*(20-len(obj["nome"]))
                print(
                    f'      #{i+1}\t{obj["cod"]}       {obj["nome"]+space}\t '\
                    f'{classificacao[i][1]}\t\t{classificacao[i][2]}\t'\
                    f'{diff[i][1]}'
                )
            print(REVERSE+f'\t\t\t\tMelhor tempo : {top_times[0][0]} - {top_times[0][1]}'+RESET)
            print(BIN*17)
            print(BOUT*17)
            print(BIN*17)
            print(BOUT*17)
            return first_menu()
        # caso a opção seja 2
        elif opt == '2':
            # mostro o painel de números individuais
            print(BIN*17)
            print(BOUT*17)
            print(BIN*17)
            print(BOUT*17)

            print(
                REVERSE+'    Nome              Posição      Tempo Total             Melhor Volta        Velocidade Média      '+RESET
                )
            for i in range(len(classificacao)):
                obj = pilot[classificacao[i][0]]
                space = ' '*(20-len(obj["nome"]))
                print(
                    f'   {obj["nome"]+space}\t {i+1}\t'\
                    f'{classificacao[i][2]}\t\t{top_times[i][1]}\t'\
                    f'\t{media[i][1]}'
                )
            print(BIN*17)
            print(BOUT*17)
            print(BIN*17)
            print(BOUT*17)

            return first_menu()
        else:
            print('\t\t\t------------------'+RED+'ENTRADA INVALIDA!!!'+RESET+'-------------------')
            # chamo o menu principal novamente
            return first_menu()
    except KeyboardInterrupt:
        print('---------------------'+RED+'FIM!!!'+RESET+'------------------------')
        sys.exit()
    return 'issae'

first_menu()
