





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

RAYON = 20


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

###################################################################################################
### FONCEUR #######################################################################################
###################################################################################################
    
def fonceur(me):
	#print "entre effectivement dans fonceur strat"
	if me.test_peut_shooter:
		print "FONCEUR EN EFFET CHOISI"
		return me.shoot_vers(me.but_pos_adv)
	else:
		print "FONCEUR EN EFFET CHOISI"
		return me.courir_vers_ball

Fonceur_Strat = SousStrat(fonceur)


###################################################################################################
### SE DEMARQUER: BIEN SE POSITIONNER POUR RECEVOIR UNE PASSE TOUT EN ETANT PROCHE DES BUTS ADV ###
###################################################################################################

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
	d_min=999
	found=False
	for good_point in liste_points:
		d=dist(good_point,me.pos_adv_pr_moi)
		if d>d_max:
			d_max=d
			chosen_point=good_point

			dd=dist(good_point,me.but_pos_adv)
			if dd<d_min:
				d_min=dd
				better_point=good_point       # better_point sera le point qui est le plus proche des buts adv
				found=True
	if (found):
		if dist(chosen_point,me.but_pos_adv)<dist(better_point,me.but_pos_adv):
			return me.courir_vers(chosen_point)
		else:
			return me.courir_vers(better_point)	

	return me.courir_vers(chosen_point)

Demarquer_Strat = SousStrat(demarquer)


###################################################################################################
### DEMARQUER EN DEFENSE : COMME DEMARQUER MAIS TOUT EN ETAT PROCHE DE MES BUTS ###################
###################################################################################################

def demarquer_def(me):
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
	d_min=999
	found=False
	for good_point in liste_points:
		d=dist(good_point,me.pos_adv_pr_moi)
		if d>d_max:
			d_max=d
			chosen_point=good_point

			dd=dist(good_point,me.but_pos)
			if dd<d_min:
				d_min=dd
				better_point=good_point       # better_point sera le point qui est le plus proche des buts adv
				found=True
	if (found):
		if dist(chosen_point,me.but_pos)<dist(better_point,me.but_pos):
			return me.courir_vers(chosen_point)
		else:
			return me.courir_vers(better_point)	

	return me.courir_vers(chosen_point)

Demarquerdef_Strat= SousStrat(demarquer_def)	

###################################################################################################
### FAIRE UNE PASSE ###############################################################################
###################################################################################################

def passe(me):
	res=SoccerAction(Vector2D(),Vector2D())
	res.name="passe"
	if me.test_peut_shooter:
		res=me.shoot_vers_norm(me.pos_equi_pr_ball,3.0)
		return res
	else:
		res=me.courir_vers_ball2
		return res

###################################################################################################
### PROTEGER CAGE #################################################################################
###################################################################################################

def protect_cage(me):
	res=SoccerAction(Vector2D(),Vector2D())
	#res.name="protect cage"
	if me.test_peut_shooter:
		
		return me.degager
	else:
		if me.ball_pos.y>me.but_pos.y+GAME_GOAL_HEIGHT/2:
			res=me.courir_vers(Vector2D(x=0.5,y=me.but_pos.y+GAME_GOAL_HEIGHT/2))
			return res
		if me.ball_pos.y<me.but_pos.y-GAME_GOAL_HEIGHT/2:
			res=me.courir_vers(Vector2D(x=0.5,y=me.but_pos.y-GAME_GOAL_HEIGHT/2))
			return res
		else:
			res=me.courir_vers(Vector2D(x=0.5,y=me.ball_pos.y))
			return res


###################################################################################################
### ALLIGNER SUR DEMI CERCLE ######################################################################
###################################################################################################

def alligne_demi_cercle(me):
	vecteur=me.ball_pos-(me.but_pos)
	angle_ball_but=vecteur.angle

	ux=(math.cos(angle_ball_but))*(DCERCLE_RAYON)
	uy=(math.sin(angle_ball_but))*(DCERCLE_RAYON)
	
	pos_x=me.but_pos.x+ux
	pos_y=me.but_pos.y+uy
	
	res=me.courir_vers(Vector2D(pos_x,pos_y))
	res.name="alligne sur demi"

	return res



