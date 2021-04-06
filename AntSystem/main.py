import sys;
print("PATH", sys.path)
sys.path.extend(['/home/runner/work/AntSystem-TSP-/AntSystem-TSP-/AntSystem'])
from AntSystem.ReadData import ReadData
from AntSystem.Colony import Colony


def main():
    read_data = ReadData("../data/ulysses16.xml")
    data = read_data.get_tree()
    dimension = ReadData.get_dimension(data)
    graph = ReadData.create_graph(data, dimension)
    colony = Colony(dimension=dimension, a_graph=graph, number_of_ants=16, alpha=1, beta=6, evaporation_rate=0.9,
                    number_of_cycles=700)
    print("WAITING....")
    colony.run()
    print("Name of file:", read_data.get_name_of_file())
    print("Number of ants:", colony.get_number_of_ants())
    print("Alpha:", colony.get_alpha())
    print("Beta:", colony.get_beta())
    print("Evaporation rate:", colony.get_evaporation_rate())
    print("Number of ants:", colony.get_number_of_ants())
    print("Min length:", colony.get_min_length_all_time())
    print("Min tour:", colony.get_min_tour_all_time())


if __name__ == "__main__":
    main()
