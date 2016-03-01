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
	   return me.shoot(me.but_pos_adv)
	else:
	   return me.aller(me.ball_pos)

def fonceur_bis(me):
    if me.test_peut_shooter:
	return me.shoot_avec_angle_puissance(me.angle_player_but,10.)

    else:
	return me.courir_vers(me.ball_pos)


def fonceur_pass(me):
	#print(me.aller(me.ball_position))
	#print(me.shoot_vers_equipier_proche())

        if me.test_peut_shooter:
 	   return me.shoot_vers_equipier_proche

	else:
	   return me.aller(me.ball_pos)


#Attaquant 1_VS_1 ou 2_VS_2
def shooteur_malin(me):
    if me.test_peut_shooter:

	if (me.dist_but_adv_ball>30):  #JE SUIS PRES DES BUTS ADV

		if dist(me.my_pos,me.pos_adv)<25:   # SI ADV EST PROCHE/S'APPROCHE  DE MOI
			return me.shoot_malin  #SHOOT 
		else:
			return me.shoot_dribble  # CONTINUE A S'APPROCHER DES BUTS

	else: # JE SUIS LOIN DES BUTS
	 	return me.shoot_dribble  

    else: # PEUT PAS SHOOTER
	return me.courir_vers_ball 


### DEFENSEUR ###

# 1_VS_1 #

	
    
 

def def_mouvement_et_shoot(me):
	#print me.state._configs[(me.key[0],me.key[1])]._last_shoot

	if (me.ball_pos.x<GAME_WIDTH/2):
	

		if me.test_peut_shooter:
		
			
			return me.shoot_vers_but_adv
		else:
									
			return me.aller_vers_ball 

	else:	
		
		return me.def_positionnement_defaut



#def def_mouvement_et_shoot_centre(me):



### GARDIEN ###

def revenir_au_but(me): #faire me revenir a la position milieu but 

  	return me.aller(me.but_pos)
	
	
def gardien_mouvement(me):

	
	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_CLOSE):
		
	 	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_TOO_CLOSE):
			
			return me.aller_vers_ball
		else:
			
			return me.alligne_sur_demi_cercle

	return revenir_au_but(me)



def gardien_shoot_vers_but(me):
	if me.test_peut_shooter:
		return me.shoot_vers_but_adv

	else:
		return gardien_mouvement(me)
		


def gardien_2(me):

	
	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_CLOSE):
	 	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_TOO_CLOSE):
			return revenir_au_but(me)
		else:
			return me.alligne_sur_demi_cercle
	else:
		if me.test_peut_shooter:
			return me.shoot_intercepter_contrecarE

		else:
			return me.aller_vers_ball + me.shoot_alea


	

FonceurStrat = SousStrat(fonceur_bis)
Gard_shoot_but = SousStrat(gardien_shoot_vers_but)

DefStrat = SousStrat(def_mouvement_et_shoot)

