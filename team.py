from Strategies import*
from StratsSpecialise import *
from soccersimulator import SoccerTeam, Player
from decisiontree import DTreeStrategy, gen_features
from keyb_strats import *
import cPickle
import os

fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"monarbre.pkl")
tree = cPickle.load(file(fn))

#tree = cPickle.load(file("./monarbre.pkl"))
dic = {"dribbler": Strat_dribble,"shoot_sud":Strat_shoot_sud, "shoot_nord":Strat_shoot_nord, "rien":Strat_rien, "degager":Strat_degager}
treeIA = DTreeStrategy(tree,dic,gen_features)



#### Mes tests
Priya_1a = SoccerTeam("Priya_1a",[Player("Keystrat",keystrat_test)])
Priya_1b =SoccerTeam("Priya_1b",[Player("j1vs1",J_1vs1_Strat)])

Priya_2a = SoccerTeam("Priya_2a",[Player("j1",J_2vs2_Strat),Player("j2",Gard_shoot_but)])
Priya_2b =SoccerTeam("Priya_2b",[Player("1ATTb",FonceurStrat),Player("GARDIENb",Gard_shoot_but)])
Priya_2bb = SoccerTeam("Priya_2bb",[Player("k1",J_2vs2_Strat),Player("k2",Gard_shoot_but)])

Priya_4a = SoccerTeam("Priya_4a",[Player("MILIEU",J_2vs2_Strat),Player("GARDIENa",Gard_shoot_but),Player("2ATTa",FonceurStrat),Player("1DEFa",DefStrat)])

Priya_4b =SoccerTeam("Priya_4b",[Player("1ATTb",FonceurStrat),Player("GARDIENb",Gard_shoot_but),Player("2ATTb",FonceurStrat),Player("1DEFb",DefStrat)])


### Pour le tournoi
team1 = SoccerTeam("team1",[Player("f1",J_1vs1_Strat)])
team2 = SoccerTeam("team2",[Player("ATT1",J_2vs2_Strat_bis),Player("GARD",Gard_shoot_but)])
team4 = SoccerTeam("team4",[Player("ATT1",FonceurStrat),Player("gk2",Gard_shoot_but),Player("ATT2",FonceurStrat),Player("DEF1",DefStrat)])


##### IA DecisionTree
#tree = cPickle.load(file("./tree.pkl"))
#dic = {"dribbler": Strat_dribble,"shoot_sud":Strat_shoot_sud, "shoot_nord":Strat_shoot_nord}
#treeIA = DTreeStrategy(tree,dic,gen_features)
#playerIA = Player("IAtree",treeIA)
#teamIA = SoccerTeam


