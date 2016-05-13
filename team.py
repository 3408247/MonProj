from Strategies import*
from StratsSpecialise import *
from soccersimulator import SoccerTeam, Player
from decisiontree import DTreeStrategy, gen_features
from keyb_strats import *
import cPickle
import os

#fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"j2.pkl") # put path eg arbre/j2.pkl
#print fn
#tree_j2 = cPickle.load(file(fn))

#tree = cPickle.load(file("./monarbre.pkl"))
#dic = {"dribbler": Strat_dribble,"shoot_sud":Strat_shoot_sud, "shoot_nord":Strat_shoot_nord, "rien":Strat_rien, "degager":Strat_degager}
#treeIA = DTreeStrategy(tree,dic,gen_features)

#tree_j2 = cPickle.load(file("./j2.pkl"))

#dic_2 = {"dribble vers but": Strat_dribble_but,"shoot_sud":Strat_shoot_sud, "shoot_nord":Strat_shoot_nord, "posdef":Strat_posdef, #"degager":Strat_degager,"piquer":Strat_piquer}
#IA_Strat= DTreeStrategy(tree_j2,dic_2,gen_features)


#### Team IA
#TeamIA = SoccerTeam("teamIA",[Player("playerIA",IA_Strat),Player("GARD2",G_2vs2)])


### Pour le tournoi
team1 = SoccerTeam("team1",[Player("j1",J_1vs1_Strat)])
team2 = SoccerTeam("team2",[Player("ATT",Attack2vs2_Strat),Player("Aid",Aideur2vs2_Strat)])
team4 = SoccerTeam("team4",[Player("ATT",Attack4vs4_Strat),Player("Gard",Gardien_Strat),Player("Milieu",Milieu4vs4_Strat),Player("Def",Def4vs4_Strat)])



##### IA DecisionTree
#tree = cPickle.load(file("./tree.pkl"))
#dic = {"dribbler": Strat_dribble,"shoot_sud":Strat_shoot_sud, "shoot_nord":Strat_shoot_nord}
#treeIA = DTreeStrategy(tree,dic,gen_features)
#playerIA = Player("IAtree",treeIA)
#teamIA = SoccerTeam



"""
#### Mes tests
Priya_1a = SoccerTeam("Priya_1a",[Player("a",J_1vs1_Strat)])
Priya_1b =SoccerTeam("Priya_1b",[Player("b",Rien_Strat)])

Priya_2a = SoccerTeam("Priya_2a",[Player("aideur",Aideur2vs2_Strat),Player("Attack",Attack2vs2_Strat)])
Priya_2b =SoccerTeam("Priya_2b",[Player("att",Attack2vs2_Strat),Player("def",Def4vs4_Strat)])
#Priya_2bb = SoccerTeam("Priya_2bb",[Player("k1",FonceurStrat),Player("k2",G_2vs2)])

Priya_4a = SoccerTeam("Priya_4a",[Player("MILIEU",Milieu4vs4_Strat),Player("GARDIEN",Gardien_Strat),Player("Attack",Attack4vs4_Strat),Player("Def",Def4vs4_Strat)])

#Priya_4b =SoccerTeam("Priya_4b",[Player("1ATTb",FonceurStrat),Player("GARDIENb",G_2vs2),Player("2ATTb",FonceurStrat),Player("1DEFb",DefStrat)])
"""





