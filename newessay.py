from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from newqkbs import *
from StratsSpecialise import *
from newqlearn import *
import pickle

t1= SoccerTeam("Qq",[Player("QPlayer",QStrat)])
t2 = SoccerTeam("Adv",[Player("j1",J_1vs1_Strat)])

mat = SoccerMatch(t1,t2)
#soccersimulator.show(mat)
print
cpt = 0
while cpt<=0:
    print "CPT", cpt
    print "      "

    print "BEGIN match.play()"
    #mat.play()
    soccersimulator.show(mat)
    print "      "
    print "### FIn match.play Now MAJ ##"


    # FAIRE LA MISE A JOUR APRES AVOIR JOUE MATCH 
    maj(mat,1,0,NOM_FICHIER_DIC)
    print " ## FIN MAJJJ##"

    print "CA CETAIT POUR MATCH CPT", cpt

    cpt+=1

print "FIN FINALE"
