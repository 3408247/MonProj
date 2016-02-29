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
	
	if (me.ball_position.x<GAME_WIDTH/2): #SI DANS MA MOITIER DE TERRAIN

		if me.a_la_balle==2:  # SI ADV A LA BALLE
			if me.test_peut_shooter:
				return me.shoot_degager 
			else:
				return me.courir_vers_ball
		else:
			return shooteur_malin(me)  

	else: # DANS MOITIER ADV
		return shooteur_malin(me)


#2vs2#

def j_2vs2(me):
	flag = me.key[0]==1 
	print me.state.step,me.key[1]

	if(me.ball_position.x<GAME_WIDTH/2): # DANS MA MOITIER
		print "la1"
		if me.a_la_balle==2:  # SI ADV A LA BALLE

			if me.test_peut_shooter:
				return me.shoot_vers_but_adv 

			else:
				print "la", me.courir_vers_ball
				return me.courir_vers_ball

		if me.a_la_balle==1: #JAI LA BALLE

			print "labis"
			if dist(me.my_position,me.pos_adv_plus_proche)<7:  #ADV FONCE SUR MOI
				return me.shoot_vers_equipier_proche # FAIRE PASSE
			else:
				return shooteur_malin(me) # CONTINUER NORMAL 

		else: #PERSONNE N'A LA BALLE 

			return shooteur_malin(me)

	else:  # DANS SA MOITIER 
		print "later",me.my_position,me.pos_adv_plus_proche
		if dist(me.my_position,me.pos_adv_plus_proche)<7: #ADV FONCE SUR MOI
			return me.shoot_vers_equipier_proche # FAIRE PASSE
		else:
			print "ici",shooteur_malin(me)
			return shooteur_malin(me) # CONTINUER NORMAL 



J_1vs1_Strat = SousStrat(j_1vs1)
#Test_Strat = SousStrat(test)

J_2vs2_Strat = SousStrat(j_2vs2)
J_2vs2_Strat_bis= SousStrat(j_2vs2)
Hello = SousStrat(j_2vs2)
Hey = SousStrat(j_2vs2)




