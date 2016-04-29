





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

RAYON = 15


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
    
### SUIVRE BALL ###

def suivre_balle(me):
	balle= me.state.ball
	for i in range(0,5):
		balle.next(Vector2D())

	y_=balle.position.y
	
	if balle.position.x<=GAME_WIDTH/2:
	 	x_=balle.position.x - 6
   			
	else:
		x_=balle.position.x - 6
   	
    	
	point=Vector2D(x=x_,y=y_)
	return me.courir_vers(point)


### SE DEMARQUER: BIEN SE POSITIONNER POUR RECEVOIR UNE PASSE ###
def demarquer(me):
	v_ball_but= me.but_pos_adv-me.ball_pos
	angle_ball_but = v_ball_but.angle
	
	# (pos_x, pos_y) : position entre ball et but se trouvant a une distance de RAYON de la balle
	pos_x= (math.cos(angle_ball_but)*RAYON) + me.ball_pos.x
	pos_y= (math.sin(angle_ball_but)*RAYON) + me.ball_pos.y

	chosen_point=Vector2D(pos_x,pos_y)

	# Chercher un/des points autour de (pos_x, pos_y) tel que il n'y ait pas d'adv entre ball et ce point
	liste_points=[]  # Liste de Vector2D

	for deltax in range (-7,7):
		for deltay in range (-7,7):
			point=Vector2D(x=pos_x+deltax,y=pos_y+deltay)
			if me.obs_entre(point,me.ball_pos)==False:
				good_point=point
				liste_points.append(good_point)

	# Parmi ces points trouves, chercher celui qui est le plus loin de l'adv le plus proche de moi	
	d_max=0
	for good_point in liste_points:
		d=dist(good_point,me.pos_adv_pr_moi)
		if d>d_max:
			d_max=d
			chosen_point=good_point
	
	return me.courir_vers(chosen_point)

Demarquer_Strat = SousStrat(demarquer)


### FAIRE UNE PASSE ###
def passe(me):
	if me.test_peut_shooter:
		return me.shoot_vers(me.pos_eq_pr_ball)
	else:
		return me.courir_vers_ball2

#def chercher(me):
	




### ATTAQUANT ###


def fonceur(me):
	if me.test_peut_shooter:
		return me.shoot_vers(me.but_pos_adv)
	else:
		return me.courir_vers_ball

"""
#"me->objet state" faire me bouger et shooter vers but de l'opposant  print("Fonceur", me.shoot_vers_but_adv, me.state._configs[(me.key[0],me.key[1])]._last_shoot)

def fonceur(me): 

	if me.test_peut_shooter:
		return me.shoot_vers(me.but_pos_adv)
	else:
	   	return me.courir_vers_ball
"""
def fonceur_pass(me):
	#print(me.aller(me.ball_position))
	#print(me.shoot_vers_equipier_proche())

        if me.test_peut_shooter:
 	   return me.shoot_vers_equi_proche

	else:
	   return me.aller(me.ball_pos)


#Attaquant 1_VS_1 ou 2_VS_2



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

def alligne_demi_cercle(me):
	vecteur=me.ball_pos-(me.but_pos)
	angle_ball_but=vecteur.angle

	ux=(math.cos(angle_ball_but))*(DCERCLE_RAYON)
	uy=(math.sin(angle_ball_but))*(DCERCLE_RAYON)
	
	pos_x=me.but_pos.x+ux
	pos_y=me.but_pos.y+uy

	return me.courir_vers(Vector2D(pos_x,pos_y))


def gardien_mouvement(me):

	
	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_CLOSE):
		
	 	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_TOO_CLOSE):
			
			return me.courir_vers_ball
		else:
			
			return alligne_demi_cercle(me)

	return me.courir_vers(me.but_pos)



def gardien_shoot_vers_centre(me):
	if me.test_peut_shooter:
		return me.degager

	else:
		return gardien_mouvement(me)
		

	

FonceurStrat = SousStrat(fonceur)
Gard_shoot_but = SousStrat(gardien_shoot_vers_centre)

DefStrat = SousStrat(def_mouvement_et_shoot)

