from Strategies import*
from StratsSpecialise import *
from soccersimulator import SoccerTeam, Player
import os
#from newqlearn import *
from newqstrat import *

team_qa= SoccerTeam("teamq",[Player("PlayerQ",Q_Strat),Player("Def",DefStrat)])
team_bb = SoccerTeam("team_bb",[Player("Def",DefStrat),Player("Def",DefStrat)])

matchfuck=SoccerMatch(team_qa,team_bb)
soccersimulator.show(matchfuck)

maj(matchfuck,1,1,NOM_FICHIER_DIC)
