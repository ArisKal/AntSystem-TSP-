### Introduction 
Σε αυτό τον αλγορίθμο θα λύσουμε το πρόβλημα του **πλανόδιου πωλητή(TSP)** με τον μαθευρετικό αλγόριθμο **AntSystem(ACO)** ο οποίος προτάθηκε απο τον **Marco Dorigo** το 1992 στο διδακτορικό του. είναι μια τεχνική πιθανοτήτων για την επίλυση υπολογιστικών προβλημάτων για την εύρεση καλών διαδρομών σε ένα γράφημα.  
Τα τεχνητά μυρμήγκια στον αλγόριθμο έχουν συμπεριφορά που είναι εμπνευσμένη απο τα πραγματικά μυρμήγκια,για παράδειγμα η επικοινωνία μεταξύ των βιολογικών μιρμηγκιών βασίζεται σε μια ουσία που ονομάζεται **φερομόνη** έτσι και στα τεχνιτά μυρμήγκια.  
Τα πραγματικά μυρμήγκια  αναπτήσουν μια τεχνική για να βρούν την συντομότερη διαδρομή απο την φωλιά τους προς την πηγή της τροφλης και αντιθέτως.  
Τα τεχνιτά μυρμήγκια καταγράφουν τις θέσεις τους και την ποιότητα της λύσεις,έτσι σε κάθε επανάληψη του αλγορίθμου να βρίσκουν καλύτερες λύσεις.  
Ο αλγόριμος **AntSystem** είναι ένας αλγόριθμος που ανήκει στην "οικογένεια" των αλγορίθμων **Swarm Intelligence**.   

### The Ant System
Αρχικά έχουμε $n$ πόλεις το $d_{ij}$ είναι η απόσταση μεταξύ την πόλης $i$ και της πόλης $j$ .Το $b_i(t)=(i-1,...,n)$ είναι ο αριθμός των μυρμηγκιών στην πόλη $i$ την δεδομένη στιγμή $t$ και $m=\sum_{i=1}^{n} b_i(t)$ είναι ο συνόλικός αριθμός των μυρμληγκιών.Κάθε μύρμήγκι έχει τα παρακάτω χαρακτηριστηκά:  

* διαλέγει την επόμενη πόλη με μια ποθανότητα είναι σε συνάρτηση με την απόσταση των πόλεων και την ποσότητα της φερομόνης στην ακμή που συνδέει τις δύο πόλεις.    
* το μυρμήγκι έχει μνήμη θυμάται κάθε πόλη που έχει επισκεφτεί τις αποθηκεύει σε μία λίστα και μπορεί να επεισκεφτει **μονο** τις πόλείς που δεν έχει επισκέφτεί ακόμα.  
* μόλις ολοκληρώσει την διαδρομόμη του αφήνει την φερομόνη στις ακμές$(i,j)$ που έχει επισκεφτεί.  

Το $T_{i,j}(t)$ είναι η ένταση της φερομόνης στην ακμή $(i,j)$ την στιγμή $t$.
Κάθε μυρμήγκι την στιγμή $t$ επιλέγει την επόμενη οταν $t+1$.Μια επανάληψη του αλγορίθμου είναι $m$ κινήσεις που γίνονανται απο $m$ μυρμήγκια στο διάστημα $(t,t+1)$,τοτε σε $n$ επαναλήψεις του αλγορίθμου(εδω το ονομάζουμε cycle) κάθε μυρμήγκι έχει ολοκλήρώσει ενα tour.Και σε αυτο το σημέιο  η ένταση της φερομόνης ανανεώνεται απο την παρακάτω φόρμουλα:  
$T_{ij}(t+n)=(ρ-1)(t)+ΔT_{ij}$ (1)   
όπου:

* $ρ$ είναι η  εξάτμιση της φερομόνης στον χρόνο $t$ και $t+n$  
* $ΔT_{i,j} = \sum_{k=1}^m ΔT_{i,j}^k$ (2)  

Όπου το $ΔT_{i,j}^k$ είναι η ποσότητα της φερομόνης στις ακμές $(i,j)$ από το $k$ μυρμήγκι ανάμεσα την χρονική στιγμή $t$ και $t+n$ αυτο δίνεται απο τον τύπο:

$ΔΤ_{i,j}^k = Q/L_k$ (3)   
*αλλιώς:*  
$ΔΤ_{i,j}^k = 0$ (3)  

όπου:  
το $Q$ είναι μια σταθερά και $L_k$ είναι το μήκος της συνολικής διαδρομής που έκανε το $k$ μυμρήγκι.  

το $ρ$ πρέπει να ειναι $<1$  
Για να επισκεφτούν όλα τα μυρμήγκια όλες τις πόλεις κάθε μυρμήγκι έχει μία λίστα(list) που αποθηκεύει τις πόλεις που έχει επισκέφτεί τον χρόνο $t$ kκαι απογορεύει στο μυρμήγκι να επισκεφτεί ξανά αυτή την πόλη πριν ολοκλήρώσει μια επανάληψη ενα tour δηλαδη.Οταν το μυρμήγκι ολοκηρώσει το tour τοτε η λίστα αδειάζει.  

Ορατότητα ονομάζεται **visiblity** $n_{i,j}$ είναι η ποσότητα $1/d_{i,j}$.H ορατότηα δεν αλλάζει καθώς τρέχει ο αλγόριθμος όπως η φερομόνη.

