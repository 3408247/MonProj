from soccersimulator import *
from Outils import*
from Strategies import*
import pickle

GAMMA  =0.6
ALPHA  =0.9
 
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
		
		dict_a["rien"]=0    # on met ici des string("gard")et apres on fera la correspondance string vers strat
		dict_a["fonceur"]=0
		
		
		dic_s[s]=dict_a    # dic_s= { (0,0): {"fonceur": 0, "gard":0} , (0,1) : {"fonceur": 0, "gard":0} }
	
	return dic_s


def MonteCarlo(q,scenarios,idt,idp): #scenarios est une liste de couple (etat,action)  remarque: dernier etat none
      # q est dico de dico 
      #parcurir liste a lenvers
	

	for sce in scenarios:
		
		while sce[0]!=None:

			
			R = 0
			act_choisi = sce[1]
	
			for t in range (MAX_STEP-1,0,-1):

				st=sce[t]
			
			
				R= GAMMA*R + recompense(st,idt,idp)
				etat_discretise=discretisation(st,idt,idp)
				q[etat_discretise][act_choisi]=q[etat_discretise][act_choisi] + ALPHA*(R-q[etat_discretise][act_choisi])  #Que faire la maj comme ca ou bien faire return q ?
 	return q


		
def prendreaction_et_maj(le_match,idt,idp,fichier_dic):      
	
	observations_allsteps=le_match.states
	

	#SI LE DICTIONNAIRE EST VIDE, AU DEBUT, TOUT INITALISER A ZERO  (ou random??)
	dico_dico= pickle.load(open(fichier_dic,"r"))                                   #PROBLEME SI FICHIER EST FICHIER NORMAL VIDE
	if dico_dico=={}:
		dico_dico=initialisation(observations_allsteps)


	scenarios=[]
	
	joueur_stattaken = le_match.strats



	for step_obs in observations_allsteps:      # observation pour un step du match
		
		step_discretise=discretisation(step_obs,idt,idp)
	
		#CHOISIR ACTION A PRENDRE
		actions_possibles=dico_dico(step_discretise)      #LES ACTIONS POSSIBLES(AVEC LEUR VALEUR AFFECTEE) CORRESPONDANT A LETAT COURANT
		
		valeur_max=-999999999999999
		for action in actions_possibles:
			strat_name=action          		     #LA STRATEGIE  (clef du dic)
			valeur_associe=actions_possibles[action]     #LA VALEUR ASSOCIEE               EST-CE QUE CA MARCHE COMME CA AVEC LES DICTIONNAIRES ?
			if valeur_associe>=valeur_max:
				nom_action_choisie=strat_name  # CHOISIR LACTION AYANT VALEUR MAX 
		




	        # LA MISE A JOUR 
		for eachstep in joueur_strattaken
				
			required_team=eachstep[idt]              #RECUPERER LES STRATS PRIS PAR LEQUIPE CONCERNEE
			player_actiontaken= required_team[idp]	  #RECUPERER L'ACTION PRIS PAR LE JOUEUR CONCERNE
			
			scenarios.append((step_obs,player_action_taken))    #on ajoute couple (etatbrut,actionpris) a la liste scenarios



		dico_dico=MonteCarlo(dico_dico,scenarios,idt,idp)               #Cette fonction met a jour le dico de dico .. est-ce que ca marche comme ca en python ?

		pickle.dump(dico_dico,open(fichier_dic,"w"))     # Le fichier s'appelera tout le temps fichierdic.pkl comment faire pour changer ?


	return nom_action_choisie


def QStrategy(match,idt,idp,fichier_dic,dic_corresp):
	nom_action= prendreaction_et_maj(match,idt,idp,fichier_dic)

	for clef in dic_corresp:
		if clef==nom_action:
			return dic_corresp[clef]
		else:
			print "action pas dans dic_corresp.."
			return

	print "je sais pas"
	return






		

# C ici la ligne 4 du slide 
	
	"""liste=fichier_match.soccermatch.load 
 	

	for etape in liste:

		etat_discret=discretisation(state)

		DIC_S=fonction_q(etat_discret)"""

	
	
	
		







	
	
	

