import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from Strategies import *
from StratsSpecialise import*
from Outils import *




def shoot_malin(me):
	return me.shoot_malin

def demarque(me):
	if me.ball_pos.x>=GAME_WIDTH/2:
		return demarquer(me)
	else:
		return me.placerEntre_A_B_x(me.ball_pos,me.but_pos_adv,3*GAME_WIDTH/4)

def drib(me):
	if me.dans_zone_de_tir:
		return me.dribbler_vers(me.but_pos_adv)
	else:
		return me.dribbler_vers(me.zone_tir)


def degager(me):
	res=me.degager
	res.name="degager"
	return res

Strat_deg= SousStrat(degager)


def pos_defaut(me):
	return me.placerEntre_A_B_x(me.ball_pos,me.but_pos,GAME_WIDTH/4)
	#return me.courir_vers(me.ball_pos-Vector2D(x=5,y=0))
def suivre_balle(me):
	return suivre_balle(me)

def gardien(me):
	return gardien_mouvement(me)


#######################################

KBS_Milieu = KeyboardStrategy()
KBS_Milieu.add("d",Def4vs4_Strat)
KBS_Milieu.add("g",Attack4vs4_Strat)


#######################################

Strat_Demarque= SousStrat(demarque)
Strat_Drib = SousStrat(drib)
Strat_Passe = SousStrat(passe)
Strat_Shoot = SousStrat(shoot_malin)



KBS_att4vs4 = KeyboardStrategy()
KBS_att4vs4.add("b",Strat_Demarque)
KBS_att4vs4.add("c",Strat_Passe)
KBS_att4vs4.add("h",Strat_Drib)
KBS_att4vs4.add("d",Strat_Shoot)


########################################	
Strat_protect= SousStrat(protect_cage)
Strat_passe = SousStrat(passe)
Strat_allign= SousStrat(alligne_demi_cercle)


KBS_Gard= KeyboardStrategy()
KBS_Gard.add("x", Strat_allign)
KBS_Gard.add("c", Strat_protect)

KBS_Gard.add("s", Strat_passe)
KBS_Gard.add("d", Strat_deg)

#######################################






