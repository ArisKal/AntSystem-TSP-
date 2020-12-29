from AntSystem.ReadData import ReadData
from AntSystem.Colony import Colony
from AntSystem.ReadATT import ReadAtt
import time
import numpy as np


def main():

    read_data = ReadData("../data/ulysses16.xml")
    data = read_data.get_tree()
    dimension = ReadData.get_dimension(data)
    graph = ReadData.create_graph(data, dimension)
    # np.around(graph)
    # colony = Colony(dimension, a_graph, number_of_ants, alpha, beta, evaporation_rate, number_of_cycles)
    graph = np.array([[0, 3, 6, 2, 3], [3, 0, 5, 2, 3], [6, 5, 0, 6, 4], [2, 2, 6, 0, 6], [3, 3, 4, 6, 0]])


    # print(read_data.get_name_of_file())
    # print(graph)
    # try:
    #     read = ReadAtt("../data/oliver30.tsp")
    #     f = read.get_file()
    # except:
    #     FileNotFoundError
    #     print("FILE NOT FOUND!")
    #
    # read.set_data(f)
    # data = read.get_data()
    # graph = ReadAtt.get_cost_matrix(data)
    # np.round(graph)
    start_time = time.time()
    colony = Colony(len(graph), graph, 1, 0.7, 0.7, 0.5, 1)
    colony.run()
    end_time = time.time()
    print("Parameters:")
    print("Number of ants:", colony.get_number_of_ants())
    print("alpha", colony.get_alpha())
    print("beta", colony.get_beta())
    print("evaporation_rate", colony.get_evaporation_rate())
    print("Minimum length:", colony.get_min_length(), ":",  colony.get_shortest_tour())
    print("time:", end_time - start_time)

if __name__ == "__main__":
    main()
