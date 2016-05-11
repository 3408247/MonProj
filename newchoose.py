from Strategies import*
from StratsSpecialise import *
from soccersimulator import SoccerTeam, Player
import os
#from newqlearn import *
from newqstrat import *

team_qa= SoccerTeam("teamq",[Player("PlayerQ",Q_Strat),Player("Garda",Gardien_Strat)])
team_bb = SoccerTeam("team_bb",[Player("rientb",Rien_Strat),Player("Gardb",Gardien_Strat)])

matchfuck=SoccerMatch(team_qa,team_bb)
soccersimulator.show(matchfuck)

maj(matchfuck,1,1,NOM_FICHIER_DIC)
