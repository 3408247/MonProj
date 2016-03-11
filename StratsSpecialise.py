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

			return me.degager
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

	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_CLOSE):
		
	 	if (dist(me.but_pos,me.ball_pos)<SEUIL_BALL_TOO_CLOSE):
			if me.a_la_balle==3:
				return me.degager
			if me.a_la_balle==2:
				return me.alligne_sur_demi_cercle

			else:
				if me.test_peut_shooter:
					if (qui_entre(me.ball_pos,me.pos_equipier_plus_proche)==False) and (dist(me.ball_pos,me.pos_equi_proche)<GAME_WIDTH/4):
						return shoot_vers(me.pos_equi_plus_proche)
					else:
						return me.degager
				else:
					return me.courir_vers_ball			

		return me.alligne_sur_demi_cercle

	return me.courir_vers_(me.but_pos)
			
	

J_1vs1_Strat = SousStrat(j_1vs1)
#Test_Strat = SousStrat(test)

J_2vs2_Strat = SousStrat(j_2vs2)
J_2vs2_Strat_bis= SousStrat(j_2vs2)
Hello = SousStrat(j_2vs2)
Hey = SousStrat(j_2vs2)

G_2vs2= SousStrat(g_2vs2)




