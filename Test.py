import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import SoccerTeam, SoccerMatch, Player
from strattest import *
from StratsSpecialise import*


team1b =SoccerTeam("team1b",[Player("gard",Gardien_Strat),Player("atta",Attack4vs4_Strat),Player("milieu",Milieu4vs4_Strat),Player("def",Def4vs4_Strat)])
 
team1a =SoccerTeam("team1a",[Player("atta",Attack4vs4_Strat),Player("def",Def4vs4_Strat),Player("gard",Gardien_Strat),Player("TEST",Complexe_Strat)])

match = SoccerMatch(team1b, team1a)
#SoccerMatch.save(match,"fichier.match")
soccersimulator.show(match)
