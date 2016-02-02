# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:38:24 2016

@author: 3408247
"""

import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from random import uniform


class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.key = (idteam,idplayer)

##############################################################################################################
## POSITIONS #################################################################################################
##############################################################################################################
    @property
    def my_position(self): #retourne Vector2D->la position de self (ici joueur)
        return self.state.player_state(self.key[0],self.key[1]).position
        #equivalent a self.state.player_state(self.key[0],self.key[1])
    
    @property    
    def ball_position(self): #retoune Vector2D->la position de self (ici ball)
        return self.state.ball.position

    @property
    def but_position(self): #retourne Vector2D->la position_milieu du but 
	if (self.key[0]==1):	
		return Vector2D(x=0,y=GAME_HEIGHT/2)

	if (self.key[0]==2):
		return Vector2D(x=GAME_WIDTH,y=GAME_HEIGHT/2)

    @property   
    def but_position_adv(self): #retourne Vector2D->la position_milieu du but de l'adversaire
	if (self.key[0]==2):	
		return Vector2D(x=0,y=GAME_HEIGHT/2)

	if (self.key[0]==1):
		return Vector2D(x=GAME_WIDTH,y=GAME_HEIGHT/2)

##############################################################################################################
## DISTANCES #################################################################################################
##############################################################################################################

    def dist(self,u,v): #"u->Vector2D, v->Vector2D" #retourne float->la distance entre u et v
	return u.distance(v)

    def dist_player_ball(self,player,ball): #distance entre player et ball
	return dist(self.my_position,ball_position)

    @property
    def dist_but_ball(self): #distance entre but et ball
	return dist(self.but_position,ball_position)

    @property
    def dist_but_adv_ball(self): #distance entre but_adv et ball
	return dist(self.but_position_adv,ball_position)
        
##############################################################################################################
## MOUVEMENTS ################################################################################################
##############################################################################################################

    def aller(self,p): #"self->vector2D, p->vector2D" #retourne SoccerAction->faire bouger self jusqu'a p ; pas de shoot
        return SoccerAction(p-self.my_position,Vector2D())

    @property
    def test_peut_shooter(self):
	return (dist(self.my_position,self.ball_position)<BALL_RADIUS+PLAYER_RADIUS)
		
##############################################################################################################
## SHOOTS ####################################################################################################
##############################################################################################################
	
        
    def shoot(self,p): #pas de mouvement; faire shooter dans la direction p - self
        return SoccerAction(Vector2D(),p-self.my_position)

    def shoot_alea(self):
	angleu=uniform(0.,shootRandomAngle)
	normeu=uniform(1.,maxBallAcceleration)
        return SoccerAction(Vector2D(angle=angleu,norm=normeu))
