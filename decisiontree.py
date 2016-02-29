from soccersimulator import SoccerMatch, SoccerTournament,KeyboardStrategy
from soccersimulator import SoccerTeam, Player, show
#from strategies import RandomStrategy,FonceurStrategy,DefenseStrategy
from soccersimulator import settings, Vector2D,DecisionTreeClassifier,export_graphviz
import cPickle
from Outils import*
from Strategies import *
from keyb_strats import *

#LANCER CE FICHIER DANS LE TERMINAL POUR SAUVEGARDER LES PACKETS D'EXEMPLES

## Fonction de generation de descripteurs
def gen_features(state,id_team,id_player):

    Etat=MyState(state,id_team,id_player)
    
    d_ball_me      = Etat.dist_player_ball
    d_ball_but_adv = Etat.dist_but_adv_ball
    d_me_adv       = dist(Etat.my_position,Etat.pos_adv_plus_proche)  

    #bpos = state.ball.position
    #mpos = state.player_state(id_team,id_player).position
    #myg = Vector2D((id_team-1)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
    #hisg = Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)


    #return [bpos.distance(mpos),bpos.distance(myg),bpos.distance(hisg)]
    return [d_ball_me,d_ball_but_adv,d_me_adv]	

def build_apprentissage(fn,generator):
    ex_raw = KeyboardStrategy.read(fn)
    exemples = []
    labels = []
    for x in ex_raw:
        exemples.append(gen_features(x[1],x[0][0],x[0][1]))
        labels.append(x[0][2])
    return exemples,labels

def apprendre_arbre(train,labels,depth=5):
    tree= DecisionTreeClassifier()
    tree.fit(train,labels)
    return tree

def affiche_arbre(tree):
    long = 10
    sep1="|"+"-"*(long-1)
    sepl="|"+" "*(long-1)
    sepr=" "*long
    def aux(node,sep):
        if tree.tree_.children_left[node]<0:
            ls ="(%s)" % (", ".join( "%s: %d" %(tree.classes_[i],int(x)) for i,x in enumerate(tree.tree_.value[node].flat)))
            return sep+sep1+"%s\n" % (ls,)
        return (sep+sep1+"X%d<=%0.2f\n"+"%s"+sep+sep1+"X%d>%0.2f\n"+"%s" )% (tree.tree_.feature[node],tree.tree_.threshold[node],aux(tree.tree_.children_left[node],sep+sepl),
                                   tree.tree_.feature[node],tree.tree_.threshold[node],aux(tree.tree_.children_right[node],sep+sepr))
    return aux(0,"")



## constitution de la base d'entrainement et des labels
train,labels = build_apprentissage("./test.tree",gen_features)
## apprentissage de l'arbre
tree = apprendre_arbre(train,labels)
## sauvegarde de l'arbre
cPickle.dump(tree,file("tree.pkl","w"))
with file("tree.dot","w") as fn:
        export_graphviz(tree,fn)
  
print  affiche_arbre(tree)
# dot -Tpdf -o tree.pdf tree.dot


