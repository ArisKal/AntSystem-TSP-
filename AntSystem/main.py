from AntSystem.ReadData import ReadData
from AntSystem.Colony import Colony


def main():
    read_data = ReadData("../data/gr17.xml")
    data = read_data.get_tree()
    dimension = ReadData.get_dimension(data)
    graph = ReadData.create_graph(data, dimension)
    # colony = Colony(dimension, a_graph, number_of_ants, alpha, beta, evaporation_rate, number_of_cycles)
    print(read_data.get_name_of_file())
    colony = Colony(dimension, graph, 16, 1, 1, 0.99, 3000)
    colony.run()

if __name__ == "__main__":
    main()