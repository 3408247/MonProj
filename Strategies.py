





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
	   return me.courir_vers(me.ball_pos)

def fonceur_pass(me):
	#print(me.aller(me.ball_position))
	#print(me.shoot_vers_equipier_proche())

        if me.test_peut_shooter:
 	   return me.shoot_vers_equi_proche

	else:
	   return me.aller(me.ball_pos)


#Attaquant 1_VS_1 ou 2_VS_2
def shooteur_malin(me):

    print "distance ball et adv est"
    print dist(me.ball_pos,me.pos_adv)
    if me.test_peut_shooter:

	if (me.dist_but_adv_ball<GAME_WIDTH/4):  #JE SUIS PRES DES BUTS ADV
		print "Pres des buts"

		if dist(me.ball_pos,me.pos_adv_plus_proche)<12:   # SI ADV EST PROCHE/S'APPROCHE  DE MOI
			print "adv s'approche"
			print dist(me.my_pos,me.pos_adv_plus_proche)

			return me.shoot_malin  #SHOOT 
		else:
			print "adversaire encore loin "
			return me.shoot_dribble  # CONTINUE A S'APPROCHER DES BUTS

	else: # JE SUIS LOIN DES BUTS
		print "loin des buts"
	 	return me.shoot_dribble  

    else: # PEUT PAS SHOOTER
	print "peut pas shooter"
	return me.courir_vers(me.ball_pos) 


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
									
			return me.courir_vers(me.ball_pos)

	else:	
		
		return def_pos_defaut(me)



### GARDIEN ###

def revenir_au_but(me): #faire me revenir a la position milieu but 

  	return me.courir_vers(me.but_pos)
	
	
def gardien_mouvement(me):

	
	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_CLOSE):
		
	 	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_TOO_CLOSE):
			
			return me.courir_vers(me.ball_pos)
		else:
			
			return me.alligne_sur_demi_cercle

	return revenir_au_but(me)



def gardien_shoot_vers_but(me):
	if me.test_peut_shooter:
		return me.shoot_vers_but_adv

	else:
		return gardien_mouvement(me)
		

	

FonceurStrat = SousStrat(fonceur)
Gard_shoot_but = SousStrat(gardien_shoot_vers_but)

DefStrat = SousStrat(def_mouvement_et_shoot)

