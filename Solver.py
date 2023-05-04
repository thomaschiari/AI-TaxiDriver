from Taxi import Taxi
from aigyminsper.search.SearchAlgorithms import *

class Solver():

    @staticmethod
    def solve(mapa, pos_taxi, pos_passenger, pos_destination, is_full=False):
        state = Taxi('', pos_taxi=pos_taxi, pos_passenger=pos_passenger, pos_destination=pos_destination, map=mapa, is_full=is_full)
        #A* considera tanto heurística quanto custo, portanto, é perfeito para a situação!
        algorithm = AEstrela()
        
        result = algorithm.search(state)

        return result