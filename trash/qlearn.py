from soccersimulator import *
from Outils import*
from Strategies import*
import pickle

GAMMA  =0.6
ALPHA  =0.9
 
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
		
		dict_a["rien"]=0    # on met ici des string("rien")et apres on fera la correspondance string vers strat
		dict_a["fonceur"]=0
		dict_a["gardien"]=0
		
		
		dic_s[s]=dict_a    # dic_s= { (0,0): {"rien": 0, "fonceur":0} , (0,1) : {"rien": 0, "fonceur":0} }
	
	return dic_s


def MonteCarlo(q,scenarios,idt,idp): #scenarios est une liste de couple (etat,action)  remarque: dernier etat none
      # q est dico de dico 
      #parcurir liste a lenvers
	print "DANS MONTE CARLO"
	print "q est ", q
	Q = q  # Travailler sur la copie de q
	print "Copie Q est",Q
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

			print "entre ici"
			print "est ce que etat est none ?"
			print sce[0]==None
			
			R = 0
			act_choisi = sce[1]
	
			print "action choisi", act_choisi

			for t in range (longeur-1,0,-1):
				print "entree boucle t succes"				
				st=scenarios[t][0]
				print "etat au temps", t , "est", st
			
			
				R= GAMMA*R + recompense(st,idt,idp)

				print "R= GAMMA*R + recompense(st,idt,idp) et donc R est maintenant", R
				etat_discretise=discretisation(st,idt,idp)
				Q[etat_discretise][act_choisi]=Q[etat_discretise][act_choisi] + ALPHA*(R-Q[etat_discretise][act_choisi])  #Que faire la maj comme ca ou bien faire return q ?
		i=i+1

 	return Q


		
def prendreaction_et_maj(le_match,idt,idp,fichier_dic):      
	#print "on passe ici"
	observations_allsteps=le_match.states  # De la forme [ state_stp1, state_stp2, ..state_stpn ]
	print "Nombre de steps dans ce match.. observations allsteps:"
	print len(observations_allsteps)
	#print "on passe ici2"
	liste_etatsdis=[]
	for step in observations_allsteps:
		liste_etatsdis.append(discretisation(step,idt,idp))

	print "liste_etatsdis"
	print liste_etatsdis

	print "longueur liste_etatsdis"
	print len(liste_etatsdis)
	

	#SI LE DICTIONNAIRE EST VIDE, AU DEBUT, TOUT INITALISER A ZERO  (ou random??)
	#print "on ouvre le fichier en lecture"
	fichier_ouvert_lec= open(fichier_dic,"r")
	#print "on stocke dans dico ce fichier"
	dico_dico= pickle.load(fichier_ouvert_lec)                                   #PROBLEME SI FICHIER EST FICHIER NORMAL VIDE, .. donc deja ecrire un dico vide dans le fichier initial
	if dico_dico=={}:
	#	print "dico en effet vide"
	#	print "on ferme ce fichier"
		fichier_ouvert_lec.close()
	#	print "on rentre dans initialisation"
		dico_dico=initialisation_q(liste_etatsdis)
	#	print " on ouvre le fichier en ecriture" 
		fichier_ouvert_ecri = open(fichier_dic,"w")

	#	print "on ecrit dans le fichier dico initial"
		pickle.dump(dico_dico,fichier_ouvert_ecri) 

	#print "on (re)ferme le fichier ouvert en lecture"	
	fichier_ouvert_lec.close()
	
	#print "on ferme le fichier ouvert en ecriture"
	fichier_ouvert_ecri.close()  

	
	scenarios=[]
	
	joueur_strattaken = le_match.strats       
	# De la forme [ (('team1_pl1_stp1','team1_pl2_stp1'), ('team2_pl1_stp1','team2_pl2_stp1')), (('team1_pl1_stp2','team1_pl2_stp2'), ('team2_pl1_stp2','team2_pl2_stp2')) ...]



	for step_obs in observations_allsteps:      # observation pour un step du match  De la forme state_stpi
		#print "ici"
		
		step_discretise=discretisation(step_obs,idt,idp)  # Discretiser l'observation a ce step   # De la forme (0,1)
		#print "et la"
		#CHOISIR ACTION A PRENDRE
		actions_possibles=dico_dico[step_discretise]      #LES ACTIONS POSSIBLES(AVEC LEUR VALEUR AFFECTEE) CORRESPONDANT A LETAT COURANT  # Pour la clef (0,1) on aura {"fonceur":0, "rien":0}
	
		valeur_max=-999999999999999
		for action in actions_possibles:		     # Prenant les clefs de actions_possible, par ex la clef "fonceur"
			strat_name=action          		     #LA STRATEGIE  # clef du dic eg "fonceur")
			valeur_associe=actions_possibles[action]     #LA VALEUR ASSOCIEE  # eg 0
			if valeur_associe>=valeur_max:
				nom_action_choisie=strat_name        # CHOISIR LACTION AYANT VALEUR MAX  #eg "fonceur"  
				valeur_max=valeur_associe
		#		print "action",nom_action_choisie
		#print "a la sortie action max", nom_action_choisie



	        # LA MISE A JOUR 
		for eachstep in joueur_strattaken:		# De la forme (('team1_pl1_stp1','team1_pl2_stp1'), ('team2_pl1_stp1','team2_pl2_stp1'))
			#print "ici"	
			required_team=eachstep[idt]              #RECUPERER LES STRATS PRIS PAR LEQUIPE CONCERNEE    # ('team1_pl1_stp1','team1_pl2_stp1')
			#print "la"
			player_actiontaken= required_team[idp]	  #RECUPERER L'ACTION PRIS PAR LE JOUEUR CONCERNE    # 'team1_pl1_stp1'
			#print "and fucking here"
			
		scenarios.append((step_obs,player_actiontaken))    #on ajoute couple (etatbrut,actionpris) a la liste scenarios
		#print "got here"


	print "scenarios longueur ?"
	print len(scenarios)

	print "faisons maj de dico dico"
	dico_dico=MonteCarlo(dico_dico,scenarios,idt,idp)               #Cette fonction met a jour le dico de dico .. eg dico_dico sera desormais { (0,0): {"rien": 0, "fonceur":5} , (0,1) : {"rien": 3, "fonceur":0} }
	print "Monte carlo fini"
	
	print" on ouvre le fichier en ecriture"
	fichier_reouvert_ecri = open(fichier_dic,"w")
	print "on ecir dic maj dans fichier"
	pickle.dump(dico_dico,fichier_reouvert_ecri)     # On ecrir dans le fichier_dic cette nouvelle dico mise a jour

	print "on ferme fichier"
	fichier_reouvert_ecri.close()
	print "fichier fermE"
	print "laction choisie", nom_action_choisie
	return nom_action_choisie      # eg "fonceur"


def QStrategy(match,idt,idp,fichier_dic,dic_corresp):
	nom_action= prendreaction_et_maj(match,idt,idp,fichier_dic)

	for clef in dic_corresp:
		print "clef", clef
		if clef==nom_action:
			print "Il choisit laction", dic_corresp[clef]
			return dic_corresp[clef]
		#else:
		#	print "action pas dans dic_corresp.."
		#	return

	print "action pas dans dic_corresp"
	return






		

# C ici la ligne 4 du slide 
	
	"""liste=fichier_match.soccermatch.load 
 	

	for etape in liste:

		etat_discret=discretisation(state)

		DIC_S=fonction_q(etat_discret)"""

	
	
	
		







	
	
	
