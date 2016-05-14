from soccersimulator import *
from Outils import*
import pickle

GAMMA  =0.7
ALPHA  =0.9
 


##############################################################################################################



def discretisation(state, id_team, id_player):   # Extraire les s des O
	"""Etat=MyState(state,id_team,id_player)	
	
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

	if (proche and oppose and S.est_devant(S.balle,adv) and S.est_en_haut(S.balle,adv)):
		e=0
	if (proche and oppose and S.est_devant(S.balle,adv) and S.est_en_bas(S.balle,adv):
		e=1
	
	if (not(oppose) and not(S_est_devant(S.balle,adv))):
		e=3
	L.append(e)

     ### 0 si adv plus proche de balle, 1 sinon ####
	god=dist(S.pos_adv_pr_ball,S.ball_pos)-dist(S.my_pos,S.ball_pos)
	
	if god<0:
		f=0
	else:
		f=1
	L.append(f)	

	
	return tuple(L)

##############################################################################################################

	
#initialisation des Q(s,a) a zero quoi
def initialisation_q():  # etat_dis est le tuple d'un etat discretisE (renvoyE par la fonction discretisation)
	

	dict_a={}	
		
	dict_a["qdribler_vers_but"]=0    # on met ici des string("rien")et apres on fera la correspondance string vers strat
	dict_a["qdribler_vers_zone"]=0
	dict_a["qdegager"]=0
	dict_a["qshooter_bas"]=0
	dict_a["qshooter_haut"]=0
	dict_a["qshooter_fort"]=0
	dict_a["qshooter_malin"]=0	
	dict_a["qshooter_dansbut"]=0
	
	#dict_a = {"rien": 0, "fonceur":0, "gardien":0}
	return dict_a




		
def prendre_act(etatbrut_courant,idt,idp,nom_fichier_dic):      
	
	if etatbrut_courant==None:
		print "dernier etat_brut"
		return

	etatdis_courant= discretisation(etatbrut_courant,idt,idp)
	

	#SI LE DICTIONNAIRE EST VIDE, AU DEBUT, TOUT INITALISER A ZERO  (ou random??)
	#print "on ouvre le fichier en lecture"
	fichier_ouvert_lec= open(nom_fichier_dic,"r")
	#print "on stocke dans dico ce fichier"
	dico_dico= pickle.load(fichier_ouvert_lec)                                   #PROBLEME SI FICHIER EST FICHIER NORMAL VIDE, .. donc deja ecrire un dico vide dans le fichier initial
	if etatdis_courant not in dico_dico.keys():
	#	print "dico en effet vide"
	#	print "on ferme ce fichier"
		fichier_ouvert_lec.close()
	#	print "on rentre dans initialisation"
		dico_dico[etatdis_courant]=initialisation_q()
	#	print " on ouvre le fichier en ecriture" 
		fichier_ouvert_ecri = open(nom_fichier_dic,"w")

	#	print "on ecrit dans le fichier dico initial"
		pickle.dump(dico_dico,fichier_ouvert_ecri) 

		fichier_ouvert_ecri.close() 

	#print "on (re)ferme le fichier ouvert en lecture"	
	fichier_ouvert_lec.close()
	
	#print "on ferme le fichier ouvert en ecriture"
	#fichier_ouvert_ecri.close()  


	actions_possibles=dico_dico[etatdis_courant]

	valeur_max=-999999999999999
	for action in actions_possibles:     # Prenant les clefs de actions_possible, par ex la clef "fonceur"
		strat_name=action          		     #LA STRATEGIE  # clef du dic eg "fonceur"
		valeur_associe=actions_possibles[action]     #LA VALEUR ASSOCIEE  # eg 0
		if valeur_associe>=valeur_max:
			nom_action_choisie=strat_name        # CHOISIR LACTION AYANT VALEUR MAX  #eg "fonceur"  
			valeur_max=valeur_associe
	#print "Au niveau prendre_act nom action max est", str(nom_action_choisie), " fin de prendre_act"
	return str(nom_action_choisie)

##############################################################################################################


def corresp(nom_act,dic_corresp):

	for clef in dic_corresp:
		#print "clef", clef
		if nom_act==clef:
			#print "Dans corresp Il choisit laction", dic_corresp[clef]
			#print "la clef serait", clef
			return dic_corresp[clef]
	
	print "action pas dans dic_corresp"
	return


##############################################################################################################
##############################################################################################################

def recompense(state, id_team, id_player):   # associe a un etat, une recompense 
	Etat=MyState(state,id_team,id_player)	

	if ((Etat.ball_pos.x==Etat.but_pos_adv.x) and (Etat.ball_pos.y>=Etat.but_pos_adv.y-GOAL_HEIGHT/2) and (Etat.ball_pos.y<=Etat.but_pos_adv.y+GOAL_HEIGHT/2)):
		r=100

	if ((Etat.ball_pos.x==Etat.but_pos.x) and (Etat.ball_pos.y>=Etat.but_pos.y-GOAL_HEIGHT/2) and (Etat.ball_pos.y<=Etat.but_pos.y+GOAL_HEIGHT/2)):
		r=-100


	if ((Etat.a_la_balle==1) or (Etat.a_la_balle==2)):
		r=5
	else:
		r=-5

	return r


##############################################################################################################

def MonteCarlo(q,scenarios,idt,idp): #scenarios est une liste de couple (etat,action)  remarque: dernier etat none
      # q est dico de dico 
      #parcurir liste a lenvers
	print "DANS MONTE CARLO"
	#print "q est ", q
	Q = q  # Travailler sur la copie de q
	#print "Copie Q est",Q
	#print"monte carlo"
	#print"ici"
	longeur=len(scenarios)     # recuperer le nombre de steps jouE dans le match? ..
	print "longeur scenarios", longeur
	i=0
	for sce in scenarios:
		
		print "SCENARIO NUMBER ", i
		#print "couple (etatbrut,actionpris) ",i," est ", sce

		#print "etat brut",sce[0]
		
		if sce[0]!=None:

			#print "entre ici"
			#print "est ce que etat est none ?"
			#print sce[0]==None
			
			R = 0
			act_choisi = sce[1]
	
			#print "action choisi", act_choisi

			for t in range (longeur-1,0,-1):
			#	print "entree boucle t succes"				
				st=scenarios[t][0]
			#	print "etat au temps", t , "est", st
			
			
				R= GAMMA*R + recompense(st,idt,idp)

			#	print "R= GAMMA*R + recompense(st,idt,idp) et donc R est maintenant", R
				etat_discretise=discretisation(st,idt,idp)
				Q[etat_discretise][act_choisi]=Q[etat_discretise][act_choisi] + ALPHA*(R-Q[etat_discretise][act_choisi])  #Que faire la maj comme ca ou bien faire return q ?

		i=i+1

 	return Q

##############################################################################################################

def maj(le_match,idt,idp,nom_fichier_dic):

	etatsbruts_allsteps=le_match.states
	joueur_stratstaken = le_match.strats 
	#print "joueur strats taken", joueur_stratstaken

	scenarios=[]


	print len(etatsbruts_allsteps)

	liste_etatsdis=[]
	
	step_num=0
	for step_brut in etatsbruts_allsteps:

		print "STEP NUM",step_num
		liste_etatsdis.append(discretisation(step_brut,idt,idp))

		required_step=joueur_stratstaken[step_num]
		#print "REquired strats", required_step
		
		required_team=required_step[idt-1]
		#print "required team", required_team
		player_action_taken= required_team[idp]
		print "ply action taken", player_action_taken
		if player_action_taken=="qstrat":
			player_action_taken=joueur_stratstaken[step_num+1][idt-1][idp] #Car il y a un ptit prob dans match.strats, il affiche la premiere strategie comme qstrat tout le tmeps
		print "new pl action taken", player_action_taken

		scenarios.append((step_brut,player_action_taken))

		step_num=step_num+1


	f_ouvert_lec= open(nom_fichier_dic,"r")

	old_dic=pickle.load(f_ouvert_lec)

	f_ouvert_lec.close()

	new_dic= MonteCarlo(old_dic,scenarios,idt,idp)

	f_ouvert_ecri= open(nom_fichier_dic,"w")

	pickle.dump(new_dic,f_ouvert_ecri)

	f_ouvert_ecri.close()
	
	print" FIN MAJ ET ECRITURE DANS FICHIER"

	return 
	
		

	

	
	
		







	
	
	

