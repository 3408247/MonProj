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


class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.key = (idteam,idplayer)
      
    def my_position(self): #retourne Vector2D->la position de self (ici joueur)
        return self.state.player_state(self.key[0],self.key[1]).position
        #equivalent a self.state.player_state(self.key[0],self.key[1])
        
    def ball_position(self): #retoune Vector2D->la position de self (ici ball)
        return self.state.ball.position

    def but_position(self): #retourne Vector2D->la position_milieu du but 
	if (self.key[0]==1):	
		return Vector2D(x=0,y=GAME_HEIGHT/2)

	if (self.key[0]==2):
		return Vector2D(x=GAME_WIDTH,y=GAME_HEIGHT/2)
        
    def but_position_adv(self): #retourne Vector2D->la position_milieu du but de l'adversaire
	if (self.key[0]==2):	
		return Vector2D(x=0,y=GAME_HEIGHT/2)

	if (self.key[0]==1):
		return Vector2D(x=GAME_WIDTH,y=GAME_HEIGHT/2)

    def dist(self,u,v): #"u->Vector2D, v->Vector2D" #retourne float->la distance entre u et v
	return u.distance(v)
        

    def aller(self,p): #"self->vector2D, p->vector2D" #retourne SoccerAction->faire bouger self jusqu'a p ; pas de shoot
        return SoccerAction(p-self.my_position(),Vector2D())

        
    def shoot(self,p): #pas de mouvement; faire shooter dans la direction p - self
        return SoccerAction(Vector2D(),p-self.my_position())
        
            
"""
state= .....
monstate =MyState(state, 1,0)
monstate.aller(point)"""
