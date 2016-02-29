import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament

from Outils import *
from Strategies import *

keystrat_test= KeyboardStrategy()
keystrat_test.add("d",Strat_dribble)
keystrat_test.add("s",Strat_shoot)
