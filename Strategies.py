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
SEUIL_BALL_CLOSE = GAME_WIDTH/2
SEUIL_BALL_TOO_CLOSE = 5

DCERCLE_RAYON = 7

class SousStrat(BaseStrategy):
    def __init__(self,sous_strat):
        BaseStrategy.__init__(self,sous_strat.__name__)
        self.strat=sous_strat 
    def compute_strategy(self,state,idteam,idplayer):
        return self.strat(MyState(state,idteam,idplayer))   
    

def fonceur(me): #"me->objet state" #faire me bouger et shooter vers but de l'opposant
	return me.aller(me.ball_position())+me.shoot(me.but_position_adv())

def revenir_au_but(me): #faire me revenir a la position milieu but 

		if(me.key[0]==1):
   			return me.aller(me.but_position()+Vector2D(x=3.,y=0))
		if(me.key[0]==2):
			return me.aller(me.but_position()-Vector2D(x=3.,y=0))	

		return SoccerAction()

def alligne_sur_demi_cercle(me): #faire alligner sur demi_cercle et balle

	vect_bouger=Vector2D( angle=(me.ball_position()-me.my_position()).angle,norm=DCERCLE_RAYON)
	return me.aller(vect_bouger)

	
def pos_sur_demi_cercle(me):

	
	if (me.dist(me.my_position(),me.ball_position())<SEUIL_BALL_CLOSE):
	 	if (me.dist(me.my_position(),me.ball_position())<SEUIL_BALL_TOO_CLOSE):
	 		return revenir_au_but(me)

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

class FonceurStrat(BaseStrategy):
	def __init__(self):
		BaseStrategy.__init__(self,"fonceur")
	def compute_strategy():
		return fonceur(MyState(state,id_team,idplayer)


def defenseur(me):
		.....

def startComplexce(me):
	if me...:
		return goal(me)
	if me....:
		return defenseur(me)+degager(me)

FonceurStrat = SousStrat(fonceur)

MaStratComplexe = """
