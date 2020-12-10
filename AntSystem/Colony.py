from AntSystem.ReadData import ReadData
from AntSystem.Ant import Ant
import numpy as np
import random as rand


class Colony:
    """
    Κλάση AntSystem περίέχει όλες τις λειτουργείες την αποικίας για να βρέθει η συνομότερη διαδρομή στον πρόβλημα TSP
    """

    def __init__(self, dimension, a_graph, number_of_ants):
        """
        Στον κατασκευαστή γίνεται η αρχικοπίηση των δεδομένων που είναι απαραίτητα για την λειτουργία της αποικίας.
        - self.dimension: Διάσταση του προβήματος
        - self.graph: Ο γράφος σε μορφή πίνακα
        - self.ants: Λίστα με τα μυρμήγκια της αποικίας
        - self.number_of_ants: Αριθμος μυρμηγκιών
        :param dimension: Διάσταση του προβλήματος.
        :param a_graph: Γράφος σε μόρφη πίνακα.
        """
        self.dimension = dimension
        self.a_graph = a_graph
        self.number_of_ants = number_of_ants
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
        self.a_graph = a_graph

    def set_number_of_ants(self, number_of_ants):
        """
        Ορίζει τον αριθμο τον μυρμηγκιών στην αποικία.
        :param number_of_ants: Ακέραιος αριθμός μυρμηγκιών.
        """

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
        return self.a_graph

    def get_number_of_ants(self):
        """
        Επιστρέφει τον αριθμό τον μυρμηγκιών στην αποικία.
        :return: Ακέραιος αριθμός μυρμηγκιών.
        """
        return self.number_of_ants()

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
        # Initialize
        cycles = 0
        initial_pheromone = Colony.initialize_pheromone(self.dimension, 1)
        pheromone = initial_pheromone
        delta_pheromone = np.zeros((self.dimension, self.dimension))
        print(self.a_graph)
        visibility = colony.set_visibility(self.a_graph)

        ants = Colony.initialize_ants(self.ants, self.number_of_ants, self.dimension)
        print("============================Initialize========================================")
        for k in range(0, self.number_of_ants):
            print("ant id:", ants[k].get_ant_id())
            print("starting node:", ants[k].get_starting_node())
            print("allowed nodes:", ants[k].get_allowed_nodes())

        print("==========================TOURS=========================================")
        for k in range(0, self.number_of_ants):
            print("ant", k)
            ant = ants[k]
            tour = colony.built_tour(ant, 0.7, 0.7, pheromone, visibility, self.dimension)
            print(tour)

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
    def initialize_pheromone(dimension, initial_value):
        """
        Αρχικοποίηση της φερομόνης.
        :param dimension: Η διάσταση τοτ προβλήματος.
        :param initial_value: Αρχική τιμή που θα οριστεί.
        :return: Επιστροφή πίνακα με τις αρχικές τιμές την φερομόνης.
        """
        initial_pheromone = np.zeros((dimension, dimension))
        for row in range(0, dimension):
            for column in range(0, dimension):
                if row == column:
                    initial_pheromone[row][column] = 1
                else:
                    initial_pheromone[row][column] = initial_value
        return initial_pheromone

    @staticmethod
    def initialize_ants(ants, number_of_ants, dimension):
        """
        Αρχικοποίηση μυρμήγκιων σε τυχαίες αρχικές θέσεις.
        :param ants: Λίστα άδεια
        :param number_of_ants: Ο συνολικος αριθμος των μυρμηγκιών στην αποίκια
        :param dimension: ακέραιος με την διάσταση του προβλήματος.
        :return: Λίστα αντικειμέων τύπου Αnt με τα μυμρήγκια της αποικίας αρχικοποιημένα στις αρχικές θέσεις.
        """
        for ant_id in range(0, number_of_ants):
            # Τυχαίος αριθμός είναι  dimension -1 γιατό ξεκινάει απο το 0
            starting_node = rand.randint(0, dimension - 1)
            # Δημιουργία ενός αντικειμένου τυπου Αnt ορίζω το id του μυμρμηγκιού, και την τυχαία αρχική θέση
            ants.append(Ant(ant_id, starting_node))
            # Για κάθε μυρμήγκι ορίζω τους κόμβους που επιτρέπεται να πάει
            ants[ant_id].set_allowed_nodes(Ant.initialize_allowed_nodes(dimension))
            # Αφαιρώ απο την λίστα με τους επιτρεπτόμενους κόμβους τον αρχικο κόμβο
            ants[ant_id].get_allowed_nodes().remove(ants[ant_id].get_starting_node())

            ants[ant_id].set_tour(ants[ant_id].get_starting_node())

        return ants

    @staticmethod
    def built_tour(ant, alpha, beta, pheromone, visibility, dimension):
        """
        Μέθοδος που κατασευάζει την διαδρομή που θα ακολουθήσει το μυρμήγκι.
        :param ant: Αντικείμενο τύπου Ant.
        :param alpha: Mia σταθερή παράμετρος α.
        :param beta: Mia σταθερή παράμετρος β.
        :param pheromone: Η φερομονη στις ακμές μεταξύ των πόλεων.
        :param visibility: Η "ορατότητα" στις ακμές μεταξύ των πόλεων.
        :param dimension: Η διάσταση του προβλήματος
        :return: ενας πίνακα με την διαφρομη που ακολούθησε το μυρμήγκι
        """
        # Μέχρι να αδειάσει η λίστα με τις πόλεις που επιτεπεται να πάει το μυρμήγκι
        # είναι το σύνολο των πόλεων -1 γιάτι ήδη έχουμε αφαιρέσει απο την λίστα την αρχική πόλη.
        for iteration in range(0, dimension - 1):
            located_town = ant.get_located_node()
            allowed_towns = ant.get_allowed_nodes()
            max_probability = 0
            # Για κάθε τιμή της λίστας
            for index in range(0, len(allowed_towns)):
                # Υπολογισμος πιθανότητας να μετακινηθεί απο την πόλη που βρίσκεται αυτη την στιμγή σε μια αλλή πόλη που
                # βρίσκεται στην λίστα με τις πόλεις που επιτρέπεται να μετακινηθεί.
                probability = Ant.transition_probability(located_town, allowed_towns[index], alpha, beta, pheromone,
                                                         visibility,
                                                         allowed_towns)
                if probability > max_probability:
                    max_probability = probability
                    next_node = allowed_towns[index]
            # Τρέχον πόλη γίνεται η πόλη με την μεγαλύτερη πιθανότητα.
            ant.set_located_node(next_node)
            # Την προσθέτει στην λίστα με την διαδρομή.
            ant.set_tour(next_node)
            # Την αφαιρεί απο την λίστα με τις επιτρεπόμενες πόλεις
            ant.get_allowed_nodes().remove(ant.get_located_node())
        return ant.get_tour()


# read_data = ReadData("../data/gr17.xml")
# data = read_data.get_tree()
# name = read_data.get_name_of_file()
# data = ReadData.read_file(name)
data = np.array([[0, 3, 6, 2, 3], [3, 0, 5, 2, 3], [6, 5, 0, 6, 4], [2, 2, 6, 0, 6], [3, 3, 4, 6, 0]])
# print(data)
# dimension = ReadData.get_dimension(data)
# print(len(data))
# graph = ReadData.create_graph(data, dimension)
# print(graph)

colony = Colony(len(data), data, 5)
colony.run()
