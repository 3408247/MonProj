import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from Strategies import *
from StratsSpecialise import *
from newqlearn import *

from Outils import *

NOM_FICHIER_DIC = "lala"
DIC_CORRESP = {'fonceur':Fonceur_Strat, 'rien':Rien_Strat,'gardien':Gardien_Strat}


def qstrat(me):

	print "##########################################"
	print "ETAT"
	etatcour_brut= me.state
	print"DISCRETISE:",discretisation(etatcour_brut,me.key[0],me.key[1])
	print "##########################################"
	
	mon_idt= me.key[0]
	print"monidt:",mon_idt
	mon_idp= me.key[1]
	print"monidp:",mon_idp

	nom_act_choisie= prendre_act(etatcour_brut,mon_idt,mon_idp,NOM_FICHIER_DIC)
	
	#print "action choisie est:", nom_act_choisie
	#strat_corresp= corresp(nom_act_choisie,DIC_CORRESP)
	#print "Result de la correspondance", strat_corresp
	variable=eval(nom_act_choisie)	

	return variable(me)

		
Q_Strat = SousStrat(qstrat)



