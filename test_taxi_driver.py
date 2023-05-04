from Solver import Solver
from datetime import datetime


# =-=-=-=-=-=-=- Testes do Handout

mapa_1 = [[0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

mapa_2 = [[0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

mapa_3 = [[0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 1, 1, 0],
          [0, 1, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0]]

mapa_4 = [[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0]]

mapa_5 = [[0, 0, 0, 1, 0, 0, 0, 1],
          [0, 0, 0, 1, 0, 0, 0, 1],
          [0, 0, 0, 1, 0, 0, 0, 1],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0, 0]]

def test_mapa1():
    print('mapa 1')
    inicio = datetime.now()
    state = Solver.solve(mapa=mapa_1, pos_taxi=(0, 0), pos_passenger=(0, 5), pos_destination=(4, 0), is_full=False)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; direita ; direita ; baixo ; baixo ; baixo ; direita ; direita ; direita ; cima ; cima ; cima ; pick ; esquerda ; baixo ; baixo ; baixo ; esquerda ; esquerda ; esquerda ; esquerda ; baixo ; drop"
    assert state.g == 30

def test_mapa2():
    print('mapa 2')
    inicio = datetime.now()
    state = Solver.solve(mapa_2, (3, 5), (3, 5), (4, 0), True)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; baixo ; drop"
    assert state.g == 11

def test_mapa3():
    print('mapa 3')
    inicio = datetime.now()
    state = Solver.solve(mapa_3, (0, 0), (0, 4), (4, 0), False)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; direita ; direita ; baixo ; baixo ; baixo ; direita ; direita ; direita ; direita ; cima ; cima ; esquerda ; esquerda ; cima ; pick ; baixo ; direita ; direita ; baixo ; baixo ; esquerda ; esquerda ; esquerda ; esquerda ; cima ; esquerda ; esquerda ; baixo ; baixo ; drop"
    assert state.g == 38

def test_mapa4():
    print('mapa 4')
    inicio = datetime.now()
    state = Solver.solve(mapa_4, (1, 2), (7, 0), (7, 2), False)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; esquerda ; esquerda ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; pick ; cima ; cima ; cima ; cima ; cima ; direita ; direita ; baixo ; baixo ; baixo ; baixo ; baixo ; drop"
    assert state.g == 30

def test_mapa5():
    print('mapa 5')
    inicio = datetime.now()
    state = Solver.solve(mapa_5, (6, 0), (7, 4), (7, 6), False)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; cima ; cima ; cima ; cima ; direita ; direita ; baixo ; direita ; direita ; baixo ; baixo ; baixo ; baixo ; pick ; cima ; cima ; cima ; cima ; cima ; direita ; direita ; baixo ; baixo ; baixo ; baixo ; baixo ; drop"
    assert state.g == 35


# -=-=-=-=-=-=-=- Testes Impossíveis

mapa_unsolvable_1 = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

mapa_unsolvable_2 = [[0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0]]

mapa_unsolvable_3 = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0]]

def test_unsolvable1():
    # Passangeiro não é alcançável
    print('unsolvable 1')
    inicio = datetime.now()
    state = Solver.solve(mapa_unsolvable_1, (0, 0), (2, 2), (0, 4), False)
    fim = datetime.now()
    print(fim - inicio)
    assert state == None

def test_unsolvable2():
    # Taxi está preso
    print('unsolvable 2')
    inicio = datetime.now()
    state = Solver.solve(mapa_unsolvable_2, (2, 2), (0,0), (0, 4), False)
    fim = datetime.now()
    print(fim - inicio)
    assert state == None

def test_unsolvable3():
    # Chegada não é alcançável
    print('unsolvable 3')
    inicio = datetime.now()
    state = Solver.solve(mapa_unsolvable_3, (0, 0), (0, 3), (4, 0), False)
    fim = datetime.now()
    print(fim - inicio)
    assert state == None

def test_unsolvable4():
    # Elemento fora do mapa
    print('unsolvable 4')
    inicio = datetime.now()
    state = Solver.solve(mapa_unsolvable_3, (0, 0), (0, 1), (6, 0), False)
    fim = datetime.now()
    print(fim - inicio)
    assert state == None


# -=-=-=-=-=-=-=- Testes Muito Grandes

mapa_10x10 = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def test_mapa10x10():
    print('mapa 10x10')
    inicio = datetime.now()
    state = Solver.solve(mapa_10x10, (0, 0), (0, 9), (9, 0), False)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; direita ; direita ; direita ; baixo ; baixo ; baixo ; baixo ; direita ; direita ; direita ; cima ; cima ; cima ; direita ; direita ; direita ; cima ; pick ; esquerda ; esquerda ; esquerda ; esquerda ; baixo ; baixo ; baixo ; baixo ; esquerda ; baixo ; baixo ; baixo ; baixo ; baixo ; esquerda ; esquerda ; esquerda ; esquerda ; drop"
    assert state.g == 45

mapa_10x10_2 = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

def test_mapa10x10_2():
    print('mapa 10x10 2')
    inicio = datetime.now()
    state = Solver.solve(mapa_10x10_2, (0, 0), (9, 9), (0, 9), False)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    print(r)
    assert r == " ; baixo ; direita ; baixo ; baixo ; baixo ; direita ; direita ; direita ; baixo ; baixo ; direita ; direita ; direita ; direita ; baixo ; baixo ; direita ; baixo ; pick ; cima ; esquerda ; cima ; cima ; cima ; cima ; cima ; direita ; cima ; cima ; cima ; drop"
    assert state.g == 39

mapa_25x25 = [[0 for i in range(25)] for j in range(25)]

def test_mapa25x25():
    print('mapa 25x25')
    inicio = datetime.now()
    state = Solver.solve(mapa_25x25, (0, 0), (0, 24), (24, 0), False)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; pick ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; drop"
    assert state.g == 82

mapa_50x50 = [[0 for i in range(50)] for j in range(50)]

def test_mapa50x50():
    print('mapa 50x50')
    inicio = datetime.now()
    state = Solver.solve(mapa_50x50, (0, 0), (49, 49), (49, 0), False)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; pick ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; drop"
    assert state.g == 157

mapa_100x100 = [[0 for i in range(100)] for j in range(100)]

def test_mapa100x100():
    print('mapa 100x100')
    inicio = datetime.now()
    state = Solver.solve(mapa_100x100, (0, 0), (99, 99), (99, 0), False)
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    print(r)
    assert r == " ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; direita ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; baixo ; pick ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; esquerda ; drop"
    assert state.g == 307


def test_custom():
    print('custom')

    # Open the file for reading
    with open("map.txt", "r") as file:

        # Read the contents of the file into a list of lines
        lines = file.readlines()

        # Initialize an empty list to store the matrix
        matrix = []

        # Loop over each line in the file
        map = True
        for i in range(len(lines)):
            
            if "END" in lines[i]:
                map = False
            
            if map:
                # Split the line into a list of values
                values = lines[i].split()

                # Convert each value to a float and append it to the matrix
                row = [int(value) for value in values]
                matrix.append(row)
            else:
                if "Taxi row" in lines[i]:
                    taxi_row = int(lines[i + 1])
                elif "Taxi column" in lines[i]:
                    taxi_column = int(lines[i + 1])
                elif "Passenger row" in lines[i]:
                    passenger_row = int(lines[i + 1])
                elif "Passenger column" in lines[i]:
                    passenger_column = int(lines[i + 1])
                elif "Destination row" in lines[i]:
                    destination_row = int(lines[i + 1])
                elif "Destination column" in lines[i]:
                    destination_column = int(lines[i + 1])
                elif "Max cost" in lines[i]:
                    max_cost = int(lines[i + 1])
    

    inicio = datetime.now()
    state = Solver.solve(matrix, (taxi_row, taxi_column), (passenger_row, passenger_column), (destination_row, destination_column), False)
    r = state.show_path()
    fim = datetime.now()
    
    if state == None:
        print("Não existe solução")
    elif state.g > max_cost:
        print("Custo maior do que o custo máximo da viagem")
    else:
        print(f'Tempo de execução em segundos: {fim - inicio}')
        print(f'Custo: {state.g}')
        print()
        print(f"Posição inicial do Taxi: {(taxi_row, taxi_column)}")
        print(f"Posição inicial do Passageiro: {(passenger_row, passenger_column)}")
        print(f"Posição do Destino: {(destination_row, destination_column)}")
        print()
        print("Mapa:")
        for i in range(len(matrix)):
            print(matrix[i])
        print()
        print("Caminho encontrado: ")
        print(r)

def bruteforce():
    print('força bruta')
    print('Tamanho do Mapa (Quadrado) | Tempo para achar a solução')
    i = 10
    mapa = [[0 for j in range(i)] for k in range(i)]
    inicio = datetime.now()
    state = Solver.solve(mapa, (0, 0), (i - 1, i - 1), (i - 1, 0), False)
    fim = datetime.now()
    print(f"{i} - {fim - inicio}")

    while (state != None):
        i += 10

        mapa = [[0 for j in range(i)] for k in range(i)]
        inicio = datetime.now()
        state = Solver.solve(mapa, (0, 0), (i - 1, i - 1), (i - 1, 0), False)
        fim = datetime.now()
        print(f"{i} - {fim - inicio}")

if __name__ == '__main__':
    test_custom()
