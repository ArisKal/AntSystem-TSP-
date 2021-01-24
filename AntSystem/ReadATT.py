import numpy as np
import math


class ReadAtt:
    """
    Διαβάζει αρχεία απο τυπου .tsp με EDGE_WEIGHT_TYPE : ATT
    - self.file_name: Όνομα του αρχειου string
    - self.file: Το αρχειο ανοιχτό
    - self.data: Λίστα με τα δεδομένα του αρχείου
    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name)
        self.data = list()
        for line in self.file:
            # Όταν βρεί την γραμμή "NODE_COORD_SECTION" τότε θα αρχίσει να γράφει στην λίστα καθε γραμή.
            if 'NODE_COORD_SECTION' in line:
                for line in self.file:
                    # Όταν βρει "EOF τοτε σταματαει να γράφει στην λίστα.
                    if "EOF" in line:
                        break
                    else:
                        self.data.append(line.split())

    def set_file_name(self, file_name):
        """
        Ορίζε τον όνομα του αρχείου
        :param file_name: String
        """
        self.file_name = file_name

    def open_file(self, file_name):
        """
        Άνοιγμα αρχείου
        :param file_name: string
        """
        self.file = open(file_name)

    def set_data(self, file):
        """
        Αποθηκέυκει τα δεδομένα του αρχειού σε μια λίστα
        :param file: Το αρχείο
        """
        for line in file:
            # Όταν βρεί την γραμμή "NODE_COORD_SECTION" τότε θα αρχίσει να γράφει στην λίστα καθε γραμή.
            if 'NODE_COORD_SECTION' in line:
                for line in file:
                    # Όταν βρει "EOF τοτε σταματαει να γράφει στην λίστα.
                    if "EOF" in line:
                        break
                    else:
                        self.data.append(line.split())

    def get_file_name(self):
        """
        Επιστρέφει το όνομα του αρχείου
        :return: string
        """
        return self.file_name

    def get_file(self):
        """
        Επιστρέφει το αρχείο
        :return: file
        """
        return self.file

    def get_data(self):
        """
        Επιστρέφει την λίστα με τα δεδομένα του αρχειού
        :return: Λίστα με τα δεδόμενα του αρχείου
        """
        return self.data

    def get_cost_matrix(self):
        """
        Επιστρέφει τον πίνακα με τα κόστη μεταξύ των πόλεων,απο τι αρχείο
        :return: Επιστρέφει τον πίνακα με τα κόστη μεταξύ των πόλεων.
        """
        # Λίστα με dictionaries που θα περίεχει τις πόλεις με τις συντεταγμένες.
        cities = list()
        for i in range(0, len(self.data)):
            # Λίστα με τις πόλεις σε dictionary με keys city(το id της πόλης), coord_x(αξονας χ), coord_y(αξονας ψ)
            cities.append(
                {"city": int(self.data[i][0]), "coord_x": int(self.data[i][1]), "coord_y": int(self.data[i][2])})
        # Αύξουσα ταξινόμηση στην λίστα με τις πόλεις ανάλογα με το id της πόλης
        cities = sorted(cities, key=lambda k: k["city"])
        # Δημηουργία πίνακα με τα κόστη
        cost_matrix = np.zeros((len(cities), len(cities)))
        for i in range(0, len(cities)):
            for j in range(0, len(cities)):
                if i == j:
                    # Στα διαγώνια θα έχει την τιμή 0
                    cost_matrix[i][j] = 0
                else:
                    # Υπολογισμος της απόστασης μεταξύ των πόλεων i και j
                    cost_matrix[i][j] = ReadAtt.euclidean_distance(cities[i], cities[j])
        return cost_matrix

    # @staticmethod
    # def pseudo_euclidean_distance(city_i, city_j):
    #     """
    #     Υπολογισμός της αποστασης απο την πόλη i στην πόλη j με την συνάρτηση "pseudo-Euclidean"
    #     tsp95 manual σελ.7
    #     :param city_i:Πόλη i (real)
    #     :param city_j:Πόλη j (real)
    #     :return: Επιστρέφει την αποσταση απο την πόλη i στην πόλη j (real)
    #     """
    #     # Αποσταση μεταξύ των πόλεων ως προς τον άξονα x
    #     xd = city_i["coord_x"] - city_j["coord_x"]
    #     # Αποσταση μεταξύ των πόλεων ως προς τον άξονα y
    #     yd = city_i["coord_y"] - city_j["coord_y"]
    #     rij = math.sqrt((xd * xd + yd * yd) / 10.0)
    #     tij = round(rij)
    #     if tij < rij:
    #         dij = tij + 1
    #     else:
    #         dij = tij
    #     return dij

    @staticmethod
    def euclidean_distance(city_i, city_j):
        """
        Υπολογισμός της αποστασης απο την πόλη i στην πόλη j με την συνάρτηση "Euclidean"
        tsp95 manual σελ.7
        :param city_i:Πόλη i (real)
        :param city_j:Πόλη j (real)
        :return: Επιστρέφει την αποσταση απο την πόλη i στην πόλη j (real)
        """
        # Αποσταση μεταξύ των πόλεων ως προς τον άξονα x
        xd = city_i["coord_x"] - city_j["coord_x"]
        # Αποσταση μεταξύ των πόλεων ως προς τον άξονα y
        yd = city_i["coord_y"] - city_j["coord_y"]
        dij = math.sqrt(math.pow(xd, 2) + math.pow(yd, 2))
        return dij

