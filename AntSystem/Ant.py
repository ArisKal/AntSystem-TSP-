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
    def transition_probability(located_town, next_town, alpha, beta, pheromone, visibility, allowed_towns):
        """
        Σε αυτη την μέθοδο υπολογίζεται η πιθανότητα να παει ένα μυρμήγκι απο την πόλη i στην πόλη j :
        p(i|j) = pheromone[i,j] ^ α  *  visibility[i,j] ^ β / Σ pheromone[i,allowed_towns] ^  *
                visibility[i,allowed_towns] jE allowed towns
        p(i|j) = 0
        :param located_towns:H τρέχον πόλη ποου βρίσκεται το μυρμίγκι (ακέραιος).
        :param next_town:Η επόμη πόλη που μπόρει να επισκεφτεί (ακέραιος).
        :param alpha:Μια παράμετρος πραγματικός αριθμός.
        :param beta:Μια παράμετρος πραγματικός αριθμός.
        :param pheromone:Η φεροόνη στις ακμές μεταξύ των πόλεων(πίνακας).
        :param visibility:Η "ορατότητα" στις ακμές μεταξύ των πόλεων(πίνακας)
        :param allowed_towns: Οι πόλεις που επιτέπεται να επισκεφτεί το μυρμήγκι(Λίστα)
        :return: Πιθανότητα πραγματικός αριθμος.
        """
        # Αν ο επόμενη πόλη βρίσκεται στη λίστα με τις πόλεις που επιτρέπεται να επισκεφτεί το μυρμήγκι.
        if next_town in allowed_towns:
            # Η φερομόνη στην ακμή απο την πόλη i στον j
            pheromone_i_j = pheromone[located_town][next_town] ** alpha
            # "ορατότητα" στην ακμή απο την πόλη i στον j
            visibility_i = visibility[located_town][next_town] ** beta
            a = pheromone_i_j * visibility_i

            # Η φερομόνη σε όλες τις ακμές απο την πόλη i προς στις πόλεις που επιτρέπεται
            pheromone_all = pheromone[located_town][allowed_towns] ** alpha
            # Η ορατόττητα σε όλες τις ακμές απο την πόλη i προς στις πόλεις που επιτρέπεται
            visibility_all = visibility[located_town][allowed_towns] ** beta
            b = sum(pheromone_all * visibility_all)

            return a / b

        else:
            return 0

    @staticmethod
    def compute_tour_length(ant, a_graph):
        """
        Υπολογισμός διαδρομής κάθε μυρμηγκιού.
        :param ant: Αντικείμενο τύπου Αnt.(Ant)
        :param a_graph: Γράφος σε μορφη πίνκα.(array)
        :return: συνολικό μήκος διαδρομής.(integer)
        """
        # Άρχικοποίηση
        length_tour = 0
        # Υπολογισμος απο την λίστα με τις ακμές το μήκος της συνολικής διαδρομής
        for i in range(0, len(a_graph)):
            length_tour += a_graph[ant.get_tour()[i][0]][ant.get_tour()[i][1]]
        return length_tour
