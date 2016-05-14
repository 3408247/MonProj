from soccersimulator.settings import  *
from soccersimulator import  Vector2D, SoccerTeam, Player, SoccerAction
from soccersimulator import KeyboardStrategy, BaseStrategy
from soccersimulator import settings
from soccersimulator import SoccerMatch
from soccersimulator import SoccerTeam
import soccersimulator
from newqlearn import *

from Outils import *

NOM_FICHIER_DIC = "learningdic"
#DIC_CORRESP = {'fonceur':Fonceur_Strat, 'rien':Rien_Strat,'gardien':Gardien_Strat}
def piquer(me):

def qdribler_vers_but(me):
	if me.test_peut_shooter:
		return me.qshootdribble_vers(me.ball_pos)
	else:
		return me.qcourir_versball

def qdribler_vers_zone(me):
	if me.test_peut_shooter:
		return me.qshootdribble_vers(me.zone_tir)
	else:
		return me.qcourir_versball

def qdegager(me):
	if me.test_peut_shooter:
		return me.qshoot_degager
	else:
		return me.qcourir_versball

def qshooter_bas(me):
	if me.test_peut_shooter:
		return me.qpetitshootbas_vers(me.ball_pos)
	else:
		return me.qcourir_versball

def qshooter_haut(me):
	if me.test_peut_shooter:
		return me.qpetitshoothaut_vers(me.ball_pos)
	else:
		return me.qcourir_versball

def qshooter_fort(me):
	if me.test_peut_shooter:
		return me.qshootfort_vers(me.ball_pos)
	else:
		return me.qcourir_versball

def qshooter_malin(me):
	if me.test_peut_shooter:
		return me.shoot_malin
	else:
		return me.qcourir_versball

def qshooter_dansbut(me):
	if me.test_peut_shooter:
		return me.qshoot_dansbut
	else:
		return me.qcourir_versball	




class SurStrat(BaseStrategy):
    def __init__(self,sur_strat):
        BaseStrategy.__init__(self,sur_strat.__name__)
        self.strat=sur_strat 

    def compute_strategy(self,state,idteam,idplayer): #ou faire miroir ici
	self.state = state
     
        action,self.name=self.strat(MyState(self.state,idteam,idplayer))
	#print action
        #if(idteam!=1):
	   #action= miroir_action(action)

        #print action
        return action
	

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

QStrat = SurStrat(qstrat)

	

