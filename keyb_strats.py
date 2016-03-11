import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from Strategies import *

from Outils import *


def shoot_nord(me):
	return me.shoot_but_nord

def shoot_sud(me):
	return me.shoot_but_sud

def shoot_malin(me):
	return me.shoot_malin

def shoot_centre(me):
	return me.shoot_vers_norm(me.but_pos_adv,5.0)

def dribbler_vers_but(me):
	return me.dribbler_vers(me.but_pos_adv)

def dribbler_vers_zone_tir(me):
	return me.dribbler_vers(me.zone_tir)

def piquer(me):
	return me.piquer_balle

def degager(me):
	return me.degager

def pos_defaut(me):
	return courir_vers(me.ball_pos-Vector2D(x=5,y=0)

keystrat_test= KeyboardStrategy()

Strat_posdef = SousStrat(pos_defaut)
keystrat_test.add("a",Strat_posdef)

Strat_shoot_nord = SousStrat(shoot_nord)
keystrat_test.add("y",Strat_shoot_nord)

Strat_shoot_sud = SousStrat(shoot_sud)
keystrat_test.add("h",Strat_shoot_sud)

Strat_shoot_centre = SousStrat(shoot_centre)
keystrat_test.add("g",Strat_shoot_centre)

Strat_dribble_but = SousStrat(dribbler_vers_but)
keystrat_test.add("q",Strat_dribble_but)

Strat_dribble_zonetir = SousStrat(dribbler_vers_zone_tir)
keystrat_test.add("s",Strat_dribble_zonetir)

Strat_degager = SousStrat(degager)
keystrat_test.add("d",Strat_degager)



