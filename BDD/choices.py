'''
Created on 28 oct. 2015

@author: Moran
'''
HOMME_STATUT=1
FEMME_STATUT=2
INCONNU_STATUT=0
INCONNU_STATUT_SALLE=0
INCONNU_STATUT_TYPE=4
PROF_STATUT=0
ELEVE_STATUT=1
ADMINISTRATION_STATUT=2
ADMINISTRATEUR_STATUT=3
CLASSE_STATUT=1
LABO_STATUT=2
INFO_STATUT=3

CHOICESNB=[]
for i in range(1,20):
    CHOICESNB.append((i,str(i)))
SALLES = ((INCONNU_STATUT_SALLE, 'Type inconnu'), (CLASSE_STATUT, 'Classe'), (LABO_STATUT, 'Labo'), (INFO_STATUT, 'Info'))
SEXE = ((INCONNU_STATUT, 'Sexe Inconnu'), (HOMME_STATUT, 'Homme'), (FEMME_STATUT, 'Femme'))
TYPE = ((INCONNU_STATUT_TYPE, 'Statut Inconnu'), (PROF_STATUT, 'Prof/Chercheur'), (ELEVE_STATUT, 'Eleve'), (ADMINISTRATION_STATUT, 'Administration'), (ADMINISTRATEUR_STATUT, 'Administrateur Du Site'))