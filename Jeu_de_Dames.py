from tkinter import *

window = Tk()
window.title('JEU DE DAMES')
taille_case = 70

class Pion:
    couleur = 0  # 0 => Blanc,  1 => noir
    type = 0  # 0 => normal, 1 => dame
    selectionPosition = None
    lastMouvementPion = None

    def __init__(self, couleur=0):
        self.couleur = couleur

    def est_noir(self):
        return self.couleur == 1

    def est_blanc(self):
        return self.couleur == 0

    def est_dame(self):
        return self.type == 1

    def est_de_meme_couleur(self, pion):
        return self.couleur == pion.couleur

    def devient_dame(self):
        """definition de la fonction qui dit qu'un pion est dame ou non
        """
        self.type = 1
        return self

    def affiche(self, canvas, pos_x, pos_y):
        if self.selectionPosition == None:
            self.affichePion(canvas, pos_x, pos_y)

    def afficheMouvement(self, canvas, pos_x, pos_y):
        if self.couleur == 0:
            result = "white"
        else:
            result = "black"
        couleur = result

        if self.selectionPosition != None:
            if self.lastMouvementPion != None:
                canvas.delete(self.lastMouvementPion[0])
                if self.lastMouvementPion[1] != None:
                    canvas.delete(self.lastMouvementPion[1])

            self.lastMouvementPion = [None, None]
            if self.type == 1: #dame on dessine un rond plus petit
                couleurBord = couleur
                if self.couleur == 1:
                    couleurBord = "white"
                self.lastMouvementPion[1] = canvas.create_oval(pos_x + (taille_case) / 2, pos_y + (taille_case) / 2, pos_x - (taille_case) / 2, pos_y - (taille_case) / 2, fill=couleurBord)

            self.lastMouvementPion[0] = canvas.create_oval(pos_x + (taille_case-8) / 2, pos_y + (taille_case-8) / 2, pos_x - (taille_case-8) / 2, pos_y - (taille_case-8) / 2, fill=couleur)

    def affichePion(self, canvas, pos_x, pos_y):
        if self.couleur == 0:
            couleur = "white"
        else:
            couleur = "black"

        if self.type == 1: #dame on dessine un rond plus petit
            couleurBord = couleur
            if self.couleur == 1:
                couleurBord = "white"
            canvas.create_oval(pos_x, pos_y, pos_x + taille_case, pos_y + taille_case, fill=couleurBord)
        canvas.create_oval(pos_x + 4, pos_y + 4, pos_x + taille_case - 4, pos_y + taille_case - 4, fill=couleur)

    def selection(self, x, y):
        self.selectionPosition = (x, y)

    def arret_selection(self):
        print("arret selection of {}".format(str(self)))
        self.selectionPosition = None
        if self.lastMouvementPion != None:
            canvas.delete(self.lastMouvementPion)
            self.lastMouvementPion = None

    def __str__(self):
        if self.couleur == 0:
            if self.type == 0:
                return "pion blanc"
            else:
                return "dame blanche"
        else:
            if self.type == 0:
                return "pion noir"
            else:
                return "dame noire"

class Case:
    couleur = 0  # 0 => Blanc, 1 => noir
    pion = None

    def __init__(self, couleur=0, pion=None):
        self.couleur = couleur
        self.pion = pion

    def est_noire(self):
        return self.couleur == 1

    def selection(self, x, y):
        if (self.pion != None):
            self.pion.selection(x, y)

    def arret_selection(self):
        if (self.pion != None):
            self.pion.arret_selection()

    def __str__(self):
        return "Case {} : {}".format(self.couleur, self.pion)


