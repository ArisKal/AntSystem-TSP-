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
        - self.min_length_all_time: H μικρότερη διαδρομή σε κόστος μεσα στην αποικία.
        - self.min_tour_all_time Η διαδρομή με το μικρότερο κόστος μέσα στην αποικία.

        :param dimension: Διάσταση του προβλήματος.
        :param a_graph: Γράφος σε μόρφη πίνακα.
        :param number_of_ants: Αριθμος μυρμηγκιών
        :param alpha: Mia παραμετρος a ελέγχει την σχετική σημασιά της φερομόνης
        :param beta: Mia παραμετρος β ελέγχει την σχετική σημασιά της "ορατότητας".
        :param evaporation_rate: evaporation_rate: Ο ρυθμός εξάτμησης της φερομόνης σε κάθε κύκλο
        :param number_of_cycles: Ο αριθμός κύκλων που θα εκλτελέσει η αποικία.
        """
        self.dimension = dimension
        self.a_graph = a_graph
        self.number_of_ants = number_of_ants
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.number_of_cycles = number_of_cycles
        self.ants = list()
        self.delta = np.zeros((dimension, dimension))
        self.pheromone = np.zeros((dimension, dimension))
        self.min_length_all_time = np.inf
        self.min_tour_all_time = []

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

    def set_ants(self, ants):
        """
        Ορίζει την λίστα με τα μυρμήγκια της αποικίας.
        :param ants: list
        """
        self.ants = ants

    def set_min_length_all_time(self, min_length_all_time):
        """
        Ορίζει το μικρίτερο κόστος μεσα την αποικία.
        """
        self.min_length_all_time = min_length_all_time

    def set_min_tour_all_time(self, min_tour_all_time):
        """
        Ορίζει την διαδρομή με το μικρότερο κόστος μεσα στην αποικία.
        """
        self.min_length_all_time = min_tour_all_time

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

    def get_ants(self):
        """
        Επιστρέφει την λίστα με τα μυρμήγκια της αποικίας.
        :return: list
        """
        return self.ants

    def get_min_length_all_time(self):
        """
        Επιστρέφει τo μικρότερο κόστος στην αποικία.
        :return: real
        """
        return self.min_length_all_time

    def get_min_tour_all_time(self):
        """
        Επιστρέφει λίστα με την  διαδρόμη που έχει το μικρότερο κόστος μέσα στην αποικία.
        :return: list
        """
        return self.min_tour_all_time

    @staticmethod
    def set_visibility(a_graph):
        """
        Ορίζει την "ορατότητα" του γράφου.
        :param a_graph: array
        :return: array
        """
        visibility = np.zeros((len(a_graph), len(a_graph)))
        for i in range(0, len(a_graph)):
            for j in range(0, len(a_graph)):
                if i == j:
                    visibility[i][j] = 0
                else:
                    visibility[i][j] = 1 / a_graph[i][j]
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
            starting_town = rand.randint(0, dimension - 1)
            # Δημιουργία ενός αντικειμένου τυπου Αnt ορίζω το id του μυμρμηγκιού, και την τυχαία αρχική πόλη
            ants.append(Ant(ant_id, ant_id))
            # Για κάθε μυρμήγκι ορίζω τους κόμβους που επιτρέπεται να πάει
            ants[ant_id].set_allowed_towns(Ant.initialize_allowed_towns(dimension))
            # Αφαιρώ απο την λίστα με τους επιτρεπτόμενους κόμβους τον αρχικο κόμβο
            ants[ant_id].get_allowed_towns().remove(ants[ant_id].get_starting_town())
        return ants

    # @staticmethod
    # def get_amount_of_phreromone_deposit_by_ant(ants, number_of_towns):
    #     """
    #     Η ποσότητα φερομόνης που αφήνει το κάθε μυρμίγκι απο στις ακμές του γράφου.\
    #     Υπολογίζεται απο τον τύπο:
    #     delta_ant(x,y) = Q / length_ant
    #     Q = 1
    #     :return: Η ποσότητα φερομόνης που αφήνει το  μυρμήγκι απο στις ακμές του γράφου.
    #     """
    #     delta = np.zeros((number_of_towns, number_of_towns))
    #     for ant in ants:
    #         for edge in range(0, len(ant.get_tour())):
    #             delta[ant.get_tour()[edge][0]][ant.get_tour()[edge][1]] += 1 / ant.get_tour_length()
    #             delta[ant.get_tour()[edge][1]][ant.get_tour()[edge][0]] += 1 / ant.get_tour_length()
    #     return delta

    @staticmethod
    def update_pheromone(ants, pheromone, number_of_towns, evaporation_rate):
        """
        Ενημέρωση φερομόνης στις ακμές του γράφου.
        :param number_of_towns: Το σύνολο των πόλεων.
        :param ants: Ο πίνακας με τα μυρμήγκια.
        :param evaporation_rate: Ρυθμός εξάτμισης φερομόνης(real)
        :param pheromone: Πινακας με τις τιμές της φερομόνης πάνω στις ακμές του γράφου(array)
        :return:Πίανκας με την ενημερωμένη φερομόνη(array).
        """
        # Για κάθε μυρμήγκι
        for ant in ants:
            # Για κάθε ακμή του γράφου που έχει περάσει το μυρμήγκι αφήνει μια ποσότηα φερομόνης
            for edge in range(0, len(ant.get_tour())):
                pheromone[ant.get_tour()[edge][0]][ant.get_tour()[edge][1]] += 1 / ant.get_tour_length()
                pheromone[ant.get_tour()[edge][1]][ant.get_tour()[edge][0]] += 1 / ant.get_tour_length()
        # Για κάθε ακμή του γράφου να γίνει εξάτμιση φερομόνης.
        for i in range(0, number_of_towns):
            for j in range(0, number_of_towns):
                if i != j:
                    pheromone[i][j] = evaporation_rate * pheromone[i][j]
                else:
                    pheromone[i][j] = 0
        return pheromone

    def run(self):
        """
        Τρέχει την αποικία.
        """
        # Αρχικοποιήση της αρχικής φερομόνης στις ακμές ματαξύ των πόλεων.
        initial_pheromone = Colony.initialize_pheromone(self.dimension, initial_value=1)
        pheromone = initial_pheromone
        # Αρχικοποίηση ορατλοτητας
        visibility = Colony.set_visibility(self.a_graph)
        # Αρχικοποίση μυρμήγκιών στην αποικία.
        ants = Colony.initialize_ants(self.ants, self.number_of_ants, self.dimension)
        # graph = self.a_graph
        for number_of_cycle in range(0, self.number_of_cycles):
            # print("nc = ", number_of_cycle)
            # Για κάθε μυρμήγκι.
            for ant in ants:
                # Κατασκεύη διαδρομών
                Ant.build_tour(ant, self.dimension, pheromone, visibility, self.alpha, self.beta)
                # Υπολογισμός κόστους της διαδρομής και εισαγωγή στην λίστα
                length = Ant.compute_tour_length(ant, self.a_graph)
                if length < self.min_length_all_time:
                    self.min_length_all_time = length
                    self.min_tour_all_time[:] = ant.get_tour()
            pheromone = Colony.update_pheromone(ants, pheromone, self.dimension, self.evaporation_rate)
            for ant in ants:
                ant.set_allowed_towns(Ant.initialize_allowed_towns(self.dimension))
                ant.get_tour().clear()
                ant.set_tour_length(0)
                ant.get_allowed_towns().remove(ant.get_starting_town())

