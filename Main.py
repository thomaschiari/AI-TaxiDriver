from Game import main
from test_taxi_driver import test_custom, bruteforce
from Solver import Solver
import time

if __name__ == '__main__':

    print("Taxi Problem")
    print("============")
    print("Selecione o modo de operação (1 - game / 2 - força bruta / 3 - modo txt / 4 - teste rápido):")
    try:
        modo = int(input())
    except ValueError:
        print("Valor inválido!")
        exit()
    
    while modo < 1 or modo > 4:
        print()
        print("Valor inválido!")
        print("Selecione o modo de operação (1 - game / 2 - força bruta / 3 - modo txt / 4 - teste rápido):")
        try:
            modo = int(input())
        except ValueError:
            print("Valor inválido!")
            exit()
    
    print()
    
    if modo == 1:
        main()
    elif modo == 2:
        bruteforce()
    elif modo == 3:
        test_custom()
    elif modo == 4:
        # MAPA: 1 significa ser obstáculo!
        map = [[0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0]]
        
        ts = time.time()
        result = Solver.solve(map, (0, 0), (0, 4), (4, 0), False)
        tf = time.time()

        if result != None:
            print('Tempo de processamento em segundos: ' + str(tf-ts))
            print('O custo da solucao eh: '+str(result.g))
            print()
            print(f"Posição inicial do Taxi: {(0, 0)}")
            print(f"Posição inicial do Passageiro: {(0, 4)}")
            print(f"Posição do Destino: {(4, 0)}")
            print()
            print("Mapa:")
            for i in range(len(map)):
                print(map[i])
            print()
            print("Caminho encontrado: ")
            print(result.show_path())
        else:
            print('Nao achou solucao')
