from Strategies import*
from StratsSpecialise import *
from soccersimulator import SoccerTeam, Player
import os
from qlearn import *

"""
def chooseStrat(name):
	if name=="rien":
		print" dois faire rien strat"
		return Rien_Strat
	else:
		print "doit faire fonceur strat"
		return FonceurStrat


la_strat= chooseStrat('fonceur')
playerChoose = Player("chooseur",la_strat)

"""
team_a =SoccerTeam("Priyaa",[Player("fonceur",Fonceur_Strat),Player("Garda",Gardien_Strat)])
team_b =SoccerTeam("team_b",[Player("rientb",Rien_Strat),Player("Gardb",Gardien_Strat)])





match = SoccerMatch(team_a, team_b)
soccersimulator.show(match)
"""
print "STRATS TAKEN"
print match.strats
"""

dic_corresp = {"fonceur":Fonceur_Strat, "rien":Rien_Strat,"gardien":Gardien_Strat}
la_qstrat= QStrategy(match,1,1,"lala",dic_corresp)

PlayerQ= Player("plqyerQ",la_qastrat)

team_qa= SoccerTeam("teamq",[PlayerQ,Player("Garda",Gardien_Strat)])
team_bb = SoccerTeam("team_bb",[Player("rientb",Rien_Strat),Player("Gardb",Gardien_Strat)])

match2= SoccerMatch(team_qa, team_bb)
soccersimulator.show(match2)