class Damier:
    damier = [
                 [Case(0), Case(1)] * 5,
                 [Case(1), Case(0)] * 5
             ] * 5


    def __init__(self, damier=None):
        if damier is not None:
            self.damier = damier

    def case(self, x, y):
        if (x >= 0 and x < 10) and (y >= 0 and y < 10):
            return self.damier[y][x]

    def nouveau_jeu(self):
        # initialiser le damier avec les pions pour un début de partie
        # 20 pions, placés sur les cases foncées des 4 premières rangées
        # ??? peut être simplifié avec une boucle ???
        self.damier = [
            [Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0))],
            [Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0)],
            [Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0))],
            [Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(0)), Case(0)],
            [Case(0), Case(1), Case(0), Case(1), Case(0), Case(1), Case(0), Case(1), Case(0), Case(1)],
            [Case(1), Case(0), Case(1), Case(0), Case(1), Case(0), Case(1), Case(0), Case(1), Case(0)],
            [Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1))],
            [Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0)],
            [Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1))],
            [Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0), Case(1, Pion(1)), Case(0)],
        ]

        # # Jeu de test
        # self.damier = [
        #     [Case(0), Case(1), Case(0),          Case(1), Case(0), Case(1), Case(0), Case(1),Case(0), Case(1)],
        #     [Case(1), Case(0), Case(1, Pion(1)), Case(0), Case(1), Case(0), Case(1), Case(0), Case(1), Case(0)],
        #     [Case(0), Case(1), Case(0),          Case(1), Case(0), Case(1, Pion(1)), Case(0), Case(1),Case(0), Case(1)],
        #     [Case(1), Case(0), Case(1),          Case(0), Case(1), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(1)), Case(0)],
        #     [Case(0), Case(1), Case(0),          Case(1), Case(0), Case(1, Pion(1)), Case(0), Case(1),Case(0), Case(1)],
        #     [Case(1), Case(0), Case(1, Pion(1)), Case(0), Case(1), Case(0), Case(1, Pion(0)), Case(0), Case(1), Case(0)],
        #     [Case(0), Case(1), Case(0),          Case(1), Case(0), Case(1), Case(0), Case(1),Case(0), Case(1)],
        #     [Case(1), Case(0), Case(1),          Case(0), Case(1, Pion(0)), Case(0), Case(1), Case(0), Case(1), Case(0)],
        #     [Case(0), Case(1), Case(0),          Case(1, Pion(0)), Case(0), Case(1),Case(0), Case(1),Case(0), Case(1)],
        #     [Case(1), Case(0), Case(1),          Case(0), Case(1), Case(0), Case(1), Case(0), Case(1), Case(0)],
        # ]

        # Jeu de test dame
        """
        self.damier = [
            [Case(0), Case(1), Case(0),          Case(1, Pion(1).devient_dame()), Case(0), Case(1), Case(0), Case(1),Case(0), Case(1)],
            [Case(1), Case(0), Case(1),          Case(0), Case(1), Case(0), Case(1), Case(0), Case(1), Case(0)],
            [Case(0), Case(1), Case(0),          Case(1), Case(0), Case(1, Pion(1)), Case(0), Case(1),Case(0), Case(1)],
            [Case(1), Case(0), Case(1),          Case(0), Case(1), Case(0), Case(1, Pion(0)), Case(0), Case(1, Pion(1)), Case(0)],
            [Case(0), Case(1), Case(0),          Case(1), Case(0), Case(1, Pion(1)), Case(0), Case(1),Case(0), Case(1)],
            [Case(1), Case(0), Case(1, Pion(1)), Case(0), Case(1), Case(0), Case(1, Pion(0)), Case(0), Case(1), Case(0)],
            [Case(0), Case(1), Case(0),          Case(1), Case(0), Case(1), Case(0), Case(1),Case(0), Case(1)],
            [Case(1), Case(0), Case(1),          Case(0), Case(1, Pion(0)), Case(0), Case(1), Case(0), Case(1), Case(0)],
            [Case(0), Case(1), Case(0),          Case(1, Pion(0)), Case(0), Case(1),Case(0), Case(1),Case(0), Case(1)],
            [Case(1), Case(0), Case(1),          Case(0), Case(1), Case(0), Case(1), Case(0), Case(1), Case(0)],
        ]
        """

    def deplacements_possible(self, case_x, case_y):
        case = self.case(case_x, case_y)
        return self.deplacements_possible_pion(case_x, case_y, case.pion, [])

    def deplacements_possible_pion(self, case_x, case_y, pion, deplacements):
        # if pion blanc on descend, sauf pour manger un pion en arrière
        if pion.est_blanc() and not pion.est_dame():
            self.deplacement_possible_pour_pion(case_x, case_y, -1, +1, pion, deplacements)
            self.deplacement_possible_pour_pion(case_x, case_y, +1, +1, pion, deplacements)
            ## Ajouter pour manger en arriere
            self.peut_manger_pion(case_x - 1, case_y - 1, -1, -1, pion, deplacements)
            self.peut_manger_pion(case_x + 1, case_y - 1, +1, -1, pion, deplacements)

        # si pion noir on monte, sauf pour manger un pion en arrière
        elif pion.est_noir() and not pion.est_dame():
            self.deplacement_possible_pour_pion(case_x, case_y, -1, -1, pion, deplacements)
            self.deplacement_possible_pour_pion(case_x, case_y, +1, -1, pion, deplacements)
            ## Ajouter pour manger en arriere
            self.peut_manger_pion(case_x - 1, case_y + 1, -1, +1, pion, deplacements)
            self.peut_manger_pion(case_x + 1, case_y + 1, +1, +1, pion, deplacements)

        # si dame
        else:
            self.deplacements_possible_dame(case_x, case_y, pion, deplacements)

        return deplacements

    def deplacements_possible_dame(self, case_x, case_y, pion, deplacements):
        # dame on descend ou on monte
        for x in range(1, 10):
            for y in range(1, 10):
                # ne prend pas en compte les changements de diagonale
                self.deplacement_possible_pour_pion(case_x, case_y, -1 * x, +1 * y, pion, deplacements)
                self.deplacement_possible_pour_pion(case_x, case_y, +1 * x, +1 * y, pion, deplacements)
                self.deplacement_possible_pour_pion(case_x, case_y, -1 * x, -1 * y, pion, deplacements)
                self.deplacement_possible_pour_pion(case_x, case_y, +1 * x, -1 * y, pion, deplacements)


    def peut_encore_manger_pion(self, case_x, case_y, pion, deplacements):
        if pion.est_blanc():
            self.peut_manger_pion(case_x - 1, case_y + 1, -1, +1, pion, deplacements)
            self.peut_manger_pion(case_x + 1, case_y + 1, +1, +1, pion, deplacements)
            self.peut_manger_pion(case_x - 1, case_y - 1, -1, -1, pion, deplacements)
            self.peut_manger_pion(case_x + 1, case_y - 1, +1, -1, pion, deplacements)

        else: # if pion.est_noir():
            self.peut_manger_pion(case_x - 1, case_y - 1, -1, -1, pion, deplacements)
            self.peut_manger_pion(case_x + 1, case_y - 1, +1, -1, pion, deplacements)
            self.peut_manger_pion(case_x - 1, case_y + 1, -1, +1, pion, deplacements)
            self.peut_manger_pion(case_x + 1, case_y + 1, +1, +1, pion, deplacements)


    def deplacement_possible_pour_pion(self, case_x, case_y, increment_x, increment_y, pion, deplacements):
        # par defaut, mais peut sauter ???
        x_ = case_x + increment_x
        y_ = case_y + increment_y
        deplacement = self.coordonnees_case_disponible(x_, y_)
        if deplacement is not None:
            deplacements.append((deplacement, None))
        else:
            self.peut_manger_pion(x_, y_, increment_x, increment_y, pion, deplacements)

    def peut_manger_pion(self, x_, y_, increment_x, increment_y, pion, deplacements):
        # Faire le test si on peut manger le pion s'il est de l'autre couleur
        case_a_sauter = self.case(x_, y_)
        if case_a_sauter is not None and case_a_sauter.pion is not None and not self.a_ete_sauter(deplacements, case_a_sauter):
            if not case_a_sauter.pion.est_de_meme_couleur(pion):
                deplacement = self.coordonnees_case_disponible(x_ + increment_x, y_ + increment_y)
                if deplacement is not None:
                    # peut on continuer ???
                    # il va falloir stocker tous les pions mangés
                    deplacements_apres = [(deplacement, [case_a_sauter])]
                    self.peut_encore_manger_pion(x_ + increment_x, y_ + increment_y, pion, deplacements_apres)

                    for deplacement_case in deplacements_apres:
                        cases_a_sauter = deplacement_case[1]
                        if cases_a_sauter is not None and case_a_sauter not in cases_a_sauter:
                            cases_a_sauter.append(case_a_sauter)
                        deplacements.append((deplacement_case[0], cases_a_sauter))

    def coordonnees_case_disponible(self, x_, y_):
        case = self.case(x_, y_)
        if (case != None and case.pion == None):
            return (x_, y_)

    def a_ete_sauter(self, deplacements, case_a_sauter):
        # pour tous les déplacements possible du pion déjà calculé
        for deplacement in deplacements:
            cases = deplacement[1]
            # Pour toutes les cases ayant un pion à manger
            if cases is not None:
                for case in cases:
                    if case is not None and case == case_a_sauter:
                        return True
        return False

    def a_manger_tous_les_pions(self, pion, pions_mange):
        nombre_pions_mange = 0
        if pions_mange is not None:
            nombre_pions_mange = len(pions_mange)
        if nombre_pions_mange < self.max_pion_pouvant_etre_mange(pion.couleur):
            return False
        else:
            return True

    def max_pion_pouvant_etre_mange(self, couleur):
        max = 0
        for y in range(10):
            for x in range(10):
                case = self.case(x, y)
                if case.pion is not None and case.pion.couleur == couleur:
                    deplacements_possible = self.deplacements_possible(x, y)
                    for deplacement in deplacements_possible:
                        if deplacement[1] is not None and max < len(deplacement[1]):
                            max = len(deplacement[1])

        print("max_pion_pouvant_etre_mange " + str(max))
        return max


    def __str__(self):
        result = ""

        for numero_ligne in range(10):
            for numero_colonne in range(10):
                result += str(self.case(numero_ligne, numero_colonne))

        return result


