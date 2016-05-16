from soccersimulator import *
from Outils import*
import pickle
import random 

GAMMA  =0.9    # Poids/facteur de recompense avec temps
ALPHA  =0.2    # Facteur de convergence 
 


##############################################################################################################
#### DISCRETISATION ##########################################################################################
##############################################################################################################


def discretisation(state, id_team, id_player):   # Extraire les s des O
        """ Discretiser un etat pour in id_t et id_p donnE
        """

	S=MyState(state,id_team,id_player)

	L=[]
	
     ### Dans ma moitie ou pas ####
	if S.ball_pos.x<=GAME_WIDTH/2:
		a=0	
	else:
		a=1
	L.append(a)

     ### qui a la balle, adv, moi ou personne ####
	if S.a_la_balle==3:
		b=3
	if S.a_la_balle==1:
		b=1
	if S.a_la_balle==0:
		b=0
	L.append(b)

     ### Dans zone de tir ou pas ####
	if S.dans_zone_de_tir==False:
		c=0
	else:
		c=1
	L.append(c)

     ### Quelqu'un entre ball et but adv ####
	if S.obs_entre(S.ball_pos,S.but_pos_adv)==False:
		d=0
	else:
		d=1
	L.append(d)

     ### Direction de l'adversaire ####
	adv=S.adv_pr_posobj(S.ball_pos)
	moi=S.player_moi
	proche=dist(S.ball_pos,S.pos_adv_pr_ball)<7.
	oppose=adv.vitesse.dot(moi.vitesse)<=0

	if (proche and oppose and S.est_devant(S.balle,adv) and S.est_enhaut(S.balle,adv)):
		e=0
	if (proche and oppose and S.est_devant(S.balle,adv) and not(S.est_enhaut(S.balle,adv))):
		e=1
	
	if (not(oppose) and not(S.est_devant(S.balle,adv))):
		e=3
	else:
		e=4
	L.append(e)
     	
     ### 0 si adv plus proche de balle, 1 sinon ####
	god=dist(S.pos_adv_pr_ball,S.ball_pos)-dist(S.my_pos,S.ball_pos)
	
	if god<0:
		f=0
	else:
		f=1
	L.append(f)	
    	"""
     ### 1 si balle est a une distance de <=30 des buts adv, 0 sinon ####
	if dist(S.ball_pos,S.but_pos_adv)<=30:
		g=1
	else:
		g=0
	"""
	L.append(g)
	
	
	return tuple(L)

##############################################################################################################
#### INITIALISATION ##########################################################################################
##############################################################################################################

def initialisation_q():  

	""" Initialiser les valeurs associEs au choix d'actions possibles a 0 ou valeur aleatoire
        """
	
	dict_a={}	
		
	dict_a["qdribler_vers_but"]=random.uniform(0,3)   
	dict_a["qdribler_vers_zone"]=random.uniform(0,3)
	dict_a["qdegager"]=random.uniform(0,3)
	dict_a["qshooter_bas"]=random.uniform(0,3)
	dict_a["qshooter_haut"]=random.uniform(0,3)
	dict_a["qshooter_fort"]=random.uniform(0,3)
	dict_a["qshooter_malin"]=random.uniform(0,3)	
	dict_a["qshooter_dansbut"]=random.uniform(0,3)
	
	return dict_a


##############################################################################################################
#### PRENDRE_ACT #############################################################################################
##############################################################################################################

		
def prendre_act(etatbrut_courant,idt,idp,nom_fichier_dic):
        """ Etant donnE un etatbrut, prendre l'action ayant la valeur maximale associE (valeurs stockEs dans nom_fichier_dic
        """

	if etatbrut_courant==None:
		
		return
	
        # Discretiser l'etat brut courant
	etatdis_courant= discretisation(etatbrut_courant,idt,idp)

	# Ouvrir nom_fichier_dic en lecture, stocker dans dico_dico
	fichier_ouvert_lec= open(nom_fichier_dic,"r")
	dico_dico= pickle.load(fichier_ouvert_lec)

	# Si l'etat discret courant ne se trouve pas dans dico_dico, on initialise les valeurs associEs aux actions possible pour cet etat 
	if etatdis_courant not in dico_dico.keys():

		fichier_ouvert_lec.close()
		dico_dico[etatdis_courant]=initialisation_q()
		fichier_ouvert_ecri = open(nom_fichier_dic,"w")
		pickle.dump(dico_dico,fichier_ouvert_ecri) 
		fichier_ouvert_ecri.close()
	#else:
        #        print "etat est deja dans dic , donc no init"

	
	fichier_ouvert_lec.close()
	

        # On choisit maintenant l'action ayant la plus grande valeur associE a cet etat courant
	actions_possibles=dico_dico[etatdis_courant]

	valeur_max=-999999999999999
	nom_action_choisie="qdribler_vers_but"
	for action in actions_possibles:     # Prenant les clefs de actions_possible, par ex la clef "fonceur"
		strat_name=action          		     #LA STRATEGIE  # clef du dic eg "fonceur"
		valeur_associe=actions_possibles[action]     #LA VALEUR ASSOCIEE  # eg 0
		if valeur_associe>=valeur_max:
			nom_action_choisie=strat_name        # CHOISIR LACTION AYANT VALEUR MAX  #eg "fonceur"  
			valeur_max=valeur_associe

	# On retourne cette action 
	
	return str(nom_action_choisie)


