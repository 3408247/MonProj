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
		print"DANS MA MOITIER DE TERRAIN"
		if me.a_la_balle==3:  # SI ADV A LA BALLE
			print "ADV A BALLE je degage"

			return me.degager_centre
		else:
			print"PERSONNE OU MOI AI BALLE: dribbler vers but adv"
			return me.dribbler_vers(me.but_pos_adv)  


	else: # DANS MOITIER ADV

		print "DANS SA MOTIER"
		if me.a_la_balle==3:
			print"ADV A BALLE je pique"	
			return me.piquer_balle
		else:
			print "PERSONNE OU MOI AI BALLE:.."
			if me.dans_zone_de_tir:
				print"dans zone de tir"

				if (dist(me.ball_pos,me.but_pos_adv)<GAME_WIDTH/4):  #JE SUIS TRES PRES DES BUTS ADV
					print "Tres proche des buts adv"
					if dist(me.ball_pos,me.pos_adv_pr_ball)<12:   # SI ADV EST PROCHE/S'APPROCHE  DE MOI
						print "adv s'approche de moi"
						if (me.obs_entre(me.ball_pos,me.but_pos_adv)!=False):
							print "adv entre donc shooter/marquer de facon malin"
								
							return me.shooter_malin
 
						else: 
							print "personne entre donc shoot"
							return me.shooter_vers(me.but_pos_adv)  #SHOOT 
					else: 	
						print "adv ne s'approche pas"
						if (me.obs_entre(me.ball_pos,me.but_pos_adv)!=False):
							print"adv entre donc shooter/marquer de facon malin"
							return me.shooter_malin  # CONTINUE A S'APPROCHER DES BUTS
						else:
							print "personne entre donc shooter"
							return me.shooter_vers_norm(me.but_pos_adv,5.0)
		



				else: 
					print "Je suis pas assez proche donc continuer a dribbler"
					return me.dribbler_vers(me.but_pos_adv)
			else:
				print "pas dans zone de tir, donc dribbler vers zone de tir"

				return me.dribbler_vers(me.zone_tir)
					

#2vs2#

def j_2vs2(me):

	

	return j_1vs1(me)

"""
def J2_vs2(me):
"""
	

	
					



def g_2vs2(me):	
	
	
	if dist(me.ball_pos,me.but_pos)<DCERCLE_RAYON+5:
	# La balle est proche de mes buts
	
		if dist(me.but_pos,me.pos_adv_pr_but)>5*DCERCLE_RAYON:
		# L'adversaire le plus proche est encore loin 

	 		if me.a_la_balle==0: 
			# Personne n'a la balle

				if (me.obs_entre(me.ball_pos,me.pos_equi_pr_ball)==False):
				# Personne entre moi et equipier plus proche

					# Je shoote vers equipier
					return me.shoot_vers(me.pos_equi_pr_ball)
								
				else:
				# Il y a quelqu'un entre moi et equipier plus proche

					# Je degage le ballon
					return me.degager
			else:
				if me.test_peut_shooter:
					
					return me.degager
				else:				
					
					return alligne_demi_cercle(me)

		else: 
		# L'adversaire le plus proche est pres des buts

			# Je protege mes buts
			return protect_cage(me)


	else:
	# La balle est encore tres loin

		if dist(me.ball_pos,me.my_pos)<10:
		# La balle est assez proche
			
			if dist(me.but_pos_adv,me.pos_adv_pr_but)<20: 
			#L'adversaire le plus proche est pres des buts

				if dist(me.ball_pos,me.my_pos)<dist(me.ball_pos,me.pos_adv_pr_ball):
				# Toutefois je suis plus proche de la balle que lui
								
					if (me.obs_entre(me.ball_pos,me.pos_equi_pr_ball)==False):
					# Personne entre moi et equipier plus proche
						
						# Je shoote vers equipier
						return me.shoot_vers(me.pos_equi_pr_ball)

					else:
					# Il y a quelqu'un entre moi et equipier plus proche

						# Je degage le ballon
						return me.degager
				else:	
				# Et c'est l'adversaire qui est plus proche de la balle
					
					# Je protege mes cages
					return protect_cage(me)
			else:
			# L'adversaire le plus proche est encore loin	
		
				if (me.obs_entre(me.ball_pos,me.pos_equi_pr_ball)==False):
				# Personne entre, shoot vers equi
					return me.shoot_vers(me.pos_equi_pr_ball)
				else:
			#		print " qq entre, degage"
					return me.degager
		else:
			#"alligne sur demi cercle"
			return alligne_demi_cercle(me)
		



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
					
	

J_1vs1_Strat = SousStrat(j_1vs1)
#Test_Strat = SousStrat(test)

J_2vs2_Strat = SousStrat(j_2vs2)
J_2vs2_Strat_bis= SousStrat(j_2vs2)
Hello = SousStrat(j_2vs2)
Hey = SousStrat(j_2vs2)

G_2vs2= SousStrat(g_2vs2)




