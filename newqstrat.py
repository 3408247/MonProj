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
#def piquer(me):


########################################################################################
### REDEF DE QQS STRATEGIES A UTILISER DANS QLEARNING ##################################
########################################################################################

"""Il s'agit des actions possibles a prendre par le joueur utilisant apprentissage supervise;
"""


def qdribler_vers_but(me):
	if me.test_peut_shooter:
		return (me.qshootdribble_vers(me.but_pos_adv),"qdribler_vers_but")
	else:
		return (me.qcourir_versball,"qdribler_vers_but")

def qdribler_vers_zone(me):
	if me.test_peut_shooter:
		return (me.qshootdribble_vers(me.zone_tir),"qdribler_vers_zone")
	else:
		return (me.qcourir_versball,"qdribler_vers_zone")

def qdegager(me):
	if me.test_peut_shooter:
		return (me.qshoot_degager,"qdegager")
	else:
		return (me.qcourir_versball,"qdegager")

def qshooter_bas(me):
	if me.test_peut_shooter:
		return (me.qpetitshootbas_vers(me.but_pos_adv),"qshooter_bas")
	else:
		return (me.qcourir_versball,"qshooter_bas")

def qshooter_haut(me):
	if me.test_peut_shooter:
		return (me.qpetitshoothaut_vers(me.but_pos_adv),"qshooter_haut")
	else:
		return (me.qcourir_versball,"qshooter_haut")

def qshooter_fort(me):
	if me.test_peut_shooter:
		return (me.qshootfort_vers(me.but_pos_adv),"qshooter_fort")
	else:
		return (me.qcourir_versball,"qshooter_fort")

def qshooter_malin(me):
	if me.test_peut_shooter:
		return (me.shoot_malin,"qshooter_malin")
	else:
		return (me.qcourir_versball,"qshooter_malin")

def qshooter_dansbut(me):
	if me.test_peut_shooter:
		return (me.qshoot_dansbut,"qshooter_dansbut")
	else:
		return (me.qcourir_versball,"qshooter_dansbut")
	

########################################################################################
########################################################################################


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


########################################################################################
### La Strategie QStrat adoptE par joueur IA ###########################################
########################################################################################	

def qstrat(me):

	etatcour_brut= me.state
	mon_idt= me.key[0]
	mon_idp= me.key[1]
	
	nom_act_choisie= prendre_act(etatcour_brut,mon_idt,mon_idp,NOM_FICHIER_DIC)
	
	variable=eval(nom_act_choisie)	

	return variable(me)

QStrat = SurStrat(qstrat)

	