Ορίζουμε την πιθανότητα μετάβασης  απo την πόλη $i$ στη πόλη $j$ για κάθε μυρμήγκι $k$
απο τον τυπο:

$p_{i,j}(t)^k = [Τ_{i,j}(t)]^α * [n_{i,j}]^β / \sum_{k\in allowed_k}$ (4)  
αν το $j \in allowed_k$

αλλιώς:  
$p_{i,j}(t)^k = 0$ (4)  

Όπου $allowed_k = [N-list]$ και το $α$ και το $β$ είναι παράμετροι που ελέγχουν την σημασία της φερομόνης εναντίον της ορατότητας.  

### Αλγόριθμος(δικιά μου υλοποίηση)
Ο αλγόριθμος ονομάζεται ant-cycle
Αρχικα την χρονικη στιγμή 0 να μυρμήγκια το τοποθετούνται σε διαφορετικες πόλεις και με αρχικη τιμη $t_{i,j}$ για την φερομόνη στις ακμές του γράφου.
Δημηουργρία μιας λίστας για κάθε μυρμήγκι που θα περιέχει όλες τις πόλεις που επιτρέπεται να επισκεφτει το μυρμήγκι.Η πρώτη πόλη που τοποθετείται το μυρμήγκι θα αφαιρεθεί και απο την λίστα.Καθε κίνη που κάνει το μυρμήγκι για να μετακινηθεί απο την πόλη $i$ προς την  πόλη $j$ υπολογίζεται απο τον τύπο (4) με παράμετρο $α$ και $β$ το $Τ_{i,j}$ δίνει την πληροφορία για τα πόσα μυρμήγκια έχουν περάσει απο την ακμή $i,j$  και το $n_{i,j}$ δίνει την πληροφορία πόσο κοντα είναι στην πόλη.Προφανώς αν το $α=0$ η φερομόνη πλέον δεν παίζει ρόλο και ο αλγόριθμος γίνεται stohastic greedy.

Μετα απο n επαναλήψεις ολα τα μυρμήγκια έχουν ολοκληρώσει τις διαδρομές τους οι λίστες είναι άδειες,σε αυτο το σημείο υπολογίζουμε για κάθε μυρμήγκι το $L_k$ και ύστερα υπολογίζονται οι τιμές $ΔΤ_{i,j}^k$ και ενημερώνονται απο το τύπο 3.Επίσης η μικρότερη διαδρομή που βρίσκεται απο τα μυρμήγκια(π.χ $min L_k, k = 1,....,m)$ αποθηκεύεται και όλες οι λίστες ξαναγεμίζουν με όλες τις πόλεις του γράφου.Αυτη η διαδικασία συνέχίζεται μέχρι ο αριθμός των κύκλων φτάσει στο μέγιστο $NC_{MAX}$ ή όταν ολα τα μυρμήγκια ακολουθούν την ίδια διαδρομή stagnation ονομάζεται αυτη η συμπεριφορά.  

### Ψευδοκώδικας
1. Initialize:  
    Για κάθε ακμή $(i,j)$ βάλε αρχική τιμή $T_{i,j}=c$ για την φερομόνη και $ΔΤ_{i,j} = 0$  
    Γέμισε την λίστα(visited_towns) για κάθε μυρμήγκι για όλες τις πόλεις του γράφου  
    Tοποθέτησε m μυμρηγκιών σε n κόμβους.  
    

2. Για κάθε μυρμήγκι {k=1 to m}:    
    Αφαίρεσε απο την λίστα την αρχική πόλη.

3. Για κάθε μυρμήγκι {k=1 to m}:  
    Μέχρι να αδιάσει η λίστα {town=1 to n-1}:  
            Υπολόγισε την πιθανότητα απο τον τύπο $p_{i,j}^k$ απο τον τύπο(4) και εισχωρήσε την σε μία λίστα(probalities).  
            Επέλεξε την επόμενη πόλη*  
            Μετακίνησε το μυρμήγκι στην επόμενη πόλη j.  
            Εισχώρησε στη λίστα(tour) την πόλη
            Διέγραψε απο την λίστα(allwed_towns) την πόλη j.  

4. Για κάθε μυρμήγκι {k=1 to m}:  
   Μετακίνησε το k μυρμήγκι στην αρχική πόλη και προσθεσέτη στην λίστα(tour)  
   Υπολόγισε το $L_k$ για την διαδρομη του μυρμήγκιου κ.  
   Ενημέρωσε την συνομότερη διαδρομή  
   Για κάθε ακμή(i,j):
   Για κάθε μυρμήγκι:

    $ΔΤ_{i,j}^k = Q/L_k$  
    *αλλιώς:*  
    $ΔΤ_{i,j}^k = 0$

    $ΔΤ_{i,j} = ΔΤ_{i,j} + ΔΤ_{i,j}^k$  

5. Για κάθε ακμή $(i,j)$ υπολόγισε:  
$T_{i,j} = ρ * T_{i,j} + ΔΤ_{i,j}$   
NC = NC+1
Για κάθε ακμή(i,j):  
$ΔΤ_{i,j} = 0$ 

6.Αν το ($NC<NC_{MAX}$)
Για κάθε μυρμήγκι:
τότε:
 αδειασε τις λίστες(tour)
γέμισε τις λίστες(allowed_towns)
Και πήγαινε στο βήμα 2
αλλιώς
Print την συντομότερη διαδρομή













    






 
 