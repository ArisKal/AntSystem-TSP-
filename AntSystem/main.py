from AntSystem.ReadData import ReadData
from AntSystem.Colony import Colony
from AntSystem.ReadATT import ReadAtt
import time


def main():
    # Testing graph
    # graph = np.array([[0, 3, 6, 2, 3], [3, 0, 5, 2, 3], [6, 5, 0, 6, 4], [2, 2, 6, 0, 6], [3, 3, 4, 6, 0]])
    try:
        # file = ReadAtt("../data/berlin52.xml")
        read_data = ReadData("../data/gr17.xml")
        graph = read_data.get_cost_matrix()
        # graph = file.get_cost_matrix()
        start_time = time.time()
        colony = Colony(dimension=len(graph), a_graph=graph, number_of_ants=17, alpha=5, beta=1, evaporation_rate=0.1,
                        number_of_cycles=1000)
        colony.run()
        end_time = time.time()
        print("Parameters:")
        print("Number of ants:", colony.get_number_of_ants())
        print("alpha", colony.get_alpha())
        print("beta", colony.get_beta())
        print("evaporation_rate", colony.get_evaporation_rate())
        print("Minimum length:", colony.get_min_length(), ":", colony.get_shortest_tour())
        print("time:", end_time - start_time)
    except FileNotFoundError:
        print("FILE NOT FOUND!")


if __name__ == "__main__":
    main()
