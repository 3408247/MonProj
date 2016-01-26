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
SEUIL_BALL_FAR = 30
SEUIL_BALL_CLOSE = 20
SEUIL_BALL_TOO_CLOSE = 10

DCERCLE_RAYON = 7

class SousStrat(BaseStrategy):
    def __init__(self,sous_strat):
        BaseStrategy.__init__(self,sous_strat.__name__)
        self.strat=sous_strat 
    def compute_strategy(self,state,idteam,idplayer):
        return self.strat(MyState(state,idteam,idplayer))   
    

def fonceur(me): #"me->objet state" #faire me bouger et shooter vers but de l'opposant
	return me.aller(me.ball_position())+me.shoot(me.but_position_adv())

"""LE GOALKEEPER"""
def revenir_au_but(me): #faire me revenir a la position milieu but 

		if(me.key[0]==1):
   			return me.aller(me.but_position()+Vector2D(x=3.,y=0))
		if(me.key[0]==2):
			return me.aller(me.but_position()-Vector2D(x=3.,y=0))	

		return SoccerAction()

def alligne_sur_demi_cercle(me):
	
	if(me.key[0]==1):
		position=(me.but_position()+Vector2D(x=3.,y=0))
	if(me.key[0]==2):
		position=(me.but_position()-Vector2D(x=3.,y=0))

	if (pente(me.ball_position(),position)!=0):
		nouvelle_position=intersection_demicercle_et_ligne(position.x,position.y,DCERCLE_RAYON,pente)
		return me.aller(nouvelle_position)
	else:
		return SoccerAction()
	
		
#def goalkeeper(me):

	 #Faire me s'alligner avec la balle quand elle est loin
	#if me.dist(me.my_position(),me.ball_position())>SEUIL_BALL_FAR: 
		#return goalkeeper_revenir_au_but(me)"""

	
	#"""if (me.dist(me.my_position(),me.ball_position())>SEUIL_BALL_TOO_CLOSE)and(me.dist(me.my_position(),me.ball_position())<SEUIL_BALL_CLOSE):""" 
			

FonceurStrat = SousStrat(fonceur)
GkStrat = SousStrat(revenir_au_but)
AllignerStrat = SousStrat(alligne_sur_demi_cercle)


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
