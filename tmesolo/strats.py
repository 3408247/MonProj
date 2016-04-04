




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

from outils import *
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
    
### SUIVRE BALL ###
def suivre_ball(me):
    x_=me.ball_pos.x + 6
    y_=me.ball_pos.y
    point=Vector2D(x=x_,y=y_)
    return me.courir_vers(point)

def suivre_balle(me):
	balle= me.state.ball
	#for i in range(0,5):
	#	balle.next(Vector2D())

	y_=balle.position.y
	
	if balle.position.x<=GAME_WIDTH/2:
	 	x_=balle.position.x - 6
   			
	else:
		x_=balle.position.x - 6
   	
    	
	point=Vector2D(x=x_,y=y_)
	return me.courir_vers(point)


### FAIRE UNE PASSE ###
def passe(me):
	if me.test_peut_shooter:
		return me.shoot_vers(me.pos_adv_plus_proche)
	else:
		return me.courir_vers_ball




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


FonceurStrat = SousStrat(fonceur)


### JOUEUR QUI GARDE LA BALLE et FAIT DES PASSES ###

def jpasse(me):

	if me.a_la_balle==1:       # MOI J'AI LA BALLE

		if (dist(me.ball_pos, me.pos_adv_pr_ball)<5):  # SI ADVERSAIRE EST PROCHE DE LA BALLE
			
			if (me.qui_entre(me.ball_pos,me.pos_equi_plus_proche)==False):  # Si je ne peux pas faire de passe, car il y a qq entre la balle et mon equipier le plus proche

				if me.test_peut_tirer:

					return me.shoot_dribble_vers(me.pos_equi_plus_proche)  # J'essaye de dribbler vers mon equipier le plus proche, ce dribble fera en sorte que j'evite le joueur adversaire: voir shoot_dribble_vers dans outils

				else:
	
					return me.courir_vers_ball

			else:    # Il n'y a personne entre, donc faire la passe

				return passe(me)

		else:   # Adversaire n'est pas proche, je suis safe
			
			return SoccerAction(Vector2D(),Vector2D()) # Fait rien

	
	if me.a_la_balle==2:      # Mon equipe a la balle

		return suivre_balle(me)

	if me.a_la_balle==0:   # Si personne n'a la balle

		if (dist(me.my_pos,me.ball_pos))< (dist(me.pos_equi_plus_proche,me.ball_pos)):  # Si je suis plus proche de la balle que mon equipier
			return me.courir_vers_ball
		else:
			return suivre_balle(me)

	else:  # Si adversaire a la balle


		if (dist(me.my_pos,me.ball_pos))< (dist(me.pos_equi_plus_proche,me.ball_pos)):  # Si je suis plus proche de la balle que mon equipier


			if me.test_peut_tirer:    # Contrainte sur joueur eq 1
				return me.piquer_balle

			else:

				return me.courir_vers_ball
		else:
			return suivre_balle(me)


		
				
PasseStrat = SousStrat(jpasse)


### JOUEUR QUI ESSAYE DE CHOOPER LA BALLE ###


	




