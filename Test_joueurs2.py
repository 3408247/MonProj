import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import SoccerTeam, SoccerMatch, Player
from Strategies import *
#from team import *
from StratsSpecialise import*
from keyb_strats import *
import cPickle 
from decisiontree import DTreeStrategy, gen_features_gardien



tree = cPickle.load(file("entrain_gard2.pkl"))
dic = {"alligne_demi_cercle": Strat_allign,"passe":Strat_passe, "degager":Strat_deg,"protect_cage":Strat_protect}
treeIA = DTreeStrategy(tree,dic,gen_features_gardien)
playerIA = Player("IAtree",treeIA)





team1b =SoccerTeam("team1b",[Player("gard",Gardien_Strat),Player("atta",Attack4vs4_Strat),Player("milieu",Milieu4vs4_Strat),Player("def",Def4vs4_Strat)])
 
team1a =SoccerTeam("team1a",[Player("atta",Attack4vs4_Strat),Player("def",Def4vs4_Strat),Player("gard",Gardien_Strat),Player("KBS_M",KBS_Milieu)])

match = SoccerMatch(team1b, team1a)
#SoccerMatch.save(match,"fichier.match")
soccersimulator.show(match)

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


