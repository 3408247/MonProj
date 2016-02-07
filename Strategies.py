# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:45:44 2016

@author: 3408247
"""
import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament

from Outils import *
SEUIL_BALL_FAR = 40
SEUIL_BALL_CLOSE = 74
SEUIL_BALL_TOO_CLOSE = 10

DCERCLE_RAYON = 5

class SousStrat(BaseStrategy):
    def __init__(self,sous_strat):
        BaseStrategy.__init__(self,sous_strat.__name__)
        self.strat=sous_strat 
    def compute_strategy(self,state,idteam,idplayer):
        return self.strat(MyState(state,idteam,idplayer))   
    

def fonceur(me): #"me->objet state" #faire me bouger et shooter vers but de l'opposant
	return me.aller(me.ball_position)+me.shoot(me.but_position_adv)

def fonceur_bis(me):
	return me.aller_vers_ball + me.shoot_avec_angle_puissance(3.14,1)

def revenir_au_but(me): #faire me revenir a la position milieu but 

		if(me.key[0]==1):
   			return me.aller(me.but_position)
		if(me.key[0]==2):
			return me.aller(me.but_position)	

		return SoccerAction()

def alligne_sur_demi_cercle(me): #faire alligner sur demi_cercle et balle
	
	#ERROR: Type Error: Unsupported operand type(s) * for float and instancemethod
		
	ux=(math.cos(me.angle_ball_but))*(DCERCLE_RAYON)
	uy=(math.sin(me.angle_ball_but))*(DCERCLE_RAYON)
	
	pos_x=me.but_position.x+ux
	pos_y=me.but_position.y+uy
	return me.aller(Vector2D(pos_x,pos_y))

	
def pos_sur_demi_cercle(me):

	
	if (me.dist(me.but_position,me.ball_position)<SEUIL_BALL_CLOSE):
	 	if (me.dist(me.but_position,me.ball_position)<SEUIL_BALL_TOO_CLOSE):
			return revenir_au_but(me)
		else:
			return alligne_sur_demi_cercle(me)
	else:
		return SoccerAction()


	
	

FonceurStrat = SousStrat(fonceur)
GkStrat = SousStrat(revenir_au_but)
AllignerStrat = SousStrat(pos_sur_demi_cercle)



class RandomStrategy(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        
        if id_team==1:
            position_milieu_but=Vector2D(x=150.,y=45.)
            
        if id_team==2:
            position_milieu_but=Vector2D(x=0.,y=45.)
            
        vector_acc=state.ball.position-state.player_state(id_team,id_player).position
        
        if (state.ball.position.distance(state.player_state(id_team,id_player).position)<BALL_RADIUS+PLAYER_RADIUS):
            vector_shoot=position_milieu_but-state.ball.position
        else:
            vector_shoot=Vector2D()
        
        return SoccerAction(vector_acc,vector_shoot)
    

"""FonceurStrat =  SousStrat(fonceur ) ---> FonceurStrat.strat == fonceur,
 FonceurStrat.compute_strategy(state,idtema,idplayer) <--> fonceur(MyState(state,id_team,idplayer))

class Strat(BaseStrategy):
	def __init__(self,decideur):
		BaseStrategy.__init__(self,decideur.__name__)
		self.decideur = decideur
	def compute_strategy():
		return self.decideur(MyState(state,id_team,idplayer)


Fonceur = Strat(defenseur)

def defenseur(me):
		return SoccerAction().....

def startComplexce(me):
	if me...:
		return goal(me)
	if me....:
		return defenseur(me)+degager(me)

FonceurStrat = SousStrat(fonceur)

MaStratComplexe = """