##############################################################################################################
#### RECOMPENSE ##############################################################################################
##############################################################################################################

def recompense(state, id_team, id_player):   
        """ Associer a un etat, une recompense
        """
	Etat=MyState(state,id_team,id_player)	
	r=0
	
        ### J'ai marquE un but ####
	if ((Etat.ball_pos.x==Etat.but_pos_adv.x) and (Etat.ball_pos.y>=Etat.but_pos_adv.y-GOAL_HEIGHT/2) and (Etat.ball_pos.y<=Etat.but_pos_adv.y+GOAL_HEIGHT/2)):
		r+=100
		
        ### Adversaire a marquE un but ####
	if ((Etat.ball_pos.x==Etat.but_pos.x) and (Etat.ball_pos.y>=Etat.but_pos.y-GOAL_HEIGHT/2) and (Etat.ball_pos.y<=Etat.but_pos.y+GOAL_HEIGHT/2)):
		r+=-150

        ### Personne n'a la balle ####
	if (Etat.a_la_balle==0):
		r+=5

        ### J'ai la balle ####
	if (Etat.a_la_balle==1): 
		r+=50

        ### Adversaire a la balle ####		
	if (Etat.a_la_balle==3):
		r+=-50

        ### Balle dans zone de tir ####
	if Etat.dans_zone_de_tir==True:
		r+=10

        ### Balle dans moitiE adverse ####	
	if Etat.ball_pos.x>=GAME_WIDTH/2:
		r+=5
        ### Balle dans ma moitiE ####
	else:
		r+=-1

        ### Balle proche des buts adv ###
	if dist(Etat.ball_pos,Etat.but_pos_adv)<=30:
		r+=10
		

	return r


##############################################################################################################
#### MONTECARLO ##############################################################################################
##############################################################################################################

def MonteCarlo(q,scenarios,idt,idp): #scenarios est une liste de couple (etat,action)  remarque: dernier etat none
        """ q est le dictionnaire de dictionnaire
            scenarios est le couple(etatbrut,action)
        """
        
	
	Q = q  # Travailler sur la copie de q

	i=0
	longeur=len(scenarios)
   
	for sce in scenarios:

		if sce[0]!=None:   # Ne sert a rien ici 

			R = 0
			act_choisi = sce[1]
	


			for t in range (longeur-1,-1,-1):      # Parcourir les scenarios a l'envers
				
				st=scenarios[t][0]
				
				R= GAMMA*R + recompense(st,idt,idp)

				etat_discretise=discretisation(st,idt,idp)

                                # Mettre a jour le dictionnaire utilisant methode MonteCarlo 
				Q[etat_discretise][act_choisi]=Q[etat_discretise][act_choisi] + ALPHA*(R-Q[etat_discretise][act_choisi])  

		i=i+1


 	return Q

##############################################################################################################
#### MISE A JOUR##############################################################################################
##############################################################################################################

def maj(le_match,idt,idp,nom_fichier_dic):
        """ Lire les etats et les actions pris pendant le_match, mettre a jour le dictionnaire de dictionnaire 
        """
        
	etatsbruts_allsteps=le_match.states
        print "longueur des etats bruts", len(le_match.states)
	joueur_stratstaken = le_match.strats 
	#print "joueur strats taken", joueur_stratstaken
        print "longueur des strats taken", len(le_match.strats)

	scenarios=[]


	liste_etatsdis=[]
	
	step_num=0
	for step_brut in etatsbruts_allsteps:

		liste_etatsdis.append(discretisation(step_brut,idt,idp))

                # Obtenir l'action pris par joueur de idt et idp lors de cet etat du match 
		required_step=joueur_stratstaken[step_num]
		required_team=required_step[idt-1]
		player_action_taken= required_team[idp]
	
		if player_action_taken=="qstrat":
			player_action_taken=joueur_stratstaken[step_num+1][idt-1][idp] #Car il y a un ptit prob dans match.strats, il affiche la premiere strategie comme qstrat tout le tmeps
		
                # Construire la liste (etatbrut, action) petit a petit 
		scenarios.append((step_brut,player_action_taken))

		step_num=step_num+1

		

        print "longeur scenarios", len(scenarios)

	f_ouvert_lec= open(nom_fichier_dic,"r")

	old_dic=pickle.load(f_ouvert_lec)

	f_ouvert_lec.close()

        # MAJ du dictionnaire avec MonteCarlo 
	new_dic= MonteCarlo(old_dic,scenarios,idt,idp)

	f_ouvert_ecri= open(nom_fichier_dic,"w")

	pickle.dump(new_dic,f_ouvert_ecri)

	f_ouvert_ecri.close()
        
	
	print" FIN  MAJ ET ECRITURE DANS FICHIER"

        print "#############"
        print "FIN MAJ"
        print "##############"


	return 
	
		

	

	
	
		







	
	
	