###################################################################################################
### GARDIEN COMPLET ###############################################################################
###################################################################################################
		


def gardien(me):	
	
	#print "GAAAARDIEN EN FEET CHOISIE"
	if dist(me.ball_pos,me.but_pos)<DCERCLE_RAYON+5:
		#print "La balle est proche de mes buts"
	
		if dist(me.but_pos,me.pos_adv_pr_but)>5*DCERCLE_RAYON:
		#	print "L'adversaire le plus proche est encore loin "

	 		if me.a_la_balle==0: 
		#		print" Personne n'a la balle"

				if ((me.equi_pr_posobj(me.ball_pos)!=None)and(me.obs_entre(me.ball_pos,me.pos_equi_pr_ball)==False)):
		#			print "Personne entre moi et equipier plus proche"

		#			print " Je shoote vers equipier"
					return me.shoot_vers(me.pos_equi_pr_ball)
								
				else:
		#			print"Il y a quelqu'un entre moi et equipier plus proche"

		#			print" Je degage le ballon"
					return me.degager
			else:
				if me.test_peut_shooter:
		#			print "je degage"
					return me.degager
				else:				
		#			print "jalligne"
					return alligne_demi_cercle(me)

		else: 
		#	print" L'adversaire le plus proche est pres des buts"

		#	print"Je protege mes buts"
			return protect_cage(me)


	else:
		#print" La balle est encore tres loin"

		if dist(me.ball_pos,me.my_pos)<10:
			#print" La balle est assez proche"
			
			if dist(me.but_pos_adv,me.pos_adv_pr_but)<20: 
			#	print"L'adversaire le plus proche est pres des buts"

				if dist(me.ball_pos,me.my_pos)<dist(me.ball_pos,me.pos_adv_pr_ball):
			#		print "Toutefois je suis plus proche de la balle que lui"
								
					if ((me.equi_pr_posobj(me.ball_pos)!=None)and(me.obs_entre(me.ball_pos,me.pos_equi_pr_ball)==False)):
			#			print" Personne entre moi et equipier plus proche"
						
			#			print" Je shoote vers equipier"
						return me.shoot_vers(me.pos_equi_pr_ball)

					else:
			#			print"Il y a quelqu'un entre moi et equipier plus proche"

			#			print" Je degage le ballon"
						return me.degager
				else:	
			#		print" Et c'est l'adversaire qui est plus proche de la balle"
			#		
			#		print"Je protege mes cages"
					return protect_cage(me)
			else:
			#	print"L'adversaire le plus proche est encore loin"
			#	print "me.ball_pos, me.pos_equi_pr_ball, Obstacle entre?"
			#	print me.ball_pos
			#	if (me.equi_pr_posobj(me.ball_pos)!=None):
			#		print me.pos_equi_pr_ball
		
			#		print me.obs_entre(me.ball_pos,me.pos_equi_pr_ball)
			#	else:
			#		print "it is none"
		
				if ((me.equi_pr_posobj(me.ball_pos)!=None) and (me.obs_entre(me.ball_pos,me.pos_equi_pr_ball)==False)):
			#		print"Personne entre, shoot vers equi"
					return me.shoot_vers(me.pos_equi_pr_ball)
				else:
			#		print " qq entre, degage"
					return me.degager
		else:
			#print"alligne sur demi cercle"
			return alligne_demi_cercle(me)
		

Gardien_Strat= SousStrat(gardien)




###################################################################################################
###################################################################################################


def euh(me):
	print "idt, idp: ", me.key[0],me.key[1]
	
	if me.ball_pos.x>=GAME_WIDTH/2:
		return fonceur(me)
	else:
		return gardien(me)

Euh_Strat = SousStrat(eval('euh'))




