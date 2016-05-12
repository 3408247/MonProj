import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import SoccerTeam, SoccerMatch, Player
from Strategies import *
#from team import *
from StratsSpecialise import*

"""team2a = SoccerTeam("team2a",[Player("attack",Attack2vs2_Strat),Player("Aideur",Aideur2vs2_Strat)])
team2b =SoccerTeam("team2b",[Player("j1",J_1vs1_Strat),Player("Gard",Gardien_Strat)])
 
team1a =SoccerTeam("team1a",[Player("Gard",Gardien_Strat)])
"""
team1b =SoccerTeam("team1b",[Player("j1",Euh_Strat)])
 
team1a =SoccerTeam("team1a",[Player("Def",DefStrat)])

match = SoccerMatch(team1b, team1a)
#SoccerMatch.save(match,"fichier.match")
soccersimulator.show(match)

print match.strats
#match2 = SoccerMatch.load("fichier.match")

#soccersimulator.show(match2)

"""
print "STRATS"
print match.strats

print "LENGTH STRATS"
print len(match.strats)

print "STATES"
print match.states

print "LENGTH"
print len(match.states)
"""


