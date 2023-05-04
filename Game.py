import tkinter as tk
from tkinter import messagebox
import pygame
from Solver import Solver
import time

class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.start_grid_button = tk.Button(self, text="Criar a Grade", command=self.create_grid)
        self.start_game_button = tk.Button(self, text="Começar a Simulação", command=self.start)

        self.grid_label = tk.Label(self, text="Marque os obstáculos no mapa da Grade:")
        
        self.size_lines_label = tk.Label(self, text="N° Linhas Grade:")
        self.size_lines_entry = tk.Entry(self)
        self.size_columns_label = tk.Label(self, text="N° Colunas Grade:")
        self.size_columns_entry = tk.Entry(self)

        self.taxi_line_label = tk.Label(self, text="Linha do Táxi:")
        self.taxi_line_entry = tk.Entry(self)
        self.taxi_column_label = tk.Label(self, text="Coluna do Táxi:")
        self.taxi_column_entry = tk.Entry(self)

        self.passenger_line_label = tk.Label(self, text="Linha do Passageiro:")
        self.passenger_line_entry = tk.Entry(self)
        self.passenger_column_label = tk.Label(self, text="Coluna do Passageiro:")
        self.passenger_column_entry = tk.Entry(self)

        self.destination_line_label = tk.Label(self, text="Linha do Destino:")
        self.destination_line_entry = tk.Entry(self)
        self.destination_column_label = tk.Label(self, text="Coluna do Destino:")
        self.destination_column_entry = tk.Entry(self)

        self.max_cost_label = tk.Label(self, text="Custo Máximo:")
        self.max_cost_entry = tk.Entry(self)
        
        self.size_lines_label.grid()
        self.size_lines_entry.grid()
        self.size_columns_label.grid()
        self.size_columns_entry.grid()
        self.taxi_line_label.grid()
        self.taxi_line_entry.grid()
        self.taxi_column_label.grid()
        self.taxi_column_entry.grid()
        self.passenger_line_label.grid()
        self.passenger_line_entry.grid()
        self.passenger_column_label.grid()
        self.passenger_column_entry.grid()
        self.destination_line_label.grid()
        self.destination_line_entry.grid()
        self.destination_column_label.grid()
        self.destination_column_entry.grid()
        self.max_cost_label.grid()
        self.max_cost_entry.grid()
        self.start_grid_button.grid()
    

    def create_grid(self):
        try:
            size = [int(self.size_lines_entry.get()), int(self.size_columns_entry.get())]
        except:
            size = [0, 0]
        self.grid = []
        for i in range(size[0]):
            row = []
            for j in range(size[1]):
                var = tk.IntVar()
                checkbox = tk.Checkbutton(self, variable=var)
                checkbox.grid(row=i+2, column=10+j)
                row.append(var)
            self.grid.append(row)

        self.start_game_button.grid()


    def start(self):
        size = (int(self.size_lines_entry.get()), int(self.size_columns_entry.get()))
        taxi = (int(self.taxi_line_entry.get()), int(self.taxi_column_entry.get()))
        passenger = (int(self.passenger_line_entry.get()), int(self.passenger_column_entry.get()))
        destination = (int(self.destination_line_entry.get()), int(self.destination_column_entry.get()))
        max_cost = int(self.max_cost_entry.get())

        if passenger[0] > size[0]-1 or passenger[1] > size[1]-1:
            print("Coordenadas do passageiro estão fora do limite!")
            popup = tk.messagebox.showerror("Erro", f"Coordenadas do passageiro estão fora do limite!")
            return

        if destination[0] > size[0]-1 or destination[1] > size[1]-1:
            print("Coordenadas do destino estão fora do limite!")
            popup = tk.messagebox.showerror("Erro", f"Coordenadas do destino estão fora do limite!")
            return

        if taxi[0] > size[0]-1 or taxi[1] > size[1]-1:
            print("Coordenadas do taxi estão fora do limite!")
            popup = tk.messagebox.showerror("Erro", f"Coordenadas do taxi estão fora do limite!")
            return

        selected = []
        for i in range(len(self.grid)):
            row = []
            for j in range(len(self.grid[i])):
                if self.grid[i][j].get() == 1:
                    row.append(1)
                else:
                    row.append(0)
            selected.append(row)

        if selected[taxi[0]][taxi[1]] == 1:
            print("Coordenadas iniciais do taxi estão em um obstáculo!")
            popup = tk.messagebox.showerror("Erro", f"Coordenadas iniciais do taxi estão em um obstáculo! Não é possível iniciar a rota.")
            return

        if selected[passenger[0]][passenger[1]] == 1:
            print("Coordenadas do passageiro estão em um obstáculo!")
            popup = tk.messagebox.showerror("Erro", f"Coordenadas do passageiro estão em um obstáculo! Não é possível calcular a rota.")
            return

        if selected[destination[0]][destination[1]] == 1:
            print("Coordenadas do destino estão em um obstáculo!")
            popup = tk.messagebox.showerror("Erro", f"Coordenadas do destino estão em um obstáculo! Não é possível calcular a rota.")
            return

        ts = time.time()
        result = Solver.solve(selected, taxi, passenger, destination, is_full=False if taxi != passenger else True)
        tf = time.time()

        if result is None:
            print("Não foi possível encontrar solução.")
            # Create error message on tkinter screen
            popup = tk.messagebox.showerror("Erro", f"Solução não foi encontrada pelo agente.")
            return

        if max_cost != None and result.g > max_cost:
            print("Custo máximo excedido pelo agente!")
            popup = tk.messagebox.showerror("Erro", f"Custo máximo excedido pelo agente! O custo encontrado pelo agente foi {result.g} e o custo máximo era {max_cost}.")
            return

        path = result.show_path().replace(" ", "").split(";")
        print('Tempo de processamento em segundos: ' + str(tf-ts))
        print('O custo da solucao eh: '+str(result.g))
        print()
        print(f"Posição inicial do Taxi: {(0, 0)}")
        print(f"Posição inicial do Passageiro: {(0, 4)}")
        print(f"Posição do Destino: {(4, 0)}")
        print()
        print("Mapa:")
        for i in range(len(selected)):
            print(selected[i])
        print()
        print("Caminho encontrado: ")
        print(result.show_path())

        popup = tk.messagebox.showinfo("Sucesso!", f"Solução encontrada pelo agente! O custo encontrado pelo agente foi {result.g}. O tempo de processamento foi {tf-ts:.5f} segundos. Clique em OK para visualizar o caminho.")

        cell_size = 40
        cell_margin = 5

        pygame.init()
        screen = pygame.display.set_mode((size[1]*(cell_margin + cell_size) + cell_margin, size[0]*(cell_margin + cell_size) + cell_margin))
        pygame.display.set_caption("Game")
        clock = pygame.time.Clock()
        done = False

        counter = 0
        pick = False
        font = pygame.font.SysFont('Arial', cell_margin * 3)
        while not done and counter < len(path):
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        counter += 1
                        click = True

            # processa posições de taxi, passageiro e destino
            if click and counter < len(path):
                if path[counter] == 'pick':
                    pick = True
                elif path[counter] == 'drop':
                    pick = False
                elif path[counter] == 'direita':
                    if pick:
                        passenger = (passenger[0], passenger[1] + 1)
                    taxi = (taxi[0], taxi[1] + 1)
                elif path[counter] == 'esquerda':
                    if pick:
                        passenger = (passenger[0], passenger[1] - 1)
                    taxi = (taxi[0], taxi[1] - 1)
                elif path[counter] == 'cima':
                    if pick:
                        passenger = (passenger[0] - 1, passenger[1])
                    taxi = (taxi[0] - 1, taxi[1])
                elif path[counter] == 'baixo':
                    if pick:
                        passenger = (passenger[0] + 1, passenger[1])
                    taxi = (taxi[0] + 1, taxi[1])


            screen.fill((0, 0, 0))

            # desenha o grid na tela
            self.draw_grid(screen, selected, size, cell_size, cell_margin)

            
            # desenha o destino na tela
            pygame.draw.rect(screen, (0, 255, 0), [(cell_margin+cell_size)*destination[1]+cell_margin, (cell_margin+cell_size)*destination[0]+cell_margin, cell_size, cell_size])

            # desenha um D na tela representando o destino
            text = font.render('D', True, (0, 0, 0))
            screen.blit(text, (destination[1]*(cell_margin + cell_size) + cell_size/2, destination[0]*(cell_margin + cell_size) + cell_size/2))

            if not pick:
                # desenha o passageiro na tela
                pygame.draw.rect(screen, (255, 0, 0), [(cell_margin+cell_size)*passenger[1]+cell_margin, (cell_margin+cell_size)*passenger[0]+cell_margin, cell_size, cell_size])
                # desenha um P na tela representando o passageiro
                text = font.render('P', True, (0, 0, 0))
                screen.blit(text, (passenger[1]*(cell_margin + cell_size) + cell_size/2, passenger[0]*(cell_margin + cell_size) + cell_size/2))

                # desenha o taxi na tela
                pygame.draw.rect(screen, (0, 0, 255), [(cell_margin+cell_size)*taxi[1]+cell_margin, (cell_margin+cell_size)*taxi[0]+cell_margin, cell_size, cell_size])
                # desenha um T na tela representando o taxi
                text = font.render('T', True, (0, 0, 0))
                screen.blit(text, (taxi[1]*(cell_margin + cell_size) + cell_size/2, taxi[0]*(cell_margin + cell_size) + cell_size/2))
            else:
                # desenha um retângulo para o táxi carregar o passageiro
                pygame.draw.rect(screen, (255, 0, 255), [(cell_margin+cell_size)*taxi[1]+cell_margin, (cell_margin+cell_size)*taxi[0]+cell_margin, cell_size, cell_size])

                # desenha um T + P na tela representando o taxi com o passageiro
                text = font.render('TP', True, (0, 0, 0))
                screen.blit(text, (taxi[1]*(cell_margin + cell_size) + cell_margin + cell_size/2 - cell_margin, taxi[0]*(cell_margin + cell_size) + cell_margin + cell_size/2 - cell_margin))

            pygame.display.update()

            clock.tick(60)
        
        pygame.quit()
    

    def draw_grid(self, screen, selection, grid_size, cell_size=40, cell_margin=5, WHITE=(255, 255, 255), GRAY=(128, 128, 128)):
        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                color = WHITE if selection[row][col] == 0 else GRAY
                pygame.draw.rect(screen, color, [(cell_margin+cell_size)*col+cell_margin, (cell_margin+cell_size)*row+cell_margin, cell_size, cell_size])


def main():
    root = tk.Tk()
    root.title("Taxi Driver Agent")
    root.geometry("720x640")
    app = Game(root)
    app.mainloop()

if __name__ == "__main__":
    main()