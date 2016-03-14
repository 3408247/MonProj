## Match d'entrainement et apprentissage de l'arbre

#euh# match = SoccerMatch(team_keyb,team_bad,1000)  # On peut changer le nombre de Steps
#euh#show(match)
## Sauvegarde des exemples, mettre False a True si concatenation des fichiers
#euh#keystrat_test.write("test.exp",False) # METTRE A TRUE FOR APPENDING 


from soccersimulator import SoccerMatch, show, SoccerTeam,Player,KeyboardStrategy
import sys
from Strategies import *
from StratsSpecialise import *
from keyb_strats import *

if __name__=="__main__":
    prefix = "tree"
    if len(sys.argv)>1:
        prefix = sys.argv[1]


    team_keyb = SoccerTeam("team_keyb",[Player("KBs", keystrat_test),Player("GARD2",G_2vs2)])

    team_bad = SoccerTeam("team_bad",[Player("def",DefStrat),Player("GARD",Gard_shoot_but)])  


    match = SoccerMatch(team_bad,team_keyb,2000)
    show(match)
    keystrat_test.write(prefix+".exp",True)
