#euh#from soccersimulator import SoccerMatch, SoccerTournament,KeyboardStrategy
#euh#from soccersimulator import SoccerTeam, Player, show
#from strategies import RandomStrategy,FonceurStrategy,DefenseStrategy
#euh#from soccersimulator import settings, Vector2D,DecisionTreeClassifier
#euh#import cPickle
#euh#from Outils import*
#euh#from Strategies import *
#euh#from keyb_strats import *


## Match d'entrainement et apprentissage de l'arbre

# euh #

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

    team_keyb = SoccerTeam("team_keyb",[Player("KBs", keystrat_test)])

    team_bad = SoccerTeam("team_bad",[Player("Gard",J_1vs1_Strat)])    


    match = SoccerMatch(team_keyb,team_bad,1000)
    show(match)
    keystrat_test.write(prefix+".exp",True)
