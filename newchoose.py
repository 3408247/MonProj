from StratsSpecialise import *
from soccersimulator import SoccerTeam, Player
import os
#from newqlearn import *
from newqstrat import *

team_qa= SoccerTeam("team_qa",[Player("PlayerQ",QStrat)])
team_bb = SoccerTeam("team_bb",[Player("J1",Attack2vs2_Strat),Player("ai",Aideur2vs2_Strat)])

matchfuck=SoccerMatch(team_qa,team_bb)
soccersimulator.show(matchfuck)

print "LES STRATS DU MATCH"
print matchfuck.strats

print"FIN"
print"MAINTENANT MAJ"


maj(matchfuck,1,0,NOM_FICHIER_DIC)
