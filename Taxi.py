from aigyminsper.search.Graph import State

import copy


class Taxi(State):

    def __init__(self, op, pos_taxi, pos_passenger, pos_destination, map, is_full=False):
        self.operator = op
        self.pos_taxi = pos_taxi
        self.pos_passenger = pos_passenger
        self.pos_destination = pos_destination
        self.map = map
        self.is_full = is_full


    def sucessors(self):
        sucessors = []

        if self.map[self.pos_taxi[0]][self.pos_taxi[1]] == 1:
            return []

        # CIMA
        if (self.pos_taxi[0] - 1) >= 0:
            if self.map[self.pos_taxi[0] - 1][self.pos_taxi[1]] != 1:
                new_pos_passenger = (self.pos_taxi[0] - 1, self.pos_taxi[1]) if self.is_full else copy.deepcopy(self.pos_passenger)
                sucessors.append(Taxi('cima', (self.pos_taxi[0] - 1, self.pos_taxi[1]), new_pos_passenger, self.pos_destination, self.map, self.is_full))

        # BAIXO
        if (self.pos_taxi[0] + 1) <= (len(self.map) - 1):
            if self.map[self.pos_taxi[0] + 1][self.pos_taxi[1]] != 1:
                new_pos_passenger = (self.pos_taxi[0] + 1, self.pos_taxi[1]) if self.is_full else copy.deepcopy(self.pos_passenger)
                sucessors.append(Taxi('baixo', (self.pos_taxi[0] + 1, self.pos_taxi[1]), new_pos_passenger, self.pos_destination, self.map, self.is_full))
        
        # ESQ
        if (self.pos_taxi[1] - 1) >= 0:
            if self.map[self.pos_taxi[0]][self.pos_taxi[1] - 1] != 1:
                new_pos_passenger = (self.pos_taxi[0], self.pos_taxi[1] - 1) if self.is_full else copy.deepcopy(self.pos_passenger)
                sucessors.append(Taxi('esquerda', (self.pos_taxi[0], self.pos_taxi[1] - 1), new_pos_passenger, self.pos_destination, self.map, self.is_full))
        
        # DIR
        if (self.pos_taxi[1] + 1) <= (len(self.map[0]) - 1):
            if self.map[self.pos_taxi[0]][self.pos_taxi[1] + 1] != 1:
                new_pos_passenger = (self.pos_taxi[0], self.pos_taxi[1] + 1) if self.is_full else copy.deepcopy(self.pos_passenger)
                sucessors.append(Taxi('direita', (self.pos_taxi[0], self.pos_taxi[1] + 1), new_pos_passenger, self.pos_destination, self.map, self.is_full))
        
        # PICK
        if self.pos_taxi == self.pos_passenger and not self.is_full:
            sucessors.append(Taxi('pick', self.pos_taxi, self.pos_passenger, self.pos_destination, self.map, True))
        
        # DROP
        if self.pos_taxi == self.pos_destination and self.is_full:
            sucessors.append(Taxi('drop', self.pos_taxi, self.pos_passenger, self.pos_destination, self.map, False))
        
        return sucessors


    def cost(self):
        if self.operator == 'pick' or self.operator == 'drop':
            return 5
        else:
            return 1


    def is_goal(self):
        return self.pos_passenger == self.pos_destination and not self.is_full


    def h(self):
        if self.is_full:
            return abs(self.pos_passenger[0] - self.pos_destination[0]) + abs(self.pos_passenger[1] - self.pos_destination[1])
        else:
            return abs(self.pos_taxi[0] - self.pos_passenger[0]) + abs(self.pos_taxi[1] - self.pos_passenger[1])

    def description(self):
        return "Taxi driver is a great movie"


    def env(self):
        return str(self.pos_taxi) + " - " + str(self.pos_passenger) + " - " + str(self.pos_destination) + " - " + str(self.is_full)