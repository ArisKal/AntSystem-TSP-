import xml.etree.ElementTree as ET
import numpy as np


class ReadData:
    """
    Κλάση ReadData η οποία θα διβάζει τα προβλήματα (TSP) σε μορφή *.xml και τα μετρέπει σε πίνακα (n*n) n = διάσταση
    προβλήματος.
    Ta προβλήματα μπρούν να κατέβουν απο τον ιστότοπο:
    http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/XML-TSPLIB/instances/.
    ΠΛηροφορίες για τη δομή του xml στον ιστότοπο:
    http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/XML-TSPLIB/Description.pdf

    -self.name_of_file: Το όνομα του αρχείου.
    -self.tree:To δέντρο του xml
    """

    def __init__(self, name_of_file):
        """
        Ορίζει το όνομα του αρχείου *.xml
        :param name_of_file: το όνομα του αρχείου.
        """
        self.name_of_file = name_of_file
        self.tree = ET.parse(name_of_file)

    def set_name_of_file(self, name_of_file):
        """
        Ορίζει το όνομα του αρχείου *.xml
        :param name_of_file: το όνομα του αρχείου.
        """
        self.name_of_file = name_of_file

    def set_tree(self, name_of_file):
        """
        Διαβάσμα αρχείου *.xml και επιστροφή του δέτρου.
        :param name_of_file:Το όνομα του αρχείου
        :return:Επιστοφή δέντρου
        """
        self.tree = ET.parse(name_of_file)
        return self.tree

    def get_name_of_file(self):
        """
        Επιστροφή του ονόματος του αρχειου.
        :return: Όνομα αρχείου
        """
        return self.name_of_file

    def get_tree(self):
        """
        Επιστροφή του δέντρου του xml.
        :return: Επιστροφή του δέντρου του xml.
        """
        return self.tree

    def get_cost_matrix(self):
        """
        Δημιουργία του γράφου σε αυτή την μέθοδο απο το αρχείο βρήσκουμε τα κόστη και να εισχωρούε σε ενα πίνακα d*d
        οι διαγώνιες τιμές είναι 0
        Απο το αρχείο xml απο το tag edge μπορούμε να πάρουμε τα κόστη.
        :return:
        """
        tree = self.tree
        root = tree.getroot()
        dimension = 0
        for vertex in root.iter('vertex'):
            dimension += 1
        # Δημιουργία πίνακα dimension * dimension γεμάτος με 0
        arr = np.zeros((dimension, dimension))
        # Ορίζω τον δείκτη της γραμμής με 0
        row = 0
        # Ορίζω τον δείκ"τη της στήλης με 0
        column = 0
        # Για κάθε tag edge:
        for edge in root.iter('edge'):
            """
            Όταν ο δείτης την γραμμής είναι ίδιος με τον δείκτη της στήλης
            τοτε στον πίνακα γίνεται εισχώρηση του 0 και ο δείκτης της στήλης αυξανεται κατά 1
            """
            if row == column:
                arr[row][column] = 0
                column += 1

            #  Όταν ο δείκτης της γραμμής και της στήλης δεν είναι όμοιοι τότε εισχωρείται το κόστος
            if row != column:
                # Απο το tag 'vertex' πάρε το attribute 'cost'(έναι ένας πραγματικός αριθμος)
                arr[row][column] = edge.get('cost')
                column += 1
                # Οταν ο δείκτης της στήλης φτάσει στο τέλος τοτε αλλάζουμς γραμμή αυξάνοντας κατά 1 και μηδέζεται η
                # στήλη
            if column == dimension:
                column = 0
                row += 1
            # if row == dimension:
            #     break
        return arr

    @staticmethod
    def get_dimension(data):
        """
        Μέθοδος που επιστέφει την διάσταση του προβήματος, Κάθε αρχείο .xml περιέχει το tag "vertex" όσα "vertex"
        έχει το αρχείο τόσοι έιναι και οι κομβοι άρα και η διάσταση του προβλήματος είναι οι κομβοι. :param data:Το
        δεδομένα του αρχείου. :return:Επιστρέφει την διάσταση του προβηματος
        """
        count = 0
        tree = data
        root = tree.getroot()
        # Για όλο το αρχείο όταν βρήκει την λέξη "vertex" αύξησε τον μετρητή κατά 1.
        for vertex in root.iter('vertex'):
            count += 1
        return count

