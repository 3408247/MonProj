import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from Strategies import *

from Outils import *


# SPECIALISATION DES JOUEURS POUR LES TOURNOIS #	

# 1vs1#

def j_1vs1(me):

	
	if (me.ball_pos.x<GAME_WIDTH/2): #SI DANS MA MOITIER DE TERRAIN
	
		if me.a_la_balle==3:  # SI ADV A LA BALLE
			print "adversaire a la balle"

			return me.degager_centre
		else:
			print"personne ou moi qui ai la balle"
			return shooteur_malin(me)  

	else: # DANS MOITIER ADV
		if me.a_la_balle==3:	
			return me.piquer_balle
		else:
			return shooteur_malin(me)


#2vs2#

def j_2vs2(me):

	return j_1vs1(me)

	"""flag = me.key[0]==1 
	print me.state.step,me.key[1]

	if(me.ball_pos.x<GAME_WIDTH/2): # DANS MA MOITIER
	
		if me.a_la_balle==3:  # SI ADV A LA BALLE
			return me.degager

		if me.a_la_balle==1: #JAI LA BALLE


			if dist(me.my_pos,me.pos_adv_plus_proche)<BALL_RADIUS+PLAYER_RADIUS+6:  #ADV FONCE SUR MOI
				return me.shoot_vers(pos_equi_plus_proche) # FAIRE PASSE
			else:
				return shooteur_malin(me) # CONTINUER NORMAL 

		else: #PERSONNE N'A LA BALLE 

			return shooteur_malin(me)

	else:  # DANS SA MOITIER 
		print "later",me.my_pos,me.pos_adv_plus_proche
		if dist(me.my_pos,me.pos_adv_plus_proche)<11: #ADV FONCE SUR MOI
			return me.shoot_vers_equi_proche # FAIRE PASSE
		else:
			print "ici",shooteur_malin(me)
			return shooteur_malin(me) # CONTINUER NORMAL """

def g_2vs2(me):	
	
	if dist(me.ball_pos,me.but_pos)<DCERCLE_RAYON+5:
		print"BALL DANS DCERCLERAY+2"
	#ADV encore loin
		print "pos mon but euh"
		print me.but_pos_adv
		print "pos adv proche but"
		print me.pos_adv_pr_but
		print "adv encore loin? distance:"
		print dist(me.but_pos_adv,me.pos_adv_pr_but)
		if dist(me.but_pos_adv,me.pos_adv_pr_but)>2*DCERCLE_RAYON: 
			print"adv encore loin"

	 		if me.a_la_balle==0: #Personne n'a la balle
					print " personne n'a la balle"
					if (me.qui_entre(me.ball_pos,me.pos_equi_plus_proche)==False):
						print "  il n'y a personne entre moi et equi"
						print"   je peux shooter, je shoote vers equi"
						return me.shoot_vers(me.pos_equi_plus_proche)
			
					else:
						print "  il y a qq entre moi et equi"
						print "  je vais degager la balle"
						return me.degager
			else:
				if me.test_peut_shooter:
					print" je peux shooter je deg"
					return me.degager
				else:				
					print " Adv ou mon equipe a la balle, demi cercle"
					return me.alligne_sur_demi_cercle

		#ADV proche...danger
		else: 
			print"adv proche, protect cage"
			return protect_cage(me)
	else:
		print"BALL HYPER LOIn"
		if dist(me.ball_pos,me.my_pos)<10:
			if dist(me.but_pos_adv,me.pos_adv_pr_but)<20: 
				print "mais adv proche de mes buts"
				if dist(me.ball_pos,me.my_pos)<dist(me.ball_pos,me.pos_adv_pr_ball):
					print"toutefois je suis plus proche de balle"
					if (me.qui_entre(me.ball_pos,me.pos_equi_plus_proche)==False):
						return me.shoot_vers(me.pos_equi_plus_proche)
					else:
						return me.degager
				else:
					print"c'est adv plus proche de la balle, protect cage"
					return protect_cage(me)
			else:	
				print "adv loin de mes buts"
				if (me.qui_entre(me.ball_pos,me.pos_equi_plus_proche)==False):
					return me.shoot_vers(me.pos_equi_plus_proche)
				else:
					return me.degager
		else:
			return me.alligne_sur_demi_cercle
		
					
	

J_1vs1_Strat = SousStrat(j_1vs1)
#Test_Strat = SousStrat(test)

J_2vs2_Strat = SousStrat(j_2vs2)
J_2vs2_Strat_bis= SousStrat(j_2vs2)
Hello = SousStrat(j_2vs2)
Hey = SousStrat(j_2vs2)

G_2vs2= SousStrat(g_2vs2)




