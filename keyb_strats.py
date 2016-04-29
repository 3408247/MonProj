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
	return me.degager

def pos_defaut(me):
	return me.placerEntre_A_B_x(me.ball_pos,me.but_pos,GAME_WIDTH/4)
	#return me.courir_vers(me.ball_pos-Vector2D(x=5,y=0))
def suivre_balle(me):
	return suivre_balle(me)

def gardien(me):
	return gardien_mouvement(me)
	

keystrat_test= KeyboardStrategy()

#Strat_posdef = SousStrat(pos_defaut)
#keystrat_test.add("a",Strat_posdef)



Strat_shoot_nord = SousStrat(shoot_nord)
keystrat_test.add("y",Strat_shoot_nord)

Strat_shoot_sud = SousStrat(shoot_sud)
keystrat_test.add("h",Strat_shoot_sud)


Strat_dribble_but = SousStrat(dribbler_vers_but)
keystrat_test.add("d",Strat_dribble_but)

Strat_esq_haut= SousStrat(esquive_en_haut)
keystrat_test.add("u",Strat_esq_haut)

Strat_esq_bas= SousStrat(esquive_en_bas)
keystrat_test.add("j",Strat_esq_bas)

Strat_pos_gard = SousStrat(gardien)
keystrat_test.add("s",Strat_pos_gard)

Strat_degager = SousStrat(degager)
keystrat_test.add("f",Strat_degager)

Strat_piquer = SousStrat(piquer)
keystrat_test.add("b",Strat_piquer)


KBS = KeyboardStrategy()
Strat_demarquer= SousStrat(demarquer)
KBS.add("d",Strat_demarquer)

Strat_deg= SousStrat(degager)
KBS.add("e",Strat_deg)




