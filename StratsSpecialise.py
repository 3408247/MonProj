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
		#print"DANS MA MOITIER DE TERRAIN"
		if me.a_la_balle==3:  # SI ADV A LA BALLE
		#	print "ADV A BALLE je degage"

			return me.degager_centre
		else:
		#	print"PERSONNE OU MOI AI BALLE: dribbler vers but adv"
			return me.dribbler_vers(me.but_pos_adv)  


	else: # DANS MOITIER ADV

		#print "DANS SA MOTIER"
		if me.a_la_balle==3:
		#	print"ADV A BALLE je pique"	
			return me.piquer_balle
		else:
		#	print "PERSONNE OU MOI AI BALLE:.."
			if me.dans_zone_de_tir:
		#		print"dans zone de tir"

				if (dist(me.ball_pos,me.but_pos_adv)<GAME_WIDTH/4):  #JE SUIS TRES PRES DES BUTS ADV
		#			print "Tres proche des buts adv"
					if dist(me.ball_pos,me.pos_adv_pr_ball)<12:   # SI ADV EST PROCHE/S'APPROCHE  DE MOI
		#				print "adv s'approche de moi"
						if (me.obs_entre(me.ball_pos,me.but_pos_adv)!=False):
		#					print "adv entre donc shooter/marquer de facon malin"
								
							return me.shooter_malin
 
						else: 
		#					print "personne entre donc shoot"
							return me.shooter_vers(me.but_pos_adv)  #SHOOT 
					else: 	
		#				print "adv ne s'approche pas"
						if (me.obs_entre(me.ball_pos,me.but_pos_adv)!=False):
		#					print"adv entre donc shooter/marquer de facon malin"
							return me.shooter_malin  # CONTINUE A S'APPROCHER DES BUTS
						else:
		#					print "personne entre donc shooter"
							return me.shooter_vers_norm(me.but_pos_adv,5.0)
		



				else: 
		#			print "Je suis pas assez proche donc continuer a dribbler"
					return me.dribbler_vers(me.but_pos_adv)
			else:
		#		print "pas dans zone de tir, donc dribbler vers zone de tir"

				return me.dribbler_vers(me.zone_tir)
					
J_1vs1_Strat = SousStrat(j_1vs1)


#2vs2#

def attack_2vs2(me):
	#print"Attack2vs2"
	if me.ball_pos.x<GAME_WIDTH/2:
		#print"ma moitie"
		if dist(me.my_pos,me.ball_pos)<dist(me.pos_equi_pr_ball,me.ball_pos):
			#print"jfais j1vs1"
			return j_1vs1(me)
		else:
			#print"jfais demar"
			return demarquer(me)
	
	else:
		#print "sa moitie"
		if dist(me.my_pos,me.ball_pos)<dist(me.pos_equi_pr_ball,me.ball_pos):
			#print "je fais j1vs1"
			return j_1vs1(me)
		else:
			#print "jfais demar"
			return demarquer(me)
	

Attack2vs2_Strat = SousStrat(attack_2vs2)

def aideur_2vs2(me):
	#print "AIdeur"
	if me.ball_pos.x<GAME_WIDTH/4:
		#print "Je fais gardien"
		return gardien(me)
	else:
		#print "Je fais attack 2vs2"
		return attack_2vs2(me)

Aideur2vs2_Strat = SousStrat(aideur_2vs2)

"""
def J2_vs2(me):
"""
	

def rien(me):
	return SoccerAction(Vector2D(),Vector2D())

Rien_Strat = SousStrat(rien)	
					






# 4vs4#
"""def d_4vs4(me):

	if (me.ball_pos.x>GAME_WIDTH/2):
		return def_pos_defaut(me)

	else:
		if me.a_la_balle==0: 
			# Personne n'a la balle

				if (me.qui_entre(me.ball_pos,me.pos_equi_plus_proche)==False):
				# Personne entre moi et equipier plus proche

					# Je shoote vers equipier
					return me.shoot_vers(me.pos_equi_plus_proche)

				else:
					return me.shoot_degager
		if me.a_la_balle==
					
"""		
					
	
"""

#Test_Strat = SousStrat(test)

J_2vs2_Strat = SousStrat(j_2vs2)
J_2vs2_Strat_bis= SousStrat(j_2vs2)
Hello = SousStrat(j_2vs2)
Hey = SousStrat(j_2vs2)


"""



