
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import SoccerTeam, SoccerMatch, Player
from Strategies import *


   
team1= SoccerTeam("team1",[Player("f1",FonceurStrat),Player("gk1",GkStrat)])
team2= SoccerTeam("team2",[Player("f2",FonceurStrat),Player("gk2",GkStrat)])

match = SoccerMatch(team1,team2)
soccersimulator.show(match)
