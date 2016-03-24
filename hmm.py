from soccersimulator import *
from Outils import*
from Strategies import*

GAMMA=0.6

def recompense(state, id_team, id_player):   # associe a un etat, une recompense 
	Etat=MyState(state,id_team,id_player)	

	if (Etat.ball_pos.x=Etat.but_pos_adv.x) and (Etat.ball_pos.y>=Etat.but_pos_adv.y-GOAL_HEIGHT/2) and (Etat.ball_pos.y<=Etat.but_pos_adv.y+GOAL_HEIGHT/2):
		r=100

	if (Etat.ball_pos.x=Etat.but_pos.x) and (Etat.ball_pos.y>=Etat.but_pos.y-GOAL_HEIGHT/2) and (Etat.ball_pos.y<=Etat.but_pos.y+GOAL_HEIGHT/2):
		r=-100


	if Etat.qui_a_la_balle==1 or Etat.qui_a_la_balle==2:
		r=5
	else:
		r=-5

	return r



def discretisation(state, id_team, id_player):   # Extraire les s des O
	Etat=MyState(state,id_team,id_player)	
	
	liste=[]

    	d_me_ball= dist(Etat.ball_pos,Etat.my_pos)

	if d_me_ball<10:
		x0=0
	else:
		x0=1

	liste.append(x0)


    	d_ball_advproche_ball = dist(Etat.ball_pos,Etat.pos_adv_pr_ball) 
	
	if d_ball_advproche_ball<30:
		x1=0
	else:
		x1=1

	liste.append(x1)
	
	
	return tuple(liste)


	
#initialisation des Q(s,a) a zero quoi
def initialisation_q(etat_dis):  # etat_dis est le tuple d'etats discrets(entiers) renvoyE par la fonction discretisation 
	
	dic_s={}

	for s in etat_dis:
		dict_a={}	
		
		dict_a["fonceur"]=0    # on met ici des string("gard")et apres on fera la correspondance string vers strat
		dict_a["gard"]=0
		
		
		dic_s[s]=dict_a    # dic_s= { (0,0): {"fonceur": 0, "gard":0} , (0,1) : {"fonceur": 0, "gard":0} }
	
	return dic_s

				
def discretiser_match(match):

	liste=[]
	
	for step in match:
		LIRE LETAT COMPLET DU MATCH
		s= discretisation(DE CET ETAT COMPLET)
			
		a= LIRE ACTION PRIS
		couple=(s,a)

		liste.append(couple)
	
	return liste

		



def MonteCarlo(q, scenarios, state, idt, idp):

	etat_dis= discretisation(state, idt, idp)
	Q_s_a = initialisation_q(etat_dis)

	
	for sce in scenarios:
	
		while sce[0]!=None:
			for cle in Q_s_a:
			
				if sce[0]==cle:

					
		



	
def MonteCarlo(q,scenarios,state,idt,idp): #scenarios est une liste de couple (etat,action)  remarque: dernier etat none
      # q est dico de dico 
      #parcurir liste a lenvers
	

	for sce in scenarios:
		
		while sce[0]!=None:
			

		R=0
	
		for t in range (MAX_STEP-1,0):
			
			
			R= GAMMA*R + recompense(state,idt,idp)
			q( )=q( ) + ALPHA*(R-q( ))
 


		
def letruc(match):

	for step in match:

		etat_discret=discretisation(state)

		DIC_S=fonction_q(etat_discret)

		

	
	

