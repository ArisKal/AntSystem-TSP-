import random as rand
class Ant:
    """
    Κλάση Ant περιέχει όλα τα χαρακτηρηστικά του μηρμηγκιού
    - self.ant_id:To id που έχει το μυρμήγκι(integer).
    - self.starting_town: Η αρχική πόλη απο τον οποία θα ξεκινήσει την διαδρομή το μυρμήγκι(integer).
    - self.located_town: Εναι η πόλη που βρίσκεται το μυρμήγκι(integer).
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
        # Κένή λίστα που θα περιέχει όλες τις πόλεις που επριτρέπεται να επισκεφτει το μηρμήγκι.
        self.allowed_towns = list()
        # Κενή λίστα με τις πόλεις που έχει επισκεφτει το μηρμήγκι.
        self.tour = list()
        self.tour_length = 0


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
    def build_tour(ant, number_of_towns, pheromone, visibility, alpha, beta):
        """
        Κάθε μυρμίγκι "χτίζει" την διαδρομή που θα ακολούθήσει πάνω στον γραφο σε συνάρτηση την φερομιόνη που
        υπάρχει την δεδομένη στιγμή και και ορατότητα, τελος επιστρέφει στην αρχικλη θέση.
        :param ant: Αντικέιμενο ant.
        :param number_of_towns: Ο συνολοκός αριθμός των πόλεων πάνω στον γράφο.
        :param pheromone: Πίνακας με την φερομόνη πάνω στον γράφο.
        :param visibility: Πίνακας με την ορατότητα πάνω στον γράφο.
        :param alpha: Μία σταθερή τιμή α
        :param beta: Μια σταθέρη τιμη β
        """
        # Το μυρμίγκι θα κάνει number_of_towns - 1 επαναλήψεις για να χτίσει την διαδρομή του γιατι γιατί βρίσκεται
        # στην αρχική πόλη.
        for iteration in range(0, number_of_towns - 1):
            sum_all = 0
            # Η λίστα υα περιέχει τις πιθανότητες να πάει στην επόμενη πόλη.
            probability_list = list()
            # Για όλες τις πόλεις που **επιτρέπεται** να πάει το μυρμίγκι.
            for allowed_town in range(0, len(ant.get_allowed_towns())):
                # Το αθροισμα των πόλεων απο την παρακάτω συνάρτηση:
                sum_all += (pheromone[ant.get_located_town()][ant.get_allowed_towns()[allowed_town]] ** alpha) * \
                           (visibility[ant.get_located_town()][ant.get_allowed_towns()[allowed_town]] ** beta)
            # Για **όλες** τις πόλεις που υπάρχουν στον γράφο:
            for next_town in range(0, number_of_towns):
                # Αν η πιθανή πόλη βρίσκεται στις επιτρέπόμενες πόλεις τοτέ
                if next_town in ant.get_allowed_towns():
                    # Υπολογισμός της εξίσωσης:
                    a = (pheromone[ant.get_located_town()][next_town] ** alpha) * \
                        (visibility[ant.get_located_town()][next_town] ** beta)
                    # Το παραπάνω αποτέλεμσ διαιρείται με το σύνολο που βρέθηκε και εισάγεται στην λίστα με τις
                    # πιθανότητες.
                    probability_list.append(a / sum_all)
                else:
                    # Αν η επόμενη  πιθανή πόλη δεν είναι στην λίστα με τις επτρεπόμενς πόλεις τοτε η πιθανοτητα να
                    # πάει σε αυτή την πόλη το μυρμίγκι ειναι 0
                    probability_list.append(0)
            # Επιλογή της επομενης πόλης απο την λίστα
            random_number = rand.uniform(0, 1)
            total = 0.0
            next_town = 0
            for i in range(0, number_of_towns):
                total = total + probability_list[i]
                if total >= random_number:
                    next_town = i
                    break
            # Εισάγη στην λίστα με δισδρομομη την πόλη
            ant.set_tour((ant.get_located_town(), next_town))
            ant.set_located_town(next_town)
            # Αφαιρεί απο την λίστα με τις επιτρεπόμενς πόλεις την πόλη αυτή.
            ant.get_allowed_towns().remove(next_town)
            # Καθαρίζει την λιστα με τις πιθανότητες
            probability_list.clear()
        # Επιστρέφει το μυρμήγκι στην αρχικλη πόλη.
        ant.set_tour((ant.get_located_town(), ant.get_starting_town()))
        ant.set_located_town(ant.get_starting_town())

    @staticmethod
    def compute_tour_length(ant, a_graph):
        """
        Υπολογισμός διαδρομής κάθε μυρμηγκιού.
        :param ant: Αντικείμενο τύπου Αnt.(Ant)
        :param a_graph: Γράφος σε μορφη πίνκα.(array)
        :return: συνολικό μήκος διαδρομής.(integer)
        """
        # Υπολογισμος απο την λίστα με τις ακμές το μήκος της συνολικής διαδρομής
        for town in range(0, len(a_graph)):
            ant.tour_length += a_graph[ant.tour[town][0]][ant.tour[town][1]]
        return ant.tour_length


    # def get_amount_of_phreromone_deposit_by_ant(self, delta):
    #     """
    #     Η ποσότητα φερομόνης που αφήνει το κάθε μυρμίγκι απο στις ακμές του γράφου.\
    #     Υπολογίζεται απο τον τύπο:
    #     delta_ant(x,y) = Q / length_ant
    #     Q = 1
    #     :return: Η ποσότητα φερομόνης που αφήνει το  μυρμήγκι απο στις ακμές του γράφου.
    #     """
    #     for edge in range(0, len(self.tour)):
    #         delta[self.tour[edge][0]][self.tour[edge][1]] += 1 / self.tour_length
    #         delta[self.tour[edge][1]][self.tour[edge][0]] += 1 / self.tour_length
    #




