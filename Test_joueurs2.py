import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import SoccerTeam, SoccerMatch, Player
from Strategies import *
#from team import *
from StratsSpecialise import*
from keyb_strats import *
import cPickle 
from decisiontree import DTreeStrategy, gen_features_gardien



tree = cPickle.load(file("entrain_gard5.pkl"))
dic = {"alligne_demi_cercle": Strat_allign,"passe":Strat_passe, "degager":Strat_deg,"protect_cage":Strat_protect}
treeIA = DTreeStrategy(tree,dic,gen_features_gardien)
playerIA = Player("IAtree",treeIA)




team1b =SoccerTeam("team1b",[playerIA,Player("atta",Attack2vs2_Strat)])
 
team1a =SoccerTeam("team1a",[Player("atta",Attack2vs2_Strat),Player("aideur",Aideur2vs2_Strat)])

match = SoccerMatch(team1b, team1a)
#SoccerMatch.save(match,"fichier.match")
soccersimulator.show(match)

SoccerMatch.save(match,"ficmatch.match")
"""
print "ON LOAD"
hmmm = SoccerMatch.load("ficmatch.match")
soccersimulator.show(hmmm)
"""
#print match.strats
#match2 = SoccerMatch.load("fichier.match")

#soccersimulator.show(match2)

"""
print "STRATS"
print match.strats

print "LENGTH STRATS"
print len(match.strats)

print "STATES"
print match.states

print "LENGTH"
print len(match.states)
"""