def afficher_damier(damier: Damier):
    canvas.delete("all")
    for y in range(10):
        pos_y = y * taille_case
        for x in range(10):
            case = damier.case(x, y)
            if case.est_noire():
                pos_x = x * taille_case
                canvas.create_rectangle(pos_x, pos_y, pos_x + taille_case, pos_y + taille_case, fill="tan")

                if (case.pion != None):
                    case.pion.affiche(canvas, pos_x, pos_y)

def lancer_partie():
    damier.nouveau_jeu()
    afficher_damier(damier)
    global qui_joue
    qui_joue = 0
    afficher_message("Le joueur possédant les pions blancs commence !")

def recommencer_partie():
    canvas.delete("all")
    lancer_partie()


def afficher_message(message):
    texteExplicatif.set(message)

def afficher_message_qui_joue():
    afficher_message("C'est au joueur possédant les " + return_couleur(qui_joue) + "s de jouer")

def return_couleur(couleur):
    if couleur == 0:
        return "blanc"
    else:
        return "noir"

canvas = Canvas(window, height=taille_case * 10, width=taille_case * 10, bg="wheat")
canvas.pack()

texteExplicatif=StringVar()
texteExplicatif.set("Le jeu de dame de Raphaël et Samuel !")

messages = Label(window, textvariable = texteExplicatif, fg='blue')
messages.pack()

