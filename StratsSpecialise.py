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
			##print "adversaire a la balle"

			return me.degager_centre
		else:
			##print"personne ou moi qui ai la balle"
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




