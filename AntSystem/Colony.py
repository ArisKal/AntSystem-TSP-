from AntSystem.Ant import Ant
import numpy as np
import random as rand


class Colony:
    """
    Κλάση AntSystem περίέχει όλες τις λειτουργείες την αποικίας για να βρέθει η συνομότερη διαδρομή στον πρόβλημα TSP
    """

    def __init__(self, dimension, a_graph, number_of_ants, alpha, beta, evaporation_rate, number_of_cycles):
        """
        Στον κατασκευαστή γίνεται η αρχικοπίηση των δεδομένων που είναι απαραίτητα για την λειτουργία της αποικίας.
        - self.dimension: Διάσταση του προβήματος.
        - self.a_graph: Ο γράφος σε μορφή πίνακα.
        - self.ants: Λίστα με τα μυρμήγκια της αποικίας.
        - self.number_of_ants: Αριθμος μυρμηγκιών.
        - self.alpha: Mia παραμετρος a ελέγχει την σχετική σημασιά της φερομόνης.
        - self.beta: Mia παραμετρος β ελέγχει την σχετική σημασιά της "ορατότητας".
        - self.evaporation_rate: Ο ρυθμός εξάτμησης της φερομόνης σε κάθε κύκλο
        - self.number_of_cycles: Ο αριθμός κύκλων που θα εκλτελέσει η αποικία.
        :param dimension: Διάσταση του προβλήματος.
        :param a_graph: Γράφος σε μόρφη πίνακα.
        """
        self.dimension = dimension
        self.a_graph = a_graph
        self.number_of_ants = number_of_ants
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.number_of_cycles = number_of_cycles
        self.shortest_tour = 0
        self.min_length = np.inf
        self.ants = list()

    def set_dimension(self, dimension):
        """
        Ορίζει την διάσταση του προβήματος.
        :param dimension: integer
        """
        self.dimension = dimension

    def set_graph(self, a_graph):
        """
        Ορίζει το γράφο σε μορφή πίνακα.
        :param a_graph: array
        """
        self.a_graph = a_graph

    def set_number_of_ants(self, number_of_ants):
        """
        Ορίζει τον αριθμο τον μυρμηγκιών στην αποικία.
        :param number_of_ants: integer
        """

    def set_alpha(self, alpha):
        """
        Όρίζει την παραμετρος a ελέγχει την σχετική σημασιά της φερομόνης.
        :param alpha: real
        """
        self.alpha = alpha

    def set_beta(self, beta):
        """
        Όρίζει την παραμετρος β ελέγχει την σχετική σημασιά της "ορατότητας".
        :param beta: real
        """
        self.beta = beta

    def set_evaporation_rate(self, evaporation_rate):
        """
        Ορίζει τον  ρυθμό εξάτμησης της φερομόνης σε κάθε κύκλο
        :param evaporation_rate: real
        """
        self.evaporation_rate = evaporation_rate

    def set_number_of_cycles(self, number_of_cycles):
        """
        Ορίζει τον αριθμό των κλυκλων που θα εκτελέσει η αποικία
        :param number_of_cycles: integer
        """
        self.number_of_cycles = number_of_cycles

    def set_shortest_tour(self, shortest_tour):
        """
        Ορίζει την συντομοτερη διαδρομή
        :param shortest_tour: list
        """
        self.shortest_tour = shortest_tour

    def set_min_length(self, min_length):
        """
        Ορίζει το μικρότερο κόστος
        :param min_length: real
        """
        self.min_length = min_length

    def set_ants(self, ants):
        """
        Ορίζει την λίστα με τα μυρμήγκια της αποικίας.
        :param ants: list
        """
        self.ants = ants

    def get_dimension(self):
        """
        Επιστρέφει την διάσταση του προβήματος(integer).
        :return: integer
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
        :return: integer
        """
        return self.number_of_ants

    def get_alpha(self):
        """
        Επιστρέφει το α μια παράμετρος που ελέγχει την σχετική σημασιά της φερομόνης.
        :return: real
        """
        return self.alpha

    def get_beta(self):
        """
        Επιστρέφει το β μια παράμετρος που ελέγχει την σχετική ορατότητα της φερομόνης.
        :return: real
        """
        return self.beta

    def get_evaporation_rate(self):
        """
        Επιστρέφει το ρυθμό εξάτμισης της φερομόνης της αποικίας σε κάθε κύκλο
        :return: real
        """
        return self.evaporation_rate

    def get_number_of_cycles(self):
        """
        Επιστρέφει τον αρθμό των κύκλων που θα εκτελέσει η αποικία.
        :return: integer
        """
        return self.number_of_cycles

    def get_shortest_tour(self):
        """
        Επιστρέφει την συντομοτερη διαδρομή
        :return shortest_tour: list
        """
        return self.shortest_tour

    def get_min_length(self):
        """
        Επιστρέφει το μικρότερο κόστος
        :return min_length: real
        """
        return self.min_length

    def get_ants(self):
        """
        Επιστρέφει την λίστα με τα μυρμήγκια της αποικίας.
        :return: list
        """
        return self.ants

    @staticmethod
    def set_visibility(a_graph):
        """
        Ορίζει την "ορατότητα" του γράφου.
        :param a_graph: array
        :return: array
        """
        visibility = 1 / a_graph
        return visibility

    @staticmethod
    def initialize_pheromone(dimension, initial_value):
        """
        Αρχικοποίηση της φερομόνης.
        :param dimension: Η διάσταση τοτ προβλήματος.
        :param initial_value: Αρχική τιμή που θα οριστεί(integer).
        :return: Επιστροφή πίνακα με τις αρχικές τιμές την φερομόνης(array).
        """
        initial_pheromone = np.zeros((dimension, dimension))
        for row in range(0, dimension):
            for column in range(0, dimension):
                if row == column:
                    initial_pheromone[row][column] = 0
                else:
                    initial_pheromone[row][column] = initial_value
        return initial_pheromone

    @staticmethod
    def initialize_ants(ants, number_of_ants, dimension):
        """
        Αρχικοποίηση μυρμήγκιων σε τυχαίες αρχικές θέσεις.
        :param ants: Λίστα άδεια
        :param number_of_ants: Ο συνολικος αριθμος των μυρμηγκιών στην αποίκια
        :param dimension: ακέραιος με την διάσταση του προβλήματος(integer).
        :return: Λίστα αντικειμέων τύπου Αnt με τα μυμρήγκια της αποικίας αρχικοποιημένα στις αρχικές θέσεις(list).
        """
        for ant_id in range(0, number_of_ants):
            # Τυχαίος αριθμός είναι  dimension -1 γιατό ξεκινάει απο το 0
            # starting_town = rand.randint(0, dimension - 1)
            # Δημιουργία ενός αντικειμένου τυπου Αnt ορίζω το id του μυμρμηγκιού, και την τυχαία αρχική πόλη
            ants.append(Ant(ant_id, ant_id))
            # Για κάθε μυρμήγκι ορίζω τους κόμβους που επιτρέπεται να πάει
            ants[ant_id].set_allowed_towns(Ant.initialize_allowed_towns(dimension))
            # Αφαιρώ απο την λίστα με τους επιτρεπτόμενους κόμβους τον αρχικο κόμβο
            ants[ant_id].get_allowed_towns().remove(ants[ant_id].get_starting_town())
        return ants

    @staticmethod
    def evaporate_pheromone(pheromone, evaporation_rate):
        """
        Ενημέρωση φερομόνης στις ακμές του γράφου

        :param evaporation_rate: Ρυθμός εξάτμισης φερομόνης(real)
        :param pheromone: Πινακας με τις τιμές της φερομόνης πάνω στις ακμές του γράφου(array)
        :return:Πίανκας με την ενημερωμένη φερομόνη(array).
        """
        for i in range(0, len(pheromone)):
            for j in range(0, len(pheromone)):
                if i != j:
                    pheromone[i][j] *= (1 - evaporation_rate)
        return pheromone

    def run(self):
        """
        Τρέχει την αποικία.
        """
        # Αρχικοποιήση
        # Αρχικοποιήση της αρχικής φερομόνης στις ακμές ματαξύ των πόλεων.
        initial_pheromone = Colony.initialize_pheromone(self.dimension, 1)
        pheromone = initial_pheromone
        # Αρχικοποίηση ενός πινακα n * n διαστάσεων που θα περέχει μετα τον υπολογισμό την ποσότητας φερομόνης ανα
        # μονάδα συνολικού μήκους διαδρομης κάθε ακμής που την  επισκέφτηκε κάθε μηρμήγκι.
        quantity = np.zeros((self.dimension, self.dimension))
        # Αρχικοποίηση ενός πίνακα n * n που θα περιέχει μετα τον υπολογισμό θα περιέχει την "ορατότητα" στις ακμές
        # μεταξύ των πόλεων.
        visibility = Colony.set_visibility(self.a_graph)
        # Αρχικοποίση μυρμήγκιών στην αποικία.
        ants = Colony.initialize_ants(self.ants, self.number_of_ants, self.dimension)

        for nc in range(0, self.number_of_cycles):
            print(nc)
            # Μέχρι η λίστα με την διαδρομή να γεμίσει εναι το πληθος των πόλεων -1 γιατι βρίσκεται ήδη στην αρχική πόλη
            for ant in ants:
                for move in range(self.dimension - 1):
                    # Μετακίνησε το μυρμήγκι στη επόμενη πόλη
                    next_town = Ant.next_town(ant, self.alpha, self.beta, pheromone, visibility, self.dimension)
                    Ant.move_ant(ant, next_town)
            for ant in ants:
                # Μετάκινησε το μυρμήγκη στην αρχική πόλη
                Ant.move_ant_at_starting_node(ant)
                Ant.compute_tour_length(ant, self.a_graph)
                if ant.get_tour_length() < self.min_length:
                    self.min_length = ant.get_tour_length()
                    self.set_shortest_tour(ant.get_tour()[:])
                Ant.quantity_per_unit_of_length_of_pheromone(ant, quantity, self.dimension)
            Colony.evaporate_pheromone(pheromone, self.evaporation_rate)
            for ant in ants:
                ant.set_allowed_towns(Ant.initialize_allowed_towns(self.dimension))
                ant.get_tour().clear()
                ant.get_allowed_towns().remove(ant.get_starting_town())
                ant.set_tour_length(0)

            # quantity = np.zeros((self.dimension, self.dimension))