bouton = Button(window, text="recommencer partie", command=recommencer_partie)
bouton.pack()

case_selection = None
deplacements = []
qui_joue = 0 #Blanc
damier = Damier()
afficher_damier(damier)
lancer_partie()

def clics_souris (tk_event):
    x, y = tk_event.x, tk_event.y
    #On retrouve la case en faisant une division entière de la position de la souris avec la taille de la case
    case_x = x // taille_case
    case_y = y // taille_case
    case = damier.case(case_x, case_y)
    print("case ({}, {}) {}".format(str(case_x), str(case_y), str(case)))

    global case_selection
    global deplacements
    global qui_joue

    # sélection d'un pion
    if (case_selection == None):
        if case.pion != None and qui_joue == case.pion.couleur:
            case_selection = case
            case.selection(case_x, case_y)
            afficher_damier(damier)

            deplacements = damier.deplacements_possible(case_x, case_y)
            afficher_message_qui_joue()

            print("deplacements = ", str(deplacements))
            if (len(deplacements) == 0):
                afficher_message("Ce pion ne peut pas se déplacer !")
        else:
            afficher_message_qui_joue()
    # on déplace le pion sélectionné si possible
    else:
        if case_selection.pion != None and qui_joue == case_selection.pion.couleur:
            case_selection.arret_selection()

            for deplacement in deplacements:
                if deplacement[0] == (case_x, case_y):
                    if damier.a_manger_tous_les_pions(case_selection.pion, deplacement[1]):
                        case.pion = case_selection.pion
                        case_selection.pion = None

                        # pion devient dame ?
                        if (case.pion.est_blanc() and case_y == 9) or (case.pion.est_noir() and case_y == 0):
                            case.pion.devient_dame()

                        #on change de joueur
                        if case.pion.est_blanc():
                            qui_joue = 1
                        else:
                            qui_joue = 0
                        afficher_message_qui_joue()

                        # supprimer les pions mangés
                        if deplacement[1] is not None:
                            for case in deplacement[1]:
                                case.pion = None

                        break
                    else:
                        afficher_message("Le joueur " + return_couleur(qui_joue) + " n'a pas pris tous les pions")

            deplacements = []
            case_selection = None
            afficher_damier(damier)
        else:
            afficher_message_qui_joue()

def motion(event):
    if case_selection is not None:
        x, y = event.x, event.y
        # print('{}, {}'.format(x, y))
        #montrer que le pion bouge
        if case_selection.pion is not None:
            case_selection.pion.afficheMouvement(canvas, x, y)

canvas.bind("<Button-1>", clics_souris)
canvas.bind('<Motion>', motion)

window.mainloop()
