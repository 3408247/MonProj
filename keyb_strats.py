import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from Strategies import *
from StratsSpecialise import*
from Outils import *


def shoot_nord(me):
	return me.shoot_but_nord

def shoot_sud(me):
	return me.shoot_but_sud

def shoot_malin(me):
	return me.shoot_malin

def shoot_centre(me):
	return me.shoot_vers_norm(me.but_pos_adv,6.0)

def dribbler_vers_but(me):
	s=me.but_pos_adv-me.ball_pos
	s.norm=0.5
	
	if me.test_peut_shooter:
		return me.courir_vers_ball2+SoccerAction(Vector2D(),s)
	else:	
		return me.courir_vers_ball2

def dribbler_vers_zone_tir(me):
	if (me.dans_zone_de_tir==True):
		print "DANS ZONE DE TIR"
	return me.dribbler_vers(me.zone_tir)

def esquive_en_haut(me):
	s=me.but_pos_adv-me.ball_pos
	s.norm=0.7

	if me.test_peut_shooter:
		s.angle=s.angle+0.6
		return SoccerAction(Vector2D(),s)
	else:
		return me.courir_vers_ball2

def esquive_en_bas(me):
	s=me.but_pos_adv-me.ball_pos
	s.norm=0.7

	if me.test_peut_shooter:
		s.angle=s.angle-0.6
		return SoccerAction(Vector2D(),s)
	else:
		return me.courir_vers_ball2


def piquer(me):
	return me.piquer_balle

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


Strat_protect= SousStrat(protect_cage)
Strat_passe = SousStrat(passe)
Strat_allign= SousStrat(alligne_demi_cercle)
	

KBS_Gard= KeyboardStrategy()
KBS_Gard.add("x", Strat_allign)
KBS_Gard.add("c", Strat_protect)

KBS_Gard.add("s", Strat_passe)
KBS_Gard.add("d", Strat_deg)




"""
KBS = KeyboardStrategy()
Strat_demarquer= SousStrat(demarquer)
KBS.add("d",Strat_demarquer)

Strat_deg= SousStrat(degager)
KBS.add("e",Strat_deg)

"""


