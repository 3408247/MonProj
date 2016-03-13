





# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:45:44 2016

@author: 3408247
"""
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


class SousStrat(BaseStrategy):
    def __init__(self,sous_strat):
        BaseStrategy.__init__(self,sous_strat.__name__)
        self.strat=sous_strat 

    def compute_strategy(self,state,idteam,idplayer): #ou faire miroir ici
	self.state = state
     
        action=self.strat(MyState(self.state,idteam,idplayer))
	#print action
        if(idteam!=1):
	   action= miroir_action(action)

        #print action
        return action
    



### ATTAQUANT ###


def fonceur(me): #"me->objet state" #faire me bouger et shooter vers but de l'opposant
	#print("Fonceur", me.shoot_vers_but_adv, me.state._configs[(me.key[0],me.key[1])]._last_shoot)
	if me.test_peut_shooter:
	   return me.shoot_vers(me.but_pos_adv)
	else:
	   return me.courir_vers_ball

def fonceur_pass(me):
	#print(me.aller(me.ball_position))
	#print(me.shoot_vers_equipier_proche())

        if me.test_peut_shooter:
 	   return me.shoot_vers_equi_proche

	else:
	   return me.aller(me.ball_pos)


#Attaquant 1_VS_1 ou 2_VS_2
def shooteur_malin(me):

    if me.test_peut_shooter:

	if (dist(me.ball_pos,me.but_pos_adv)<GAME_WIDTH/4):  #JE SUIS TRES PRES DES BUTS ADV

		if dist(me.ball_pos,me.pos_adv_plus_proche)<12:   # SI ADV EST PROCHE/S'APPROCHE  DE MOI
		
			if qq_entre(me.ball_pos,me.but_pos_adv,me.pos_adv_plus_proche):
								
				return me.shoot_dribble_vers(me.but_pos_adv)
 
			else: 
				return me.shoot_malin  #SHOOT 
		else:
			print "continier a approcher dribbler"
			return me.shoot_dribble_vers(me.but_pos_adv)  # CONTINUE A S'APPROCHER DES BUTS

	else: 
		if (dist(me.ball_pos,me.but_pos_adv)<GAME_WIDTH/2): # JE SUIS ASSEZ PROCHE DES BUTS
	 
			if qq_entre(me.ball_pos,me.but_pos_adv,me.pos_adv_plus_proche):
				print "il y a qq donc continue a dribbler"
	
	 			return me.shoot_dribble_vers(me.but_pos_adv)  
			else:
				print "il n y a personne donc shoot malin"

				return me.shoot_malin

		else:  # PAS ASSEZ PROCHE
			print "pas assez proche donc continue a dribbler"
			return me.shoot_dribble_vers(me.but_pos_adv)

    else: # PEUT PAS SHOOTER
	#print "peut pas shooter"
	
	return me.courir_vers_ball2 


### DEFENSEUR ###

# 1_VS_1 #

def def_pos_defaut(me):
	return me.placerEntre_A_B_x(me.ball_pos,me.but_pos,GAME_WIDTH/4)
	

def def_mouvement_et_shoot(me):
	#print me.state._configs[(me.key[0],me.key[1])]._last_shoot

	if (me.ball_pos.x<GAME_WIDTH/2):
	

		if me.test_peut_shooter:
		
			
			return me.shoot_degager
		else:
									
			return me.courir_vers_ball

	else:	
		
		return def_pos_defaut(me)



### GARDIEN ###

def protect_cage(me):
	if me.test_peut_shooter:
		return me.degager
	else:
		if me.ball_pos.y>me.but_pos.y+GAME_GOAL_HEIGHT/2:
			return me.courir_vers(Vector2D(x=0.5,y=me.but_pos.y+GAME_GOAL_HEIGHT/2))
		if me.ball_pos.y<me.but_pos.y-GAME_GOAL_HEIGHT/2:
			return me.courir_vers(Vector2D(x=0.5,y=me.but_pos.y-GAME_GOAL_HEIGHT/2))
		else:
			return me.courir_vers(Vector2D(x=0.5,y=me.ball_pos.y))
	
	
def gardien_mouvement(me):

	
	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_CLOSE):
		
	 	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_TOO_CLOSE):
			
			return me.courir_vers_ball
		else:
			
			return me.alligne_sur_demi_cercle

	return me.courir_vers(me.but_pos)



def gardien_shoot_vers_centre(me):
	if me.test_peut_shooter:
		return me.degager

	else:
		return gardien_mouvement(me)
		

	

FonceurStrat = SousStrat(fonceur)
Gard_shoot_but = SousStrat(gardien_shoot_vers_centre)

DefStrat = SousStrat(def_mouvement_et_shoot)

