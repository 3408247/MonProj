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
		return Vector2D(x=3,y=GAME_HEIGHT/2)

	if (self.key[0]==2):
		return Vector2D(x=GAME_WIDTH-3,y=GAME_HEIGHT/2)

    @property   
    def but_position_adv(self): #retourne Vector2D->la position_milieu du but de l'adversaire
	if (self.key[0]==2):	
		return Vector2D(x=3,y=GAME_HEIGHT/2)

	if (self.key[0]==1):
		return Vector2D(x=GAME_WIDTH-3,y=GAME_HEIGHT/2)

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
    def aller_vers_but_adv(self):
	return self.aller(self.but_position_adv)

    @property
    def aller_vers_ball(self):
        return self.aller(self.ball_position)
            
    def aller_avec_angle_norme(self,theta,norme):
	dep=Vector2D(angle=theta,norm=norme)
	return SoccerAction(dep,Vector2D())
   		
##############################################################################################################
## SHOOTS ####################################################################################################
##############################################################################################################
    @property
    def test_peut_shooter_dist(self):
	return (dist(self.my_position,self.ball_position)<BALL_RADIUS+PLAYER_RADIUS)

    #def test_peut_shooter_tours(self):
        
    def shoot(self,p): #pas de mouvement; faire shooter dans la direction p - self
        return SoccerAction(Vector2D(),p-self.my_position)
    
    @property
    def shoot_alea(self):
	angleu=uniform(0.,shootRandomAngle)
	normeu=uniform(1.,maxBallAcceleration)
        return SoccerAction(Vector2D(),Vector2D(angle=angleu,norm=normeu))

    #comment shooter tres fort aleatoirement ? Decorateur thingy ? Specialisation ?
  
    @property
    def shoot_vers_but_adv(self):
         return self.shoot(self.but_position_adv)

    def shoot_avec_angle_puissance(self,theta,puissance):
	shot=Vector2D(angle=theta,norm=puissance)
	return SoccerAction(Vector2D(),shot)

   
 
##############################################################################################################
## MIROIRS ###################################################################################################
##############################################################################################################

  
    def miroir_pos(u):
	x_mod=GAME_WIDTH-u.my_position.x
	return SoccerAction(Vector2D(x_mod,u.my_position.y),Vector2D())

  
    def miroir_vect(u):
  	x_mod=-u.my_position.x
       	return SoccerAction(Vector2D(x_mod,u.my_position.y),Vector2D())
		
##############################################################################################################
## ANGLES ###################################################################################################
##############################################################################################################


    def angle_ball_but(self):

	if (self.key[0]==1):

		vecteur_ball_but_position_bis=self.ball_position-self.but_position

	else:
		vecteur_ball_but_position_bis=self.ball_position-miroir_pos(self.but_position)

	return vecteur_point_but_position_bis.angle


    def angle_player_but(self):
	
	if (self.key[0]==1):
		vecteur_player_but_position_bis=self.my_position-self.but_position

	else:
		vecteur_player_but_position_bis=self.my_position-miroir_pos(self.but_position)

	return vecteur_point_but_position_bis.angle



