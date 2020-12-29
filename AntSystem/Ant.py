import random


class Ant:
    """
    Κλάση Ant περιέχει όλα τα χαρακτηρηστικά του μηρμηγκιού
    - self.ant_id:To id που έχει το μυρμήγκι(integer).
    - self.starting_town: Η αρχική πόλη απο τον οποία θα ξεκινήσει την διαδρομή το μυρμήγκι(integer).
    - self.located_town: Εναι η πόλη που βρίσκεται το μυρμήγκι(integer).
    - self.tour_length: Είναι το συνολικό μήκος της διαδρομής.
    - self.allowed_town: Είναι μια λίστα με τις πόλεις που επιτρέπεται το μυρμήγκι να επισκεφτεί(tabu list).
    - self.tour: Είναι μια λίστα με τις πόλεις που έχει επισκεφτεί το μυρμήγκι(list).

    :param ant_id: Το id του μυρμηγκιού (integer).
    :param starting_town: Η αρχική πόλη (integer)
    """

    # Κατασκευαστής
    def __init__(self, ant_id, starting_town):
        self.ant_id = ant_id
        self.starting_town = starting_town
        # Στον κατασκευαστή η τρέχων πόλη είναι και η αρχική πόλη.
        self.located_town = starting_town
        # Στον κασκευαστή το συνολικό μήκος της διαδρομής είναι 0
        self.tour_length = 0
        # Κένή λίστα που θα περιέχει όλες τις πόλεις που επριτρέπεται να επισκεφτει το μηρμήγκι.
        self.allowed_towns = list()
        # Κενή λίστα με τις πόλεις που έχει επισκεφτει το μηρμήγκι.
        self.tour = list()

    def set_ant_id(self, ant_id):
        """
        Ορίζει το id του μυρμηγκιού.
        :param ant_id: integer
        """
        self.ant_id = ant_id

    def set_starting_town(self, starting_town):
        """
        Ορίζει την αρχική πόλη
        :param starting_town: integer
        """
        self.starting_town = starting_town

    def set_located_town(self, located_town):
        """
        Οριζεί την τρέχων πόλη.
        :param located_town: integer
        """
        self.located_town = located_town

    def set_tour_length(self, tour_length):
        """
        Ορίζει το συνολικό μήκος της διαδρομής
        :param length: float
        """
        self.tour_length = tour_length

    def set_allowed_towns(self, allowed_towns):
        """
        Ορίζει τις πόλεις που επιτρέπεται το μυρμήγκι να επισκεφτεί.
        :param allowed_towns: list
        """
        self.allowed_towns = allowed_towns

    def set_tour(self, town):
        """
        Πρόσθέτει στην λίστα με την διαδρομή μια πόλη.
        :param town: integer
        """
        self.tour.append(town)

    def get_ant_id(self):
        """
        Επιστρέφει το id του μυρμηγκιού.
        :return: integer
        """
        return self.ant_id

    def get_starting_town(self):
        """
        Επιστρέφει την αρχική πόλη
        :return: integer
        """
        return self.starting_town

    def get_located_town(self):
        """
        Επιστρέφει την τρέχον πόλη.
        :return: integer
        """
        return self.located_town

    def get_tour_length(self):
        """
        Επιστρφέφει το συνολικό μήκος της διαδρομής
        :return: float
        """
        return self.tour_length

    def get_allowed_towns(self):
        """
        Επιστροφή λίστας με τους επιτρεπτόμενους κόμβους.
        :return: list
        """
        return self.allowed_towns

    def get_tour(self):
        """
        Επιστρέφει την λίστα με την διαδρομή που έχει ακολουθήσει το μυρμήγκι.
        :return: list
        """
        return self.tour

    @staticmethod
    def initialize_allowed_towns(dimension):
        """
        Αρχικοποίηση των πόλεων που επιτρέπεται να επισκεφτεί το μυρμήγκι.
        :param dimension: Η διάσταση του προβλήματος(integer).
        :return: Μια λίστα με τους κόμβους που μπορέι να επισεφτεί το μυρμήγκι.
        """
        allowed_towns = []
        for town in range(0, dimension):
            allowed_towns.append(town)
        return allowed_towns

    @staticmethod
    def transition_probability(ant, alpha, beta, pheromone, visibility, number_of_towns):
        """
        Σε αυτη την μέθοδο υπολογίζεται η πιθανότητα να παει ένα μυρμήγκι απο την πόλη i στην πόλη j :
        p(i|j) = pheromone[i,j] ^ α  *  visibility[i,j] ^ β / Σ pheromone[i,allowed_towns] ^  *
                visibility[i,allowed_towns] jE allowed towns
        p(i|j) = 0
        :param number_of_towns:
        :param located_town:H τρέχον πόλη ποου βρίσκεται το μυρμίγκι (ακέραιος).
        :param next_town:Η επόμη πόλη που μπόρει να επισκεφτεί (ακέραιος).
        :param alpha:Μια παράμετρος πραγματικός αριθμός.
        :param beta:Μια παράμετρος πραγματικός αριθμός.
        :param pheromone:Η φεροόνη στις ακμές μεταξύ των πόλεων(πίνακας).
        :param visibility:Η "ορατότητα" στις ακμές μεταξύ των πόλεων(πίνακας)
        :param allowed_towns: Οι πόλεις που επιτέπεται να επισκεφτεί το μυρμήγκι(Λίστα)
        :return: Πιθανότητα πραγματικός αριθμος.
        """
        # Αν ο επόμενη πόλη βρίσκεται στη λίστα με τις πόλεις που επιτρέπεται να επισκεφτεί το μυρμήγκι.
        flag = True
        prob = list()
        for possibly_next_town in range(0, number_of_towns - 1):
            if possibly_next_town in ant.get_allowed_towns():
                sum = 0
                for allowed_town in range(0, len(ant.get_allowed_towns())):
                    pheromone_all = pheromone[ant.get_located_town()][
                                        ant.get_allowed_towns()[allowed_town]] ** alpha
                    visibility_all = visibility[ant.get_located_town()][
                                         ant.get_allowed_towns()[allowed_town]] ** beta
                    sum += pheromone_all * visibility_all
                for allowed_town in range(0, len(ant.get_allowed_towns())):
                    pheromone_next = pheromone[ant.get_located_town()][ant.get_allowed_towns()[allowed_town]] ** alpha
                    visibility_next = visibility[ant.get_located_town()][ant.get_allowed_towns()[allowed_town]] ** beta
                    b = pheromone_next * visibility_next
                    prob.append(b / sum)
            else:
                prob.append(0)

                next_town = random.choice(prob)
                print(next_town)
                prob = list()
                ant.set_tour((ant.located_town, next_town))
            # Γίνεται τρέχον πόλη η πόλη με την μεγαλύτερη πιθανότητα.
                ant.set_located_town(next_town)
            # Την αφαιρεί απο την λίστα με τις επιτρεπόμενες πόλεις
                ant.get_allowed_towns().remove(ant.get_located_town())
        # Προσθέτει στην λίστα με την διαδρομή την αρχική πόλη
        ant.set_tour((ant.get_located_town(), ant.get_starting_town()))
        # Γίνεται τρέχον πόλη η αρχική.
        ant.set_located_town(ant.get_starting_town())

        print(ant.get_tour())

        # global next_town
        # probs = []
        #
        # while len(ant.allowed_towns) > 0:
        #     b = 0
        #     if node in ant.allowed_towns:
        #         for node in range(0, 5):
        #             # Η φερομόνη σε όλες τις ακμές απο την πόλη i προς στις πόλεις που επιτρέπεται
        #             pheromone_all = pheromone[ant.get_located_town()][ant.allowed_towns[i]] ** alpha
        #             # Η ορατόττητα σε όλες τις ακμές απο την πόλη i προς στις πόλεις που επιτρέπεται
        #             visibility_all = visibility[ant.get_located_town()][ant.allowed_towns[i]] ** beta
        #             b += pheromone_all * visibility_all
        #     for i in range(0, len(ant.allowed_towns)):
        #
        #         # Η φερομόνη στην ακμή απο την πόλη i στον j
        #         pheromone_i_j = pheromone[ant.get_located_town()][node] ** alpha
        #         # "ορατότητα" στην ακμή απο την πόλη i στον j
        #         visibility_i = visibility[ant.get_located_town()][node] ** beta
        #         a = pheromone_i_j * visibility_i
        #         probability = a / b
        #         probs.append(probability)
        #     else:
        #         probability = 0
        #         probs.append(probability)
        #
        #     print(probs)
        #     rand = random.uniform(0, 1)
        #     # print("rand", rand)
        #     total = 0
        #     for i in range(0, 5):
        #         total += probs[i]
        #         # print("total", total)
        #         if total >= rand:
        #             next_town = i
        #             break
        #     # print("next", i)
        #     # next_town = ant.allowed_towns[i]
        #     # print(next_town)
        #
        #  #if probability > max_probability:
        #
        # #     #     max_probability = probability
        # #     #     next_town = prob_next
        #     ant.set_tour((ant.located_town, next_town))
        # #     # Γίνεται τρέχον πόλη η πόλη με την μεγαλύτερη πιθανότητα.
        #     ant.set_located_town(next_town)
        # #     # Την αφαιρεί απο την λίστα με τις επιτρεπόμενες πόλεις
        #     ant.get_allowed_towns().remove(ant.get_located_town())
        # # # Προσθέτει στην λίστα με την διαδρομή την αρχική πόλη
        # ant.set_tour((ant.get_located_town(), ant.get_starting_town()))
        # # # # Γίνεται τρέχον πόλη η αρχική.
        # ant.set_located_town(ant.get_starting_town())

    @staticmethod
    def compute_tour_length(ants, a_graph):
        """
        Υπολογισμός διαδρομής κάθε μυρμηγκιού.
        :param ants: Λίστα με αντικείμενα τύπου Ant
        :param a_graph: Γράφος σε μορφη πίνκα.(array)
        :return: Λίστα με αντικείμενα τύπου Ant
        """
        for k in range(0, len(ants)):
            length = 0
            for i in range(0, len(a_graph)):
                length += a_graph[ants[k].get_tour()[i][0]][ants[k].get_tour()[i][1]]
                print(length)
            ants[k].set_tour_length(length)
        return ants
