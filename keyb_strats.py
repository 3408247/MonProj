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


def dribbler(me):
    if me.test_peut_shooter:
	return me.dribbler_vers(me.but_pos_adv)
    else:
	return me.courir_vers_ball

def courir_malin(me):
	return me.courir_vers_ball

def rien(me):
	return SoccerAction()

def degager(me):
	if me.test_peut_shooter:
		return me.shoot_degager
	else:
		return me.courir_vers_ball

keystrat_test= KeyboardStrategy()


Strat_dribble = SousStrat(dribbler)
keystrat_test.add("d",Strat_dribble)

Strat_shoot_nord = SousStrat(shoot_nord)
keystrat_test.add("y",Strat_shoot_nord)

Strat_shoot_sud = SousStrat(shoot_sud)
keystrat_test.add("h",Strat_shoot_sud)

#Strat_shoot_malin = SousStrat(shoot_malin)
#keystrat_test.add("b", Strat_shoot_malin)

Strat_degager = SousStrat(degager)
keystrat_test.add("c",Strat_degager)

Strat_rien = SousStrat(rien)
keystrat_test.add("a",Strat_rien)
