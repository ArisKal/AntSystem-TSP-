class Ant:
    """
    Κλάση Ant περιέχει όλα τα χαρακτηρηστικά του μηρμηγκιού
    - self.ant_number: είναι ο μοναδικός χαρακτηριστικός αριθμος που έχεο το κάθε μηρμήγκι.
    - self.starting_node: είναι ο κόμβος απο τον οποίο θα ξεκινησει το μυρμήγκι.
    - self.located_nodes: έναι ο κόμβος που βρήσκεται κάθε στιγμή το μυρμήγκι.
    - self.allowed_noded: είναι μία λίστα με τους κόμβους που επριτρέπεται να επισκεφτει το μηρμήγκι.
    - self.tour: είναι μία λίστα με τους κόμβους που έχει επισκεφτει το μηρμήγκι.

    :param ant_id o αριθμός του μηρμηγκιού.
    :param starting_node o αρχικός κόμβος που τοποθετειται το μηρμήγκι,
    """

    # Κατασκευαστής
    def __init__(self, ant_id, starting_node):
        self.ant_id = ant_id
        self.starting_node = starting_node
        # Στον κατασκευαστή ο τρέχων κόμβος είναι και ο αρχικός κόμβος.
        self.located_node = starting_node
        # Κένή λίστα που θα περιέχει τους κόμβος που επριτρέπεται να επισκεφτει το μηρμήγκι.
        self.allowed_nodes = list()
        # Κενή λίστα με τους κόμβους που έχει επισκεφτει το μηρμήγκι.
        self.tour = list()

    # Ορίζει ένας αριθμό στο μυρμήγκι.
    def set_ant_id(self, ant_id):
        self.ant_id = ant_id

    # Ορίζει τον αρχικό κόμβο που θα τοποθετηθέι το μηρμήγκι.
    def set_starting_node(self, starting_node):
        self.starting_node = starting_node

    # Ορίζει τον τρέχων κόμβο
    def set_located_node(self, located_node):
        self.located_node = located_node

    # Ορίζει την λίστα με τους επιτρεπτόμενους κόμβους.
    def set_allowed_nodes(self, allowed_nodes):
        self.allowed_nodes = allowed_nodes

    # Ορίζει την λίστα με τους κόμβους που έχει επισκευφτεί το μηρμήγκι.
    def set_tour(self, tour):
        self.tour.append(tour)

    # Επιστρέφει τον αριθμό απο το μυρμήγκι.
    def get_ant_id(self):
        return self.ant_id

    # Επιστρέφει τον αρχικό κόμβο.
    def get_starting_node(self):
        return self.starting_node

    # Επιστρέφει τον τρέχων κόμβο.
    def get_located_node(self):
        return self.located_node

    def get_allowed_nodes(self):
        """
        Επιστροφή λίστας με τους επιτρεπτόμενους κόμβους.
        :return: Λίστα
        """
        return self.allowed_nodes

    # Επιστρέφει την λίστα με τους κόμβος που έχει επισκεφτεί.
    def get_tour(self):
        return self.tour

    @staticmethod
    def initialize_allowed_nodes(dimension):
        """
        Αρχικοποίηση των κόμβων που επιτρέπεται να επισκεφτεί το κάθε μυρμήγκι.
        :param dimension: Η διάσταση του προβλήματος(ακέραιος).
        :return: 'Εναν πίνακα με τους κόμβους που επιτρέπεται να επισκεφτεί το μυρμήγκι.
        """
        allowed_nodes = []
        for node in range(0, dimension):
            allowed_nodes.append(node)
        return allowed_nodes

    @staticmethod
    def transition_probability(located_node, next_node, alpha, beta, pheromone, visibility, allowed):
        """
        Σε αυτη την μέθοδο υπολογίζεται η πιθανότητα να παει ένα μυρμήγκι απο την πόλη i στην πόλη j :
        p(i|j) = pheromone[i,j] ^ α  *  visibility[i,j] ^ β / Σ pheromone[i,allowed_towns] ^  *
                visibility[i,allowed_nodes] jE allowed nodes
        p(i|j) = 0
        :param located_node:Ο τρέχον κόμβος ποου βρίσκεται το μυρμίγκι (ακέραιος).
        :param next_node:Ο επόμενος κόμβος που μπόρει να επισκεφτεί (ακέραιος).
        :param alpha:Μια παράμετρος πραγματικός αριθμός.
        :param beta:Μια παράμετρος πραγματικός αριθμός.
        :param pheromone:Η φεροόνη στις ακμές μεταξύ των κόμβων(πίνακας).
        :param visibility:Η "ορατότητα" στις ακμές μεταξύ των κόμβων(πίνακας)
        :param allowed: Οι κόμβοι που επιτέπεται να πάει το μυρμήγκι(Λίστα)
        :return: Πιθανότητα πραγματικός αριθμος.
        """
        # Αν ο επόμενος κόμβος βρίσκεται στη λίστα με τους κόμβους που επιτρέπεται να πάει το μυρμήγκι.
        if next_node in allowed:
            # Η φερομόνη στην ακμή απο τον κόμβο i στον j
            pheromone_i_j = pheromone[located_node][next_node] ** alpha
            # "ορατότητα" στην ακμή απο τον κόμβο i στον j
            visibility_i = visibility[located_node][next_node] ** beta
            a = pheromone_i_j * visibility_i

            # Η φερομόνη σε όλες τις ακμές απο τον κόμβο i προς στις πόλεις που επιτρέπεται
            pheromone_all = pheromone[located_node][allowed] ** alpha
            # Η ορατόττητα σε όλες τις ακμές απο τον κόμβο i προς στις πόλεις που επιτρέπεται
            visibility_all = visibility[located_node][allowed] ** beta
            b = sum(pheromone_all * visibility_all)

            return a / b

        else:
            return 0
