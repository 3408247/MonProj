import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament

from Outils import *
SEUIL_BALL_FAR = 40
SEUIL_BALL_CLOSE = 30
SEUIL_BALL_TOO_CLOSE = 10

RAYON = 20


class SousStrat(BaseStrategy):
    def __init__(self,sous_strat):
        BaseStrategy.__init__(self,sous_strat.__name__)
        self.strat=sous_strat 

    def compute_strategy(self,state,idteam,idplayer): #ou faire miroir ici
	self.state = state
     
        action,self.name=self.strat(MyState(self.state,idteam,idplayer))
	#print action
        if(idteam!=1):
	   action= miroir_action(action)

        #print action
        return action,self.name


def bougeversbuts(me):
	print "entre effec bouge"
	
	return me.courir_vers(me.but_pos)

def courir(me):
	print "rentre effec cour"
	return me.courir_vers_ball

def complexe(me):
	print "rentre effec compl"
	if me.ball_pos.x<=GAME_WIDTH/2:
		return courir(me)
	else:
		return bougeversbuts(me)


Complexe_Strat = SousStrat(complexe)


