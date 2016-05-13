import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from Strategies import *
from StratsSpecialise import*
from Outils import *




def degager(me):
	res=me.degager
	res.name="degager"
	return res




#######################################

KBS_Milieu = KeyboardStrategy()
KBS_Milieu.add("d",Def4vs4_Strat)
KBS_Milieu.add("g",Attack4vs4_Strat)



########################################	
Strat_protect= SousStrat(protect_cage)
Strat_passe = SousStrat(passe)
Strat_allign= SousStrat(alligne_demi_cercle)
Strat_deg= SousStrat(degager)

KBS_Gard= KeyboardStrategy()
KBS_Gard.add("x", Strat_allign)
KBS_Gard.add("c", Strat_protect)

KBS_Gard.add("s", Strat_passe)
KBS_Gard.add("d", Strat_deg)

#######################################






