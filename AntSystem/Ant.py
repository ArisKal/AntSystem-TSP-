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
        :param tour_length:
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
    def multiply_function(pheromone, visibility, located_town, possibly_next_town, alpha, beta):
        """
        Σε αύτη τη μέθοδο πολαπλασιάζεται η φερομόνη ως προς το α με την ορατότητα ως προς το β
        της ακμή απο την τρέχων πόλη ως προς στην πιθανή επόμενη πόλη.
        :param pheromone: η φερομόνη μεταξλυ των πόλεων.
        :param visibility η ορατότηα μεταξύ των πόλεων
        """
        return pheromone[located_town][possibly_next_town] ** alpha \
               * visibility[located_town][possibly_next_town] ** beta

    @staticmethod
    def next_town(ant, alpha, beta, pheromone, visibility, number_of_towns):
        """
        Σε αυτη την μεθόδο υλοποιείται σε ποιά πόλη θα μετακινιθεί το μυρμήγκι Ποιο συγκεκριμένα απο τις πόλεις που
        επιτρέπεται να μετακινηθεί το μυρμήγγκι θα υπολογίσουμε το συνολο του αποτελέσματος της μεθόδου multiply_function
        Υστερα για κάθε πολη που υπάρχει στον γραφο θα υπολογίσουμε την πιθανότητα να μετακινηθει το μυρμήγκι για κάθε
        πόλη που επιτρέπεται τα επισκεφτεί το μυρμήγκι θα υπολογίζεται το multiply_function και θα διαιρήται με το
        σύνολο που βρέθηκε προηγουμένος, το αποτέλεσμα αυτο θα μπάινει σε μια λίστα που θα έχει τις πιθανότητες για
        κάθε πόλη για να μετακινηθει το μυρμήγκι, αν η πιθανη πόλη που επιλέγεται δεν επιτρέπεται να πάει το μυρμμηγκι
        γιατι την έχει επισκεφτεί προηγουμένος τότε στην λίστα με τις πιθανότητες θα μπάινει το 0 η επολογη της επόμενης
        πόλης που θα μετακινηθεί το μυρμήγκι θα επιλέγεται με μία μεθοδο τυχαιιότητας.
        :param number_of_towns: o συνολικός αριθμός των πόλεων που υπάρχουν στον γράφο.
        :param visibility: Η ορατότηα μεταξύ των πόλεων.
        :param pheromone: Η φερομόνη μεταξύ των πόλεων.
        :param beta: Η παράμετρος β.
        :param alpha:Η παράμετρος α.
        :param ant: Ενα αντικείμενο τυπου ant
        """
        # Δημιουργια λίστας με τις πιθανότητες να μετακινήθει το μιρμήγκι απο την πόλη i στην πόλη j.
        prob = list()
        sum_all = 0
        # Η τρέχων πόλη που βρίσκεται το μυρμήγκι.
        located_town = ant.get_located_town()
        # Για κάθε πόλη που επιτρέπεται να πάει το μυρμύγκι.
        for allowed_town in range(0, len(ant.get_allowed_towns())):
            allowed_town = ant.get_allowed_towns()[allowed_town]
            # Υπολόγισε τον πολαπλασιασμο της φερομονης και της ορατοτητας για την επόμενη πόλη και προσθεσέ το
            sum_all += Ant.multiply_function(pheromone, visibility, located_town, allowed_town, alpha, beta)
        # Για κάθε πιθανή πόλη(ολες οι πόλεις του γράφου)
        for possibly_next_town in range(0, number_of_towns):
            # Αν επιτρέται να παει στην πιθανή πόλη τοτε:
            if possibly_next_town in ant.get_allowed_towns():
                # Υπολόγισε τον πολαπλασιασμο της φερομονης και της ορατοτητας για την επόμενη πόλη.
                a = Ant.multiply_function(pheromone, visibility, located_town, possibly_next_town, alpha, beta)
                # Τότε η πιθανότητα να παει σε αυτη την πόλη ειναι a/sum_all.
                probability = a / sum_all
                prob.append(probability)
            else:
                # Αλλιώς αν δεν επιτρέπεται να παέι σε αυτη την πόλη τοτε η πιθανότητα ειναι 0
                prob.append(0)
        # Επιλογη της πόλης απο την λίστα με τις πιθανότητες με μια μέθοδο τυχαιότητας.
        r = random.uniform(0, 1)
        total = 0
        next_town = int()
        for i in range(0, number_of_towns):
            total += prob[i]
            if total >= r:
                next_town = i
                break
        prob.clear()
        return next_town

    @staticmethod
    def move_ant(ant, next_town):
        ant.set_tour((ant.located_town, next_town))
        # Γίνεται τρέχον πόλη η πόλη με την μεγαλύτερη πιθανότητα.
        ant.set_located_town(next_town)
        ant.get_allowed_towns().remove(ant.get_located_town())

    @staticmethod
    def move_ant_at_starting_node(ant):
        """
        Επιστροφη μυρμηγκιού στην αρχικη πόλη
        :param ant:
        :return:
        """
        ant.set_tour((ant.get_located_town(), ant.get_starting_town()))
        ant.set_located_town(ant.get_starting_town())

    @staticmethod
    def quantity_per_unit_of_length_of_pheromone(ant, pheromone_ant_leaves, number_of_towns):
        """
        Υπολογισμός της ποσότητας φερομόνης που αφήνει κάθε μυρήγκι
        """
        # print(ant.get_tour())
        for i in range(0, number_of_towns):
            # print(ant.get_tour()[i][0], ant.get_tour()[i][1])
            pheromone_ant_leaves[ant.get_tour()[i][0]][ant.get_tour()[i][1]] += 1 / ant.get_tour_length()
        return pheromone_ant_leaves

    @staticmethod
    def compute_tour_length(ant, a_graph):
        """
        Υπολογισμός διαδρομής κάθε μυρμηγκιού.
        :param ant:
        :param a_graph: Γράφος σε μορφη πίνκα.(array)
        :return: Λίστα με αντικείμενα τύπου Ant
        """
        length = 0
        for i in range(0, len(a_graph)):
            length += a_graph[ant.get_tour()[i][0]][ant.get_tour()[i][1]]
        ant.set_tour_length(length)
