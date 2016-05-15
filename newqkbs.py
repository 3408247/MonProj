import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from newqstrat import *


class SStrat(BaseStrategy):
    def __init__(self,ss_strat):
        BaseStrategy.__init__(self,ss_strat.__name__)
        self.strat=ss_strat 

    def compute_strategy(self,state,idteam,idplayer): #ou faire miroir ici
	self.state = state
     
        action,self.name=self.strat(MyState(self.state,idteam,idplayer))
	#print action
        #if(idteam!=1):
	   #action= miroir_action(action)

        #print action
        return action

QDribbut= SStrat(qdribler_vers_but)
QDriblerzone = SStrat(qdribler_vers_zone)
QDegager = SStrat(qdegager)
QShootBas = SStrat(qshooter_bas)
QShootHaut= SStrat(qshooter_haut)
QShooterMalin= SStrat(qshooter_malin)
QShootFort= SStrat(qshooter_fort)
QDegager = SStrat(qdegager)

KBS=KeyboardStrategy()
KBS.add("y",QShootHaut)
KBS.add("h",QShootBas)
KBS.add("b",QShootFort)
KBS.add("d",QDribbut)
KBS.add("u",QShooterMalin)
KBS.add("e",QDegager)


