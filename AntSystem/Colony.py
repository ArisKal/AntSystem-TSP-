from AntSystem.ReadData import ReadData
import numpy as np


class Colony:
    """
    Κλάση AntSystem περίέχει όλες τις λειτουργείες την αποικίας για να βρέθει η συνομότερη διαδρομή στον πρόβλημα TSP
    """

    def __init__(self, dimension, a_graph):
        """
        Στον κατασκευαστή γίνεται η αρχικοπίηση των δεδομένων που είναι απαραίτητα για την λειτουργία της αποικίας.
        - self.dimesion: Διάσταση του προβήματος
        - self.graph: Ο γράφος σε μορφή πίνακα
        - self.ants: Λίστα με τα μυρμήγκια της αποικίας
        :param dimension: Διάσταση του προβλήματος.
        :param a_graph: Γράφος σε μόρφη πίνακα.
        """
        self.dimension = dimension
        self.graph = a_graph
        self.ants = list()

    def set_demesion(self, dimension):
        """
        Ορίζει την διάσταση του προβήματος.
        :param dimension: Διάσταση πρόβληματος
        """
        self.dimension = dimension

    def set_graph(self, a_graph):
        """
        Ορίζει το γράφο σε μορφή πίνακα.
        :param a_graph: Πίνακα
        """
        self.graph = a_graph

    def set_ants(self, ants):
        """
        Ορίζει την λίστα με τα μυρμήγκια της αποικίας.
        :param ants: Λίστα με α μυρμήγκια της αποικίας
        """
        self.ants = ants

    def get_demension(self):
        """
        Επιστρέφει την διάσταση του προβήματος(integer).
        :return: Ενας ακέραιο διάσταση πρόβληματος.
        """
        return self.dimension

    def get_graph(self):
        """
        Επιστρέφει το γράφο σε μορφή πίνακα.
        :return: Πίανας είναι ο γράφος
        """
        return self.graph

    def get_ants(self):
        """
        Επιστρέφει την λίστα με τα μυρμήγκια της αποικίας.
        :return: Λίστα
        """
        return self.ants

    def run(self):
        """
        Τρέχει την αποικία.
        :return:
        """
        visibility = Colony.set_visibility(self.graph)
        print(visibility)
        graph = colony.get_graph()
        print(graph)
        initial_pherome = Colony.initialize_phenome(self.dimension, 1)
        print(initial_pherome)

    @staticmethod
    def set_visibility(a_graph):
        """
        Ορίζει την "ορατότητα" του γράφου.
        :param a_graph: Πίνακας
        :return: Πίνακα
        """
        visibility = 1 / a_graph
        return visibility
    @staticmethod
    def initialize_phenome(length, initial_value):
        """
        Αρχικοποίηση της φερομόνης.
        :param length: Η διάσταση τοτ προβλήματος.
        :param initial_value: Αρχική τιμή που θα οριστεί.
        :return: Επιστροφή πίνακα με τις αρχικές τιμές την φερομόνης.
        """
        initial_pheromone = np.zeros((dimension, dimension))
        for row in range(0, length):
            for column in range(0, length):
                if row == column:
                    initial_pheromone[row][column] = 0
                else:
                    initial_pheromone[row][column] = initial_value
        return initial_pheromone



read_data = ReadData("../data/gr17.xml")
data = read_data.get_tree()

# name = read_data.get_name_of_file()
# data = ReadData.read_file(name)
dimension = ReadData.get_dimension(data)
print(dimension)
graph = ReadData.create_graph(data, dimension)
# print(graph)

colony = Colony(dimension, graph)
colony.run()