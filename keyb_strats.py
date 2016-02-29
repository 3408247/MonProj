import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from Strategies import *

from Outils import *


def shoot_nord(me):
	y_=(GAME_GOAL_HEIGHT/2)+(GAME_HEIGHT/2)
	v=Vector2D(x=GAME_WIDTH,y=y_)


	if me.test_peut_shooter:
		return me.shoot_norm(v,3.0)
	else:
		return me.courir_vers_ball


def shoot_sud(me):
	y_=(GAME_HEIGHT/2)-(GAME_GOAL_HEIGHT/2)

	v=Vector2D(x=GAME_WIDTH,y=y_)
	
	if me.test_peut_shooter:
	
		return me.shoot_norm(v,3.0)
	else:
		return me.courir_vers_ball


def dribbler(me):
    if me.test_peut_shooter:
	return me.shoot_dribble
    else:
	return me.courir_vers_ball



keystrat_test= KeyboardStrategy()


Strat_dribble = SousStrat(dribbler)
keystrat_test.add("d",Strat_dribble)

Strat_shoot_nord = SousStrat(shoot_nord)
keystrat_test.add("y",Strat_shoot_nord)

Strat_shoot_sud = SousStrat(shoot_sud)
keystrat_test.add("h",Strat_shoot_sud)



