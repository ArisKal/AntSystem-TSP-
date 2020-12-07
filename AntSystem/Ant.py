
class Ant:
    """
    Κλάση Ant περιέχει όλα τα χαρακτηρηστικά του μηρμηγκιού
    - self.ant_number: είναι ο μοναδικός χαρακτηριστικός αριθμος που έχεο το κάθε μηρμήγκι.
    - self.starting_node: είναι ο κόμβος απο τον οποίο θα ξεκινησει το μυρμήγκι.
    - self.located_nodes: έναι ο κόμβος που βρήσκεται κάθε στιγμή το μυρμήγκι.
    - self.allowed_noded: είναι μία λίστα με τους κόμβους που επριτρέπεται να επισκεφτει το μηρμήγκι.
    - self.tour: είναι μία λίστα με τους κόμβους που έχει επισκεφτει το μηρμήγκι.

    :param ant_number o αριθμός του μηρμηγκιού.
    :param starting_node o αρχικός κόμβος που τοποθετειται το μηρμήγκι,
    """

    # Κατασκευαστής
    def __init__(self, ant_number, starting_node):
        self.ant_number = ant_number
        self.starting_node = starting_node
        # Στον κατασκευαστή ο τρέχων κόμβος είναι και ο αρχικός κόμβος.
        self.located_node = starting_node
        # Κένή λίστα που θα περιέχει τους κόμβος που επριτρέπεται να επισκεφτει το μηρμήγκι.
        self.allowed_nodes = list()
        # Κενή λίστα με τους κόμβους που έχει επισκεφτει το μηρμήγκι.
        self.tour = list()

    # Ορίζει ένας αριθμό στο μυρμήγκι.
    def set_ant_number(self, ant_number):
        self.ant_number = ant_number

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
        self.tour = tour

    # Επιστρέφει τον αριθμό απο το μυρμήγκι.
    def get_ant_number(self):
        return self.ant_number

    # Επιστρέφει τον αρχικό κόμβο.
    def get_starting_node(self):
        return self.starting_node

    # Επιστρέφει τον τρέχων κόμβο.
    def get_located_node(self):
        return self.located_node

    # Επιστρέφει την λίστα με τους κόμβος που έχει επισκεφτεί.
    def get_tour(self):
        return self.tour

    @staticmethod
    def add_node(a_list, node):
        """
        Προσθέτει στην λίστα εναν κόμβο
        και την επιστρέφει.
        :param a_list: Μία λίστα (list())
        :param node: ο κόμβος (int)
        :return: Επιστρέφει την λίστα με τον επιπλέον κλομβο
        """
        a_list.append(node)
        return a_list

    @staticmethod
    def remove_node(a_list, node):
        """
        Αφαιρεί απο την λίστα εναν κόμβο
        και την επιστρέφει.
        :param a_list: Μία λίστα (list())
        :param node: ο κόμβος (int)
        :return: Επιστρέφει την λίστα με τον λιγότερο κλομβο
       """
        a_list.remove(node)
        return a_list
