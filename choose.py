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


team_a =SoccerTeam("Priyaa",[Player("rient1",Rien_Strat),Player("Gard",Gardien_Strat)])
team_fou =SoccerTeam("team_fou",[playerChoose,Player("Gard",Gardien_Strat)])
"""

dic = {"fonceur":Fonceur_Strat, "rien":Rien_Strat}
la_qstrat= QStrategy


match = SoccerMatch(team_a, team_fou)
soccersimulator.show(match)

