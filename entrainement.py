from soccersimulator import SoccerMatch, SoccerTournament,KeyboardStrategy
from soccersimulator import SoccerTeam, Player, show
#from strategies import RandomStrategy,FonceurStrategy,DefenseStrategy
from soccersimulator import settings, Vector2D,DecisionTreeClassifier
import cPickle
from Outils import*
from Strategies import *
from keyb_strats import *

team_keyb = SoccerTeam("team_keyb",[Player("KBs", keystrat_test)])

team_bad = SoccerTeam("team_bad",[Player("Gard",Gard_shoot_but)])

## Match d'entrainement et apprentissage de l'arbre

match = SoccerMatch(team_keyb,team_bad,1000)  # On peut changer le nombre de Steps
show(match)
## Sauvegarde des exemples, mettre False a True si concatenation des fichiers
keystrat_test.write("test.exp",False) # METTRE A TRUE FOR APPENDING 

