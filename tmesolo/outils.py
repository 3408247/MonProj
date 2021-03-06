# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:38:24 2016

@author: 3408247
"""
import math
import soccersimulator
from soccersimulator.settings import  *
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
from random import uniform
from copy import deepcopy
DCERCLE_RAYON = GAME_GOAL_HEIGHT/2

def miroir_pos(p):
    return Vector2D(GAME_WIDTH-p.x,p.y)

def miroir_vect(v):
    return Vector2D(-v.x,v.y)

def miroir_action(act):
    return SoccerAction(miroir_vect(act.acceleration),miroir_vect(act.shoot))

def miroir_state(etat):
    etatcpy=etat.copy()

    etatcpy.ball.position=miroir_pos(etat.ball.position)
    etatcpy.ball.vitesse=miroir_vect(etat.ball.vitesse)

    for(idt,idp) in etat.players:
	etatcpy.player(idt,idp).position=miroir_pos(etat.player(idt,idp).position)
	etatcpy.player(idt,idp).vitesse=miroir_vect(etat.player(idt,idp).vitesse)
    
    return etatcpy

def dist(u,v): #"u->Vector2D, v->Vector2D" #retourne float->la distance entre u et v
	return u.distance(v)

def qq_entre(src,dest,obs): #src->Vector2D(pos) dest->Vector2D(pos) obs->Vector2D(pos)
	vsrc_dest=dest-src
	vsrc_obs=obs-src
	return ((abs(vsrc_dest.angle-vsrc_obs.angle)<0.2 ) and (dist(src,obs)< dist(src,dest)))


class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state    #ajouter le miroir ici option 1
        self.key = (idteam,idplayer)
 
        if (idteam!=1):
	    self.state=miroir_state(self.state)


    @property
    def player_moi(self):
	return self.state.player(self.key[0],self.key[1])

    @property
    def balle(self):
	return self.state.ball


    ### POSITIONS ###

    @property
    def my_pos(self): #retourne Vector2D->la position de self (ici joueur)
        return self.state.player_state(self.key[0],self.key[1]).position
        #equivalent a self.state.player_state(self.key[0],self.key[1])
    
    @property    
    def ball_pos(self): #retoune Vector2D->la position de self (ici ball)
        return self.state.ball.position

    @property
    def but_pos(self): #retourne Vector2D->la position_milieu du but 
	
		return Vector2D(x=1,y=GAME_HEIGHT/2)


    @property   
    def but_pos_adv(self): #retourne Vector2D->la position_milieu du but de l'adversaire

		return Vector2D(x=GAME_WIDTH,y=GAME_HEIGHT/2)

    @property  
    def centre(self):
		return Vector2D(x=GAME_WIDTH/2,y=GAME_HEIGHT/2)


    ### DISTANCES ###

    
    def dist_player_ball(self,player): #distance entre player et ball
	return dist(player.position,self.ball_pos)

   
 
	
    ### ANGLES ###
    def angle_player_point(self,pos_point):
	vecteur=pos_point-self.my_pos
	return vecteur.angle


    ### MOUVEMENTS ###

    def aller(self,p): #"self->vector2D, p->vector2D" #retourne SoccerAction->faire bouger self jusqu'a p ; pas de shoot
        return SoccerAction(p-self.my_pos,Vector2D())

    def aller_avec_angle_norme(self,theta,norme):
	dep=Vector2D(angle=theta,norm=norme)
	return SoccerAction(dep,Vector2D())

    def courir_vers(self,p):
    	v=p-self.my_pos
	v.norm=1000

	return self.aller(p)
 
    @property
    def courir_vers_ball(self):
	ball = deepcopy(self.state.ball)
	for i in range(0,5): 
		ball.next(Vector2D())            # Pour avoir la balle/prevoir la balle apres 5 tours 

	vect_mouv=ball.position-self.my_pos

	vect_mouv.norm=1000

	if dist(self.my_pos,self.ball_pos)<3:       # Quand je m'approche de la balle
		vect_mouv.norm=0.5		    # Je diminue ma vitesse

	return SoccerAction(vect_mouv,Vector2D())

    @property 
    def courir_vers_ball2(self):          # Utiliser ce courir ver ball dans dribbler
	ball = deepcopy(self.state.ball)
	for i in range(0,3):
		ball.next(Vector2D())
	return self.courir_vers(ball.position)

    

    ### RADAR ###

    @property
    def adv_plus_proche(self):
	d_min=999
	liste_adv=[(it, ip) for (it, ip) in self.state.players if (it!=self.key[0])] 

	for p in liste_adv:
	
		pl=self.state.player(p[0],p[1])
		d=self.dist_player_ball(pl)
		if d<d_min:
	           d_min=d
		   lui=pl
	
	return lui

    @property
    def pos_adv_plus_proche(self):
	
	return self.adv_plus_proche.position



    @property
    def vit_adv_plus_proche(self):
	return self.adv_plus_proche.vitesse


    @property
    def equi_plus_proche(self):
	d_min=999
	liste_equipiers=[(it, ip) for (it, ip) in self.state.players if (it ==self.key[0] and ip!=self.key[1])] 
	for p in liste_equipiers:
		pl=self.state.player(p[0],p[1])
		d=self.dist_player_ball(pl)
		if d<d_min:
	           d_min=d
		   lui=pl

	return lui

    @property
    def pos_equi_plus_proche(self):
	
	return self.equi_plus_proche.position



    def pos_equi_pr_ball(self):
	d_min=999
	liste_equi=[(it, ip) for (it, ip) in self.state.players if (it ==self.key[0] and ip!=self.key[1])]  

	for p in liste_equi:
	
		pl=self.state.player(p[0],p[1])
		d=dist(pl.position,self.ball_pos)
		if d<d_min:
			d_min=d
			lui=pl.position

	return lui




    def qui_entre(self,src,dest):
	liste_adv=[(it, ip) for (it, ip) in self.state.players if (it!=self.key[0])]
	for p in liste_adv:
		obstacle=self.state.player(p[0],p[1])

		#Si l'obstacle(l'adversaire) se trouve entre ma balle et but_adv
		if qq_entre(src,dest,obstacle.position):

			return obstacle
		else:
			return False
		
			

    ### SHOOTS ###

    @property 
    def test_peut_shooter(self):
	return ((dist(self.my_pos,self.ball_pos))<BALL_RADIUS+PLAYER_RADIUS)

    def test_peut_tirer(self):   # Contrainte de l'equipe 1
	return (self.player_moi.vitesse>0.01)


    def shoot_vers(self,p): #pas de mouvement; faire shooter dans la direction p - self
        return SoccerAction(Vector2D(),p-self.my_pos)

    def shoot_vers_norm(self,p,n):
	v=p-self.my_pos
	v.norm=n

	return SoccerAction(Vector2D(),v)

  

    @property 
    def shoot_vers_equi_proche(self):
	if self.test_peut_shooter:
		return self.shoot_vers(self.pos_equi_plus_proche)
	else:
		return self.courir_vers_ball

	

    def est_devant(self,moi,lui):
	return lui.position.x>moi.position.x


    def est_enhaut(self,moi,lui):
	return lui.position.y>moi.position.y

   	

    def shoot_dribble_vers(self,p):  # OPTIMISER DRIBBLE A CE QU'IL EVITE ADVERSAIRE 
	
	s=p-self.ball_pos
	s.norm=0.5

	adv=self.adv_plus_proche
	moi= self.player_moi


	if dist(self.ball_pos,self.pos_adv_plus_proche)<12:
	
	  	if self.est_devant(moi,adv):         #Si adv est devant moi
		
			if adv.vitesse.dot(moi.vitesse)<=0:  #Si nos vitesses ont direction opposées; il s'approche vers ball
				
				
				if self.est_enhaut(moi,adv):	   # Il vient d'en haut donc moi je shoot un peu vers le bas
									
					s.angle=s.angle-0.5     # Je shoote un peu vers le bas
				else:
					
					s.angle=s.angle+0.5 # Il vient d'en bas donc moi je shoote un peu vers le haut

			#S'il s'eloigne on s'en fou

		else: #il est derriere moi

			if adv.vitesse.dot(moi.vitesse)>0: # On a les meme directions de vitesse; il s'approche de derriere
			
				s.norm=s.norm+0.1    # shooter un peu plus fort pour l'esquiver # shooter un peu plus fort pour l'esquiver 

	return SoccerAction(Vector2D(),s)
	
	
 
    def dribbler_vers(self,p):   
	if self.test_peut_shooter:

		return self.shoot_dribble_vers(p)
	else:
		return self.courir_vers_ball

    @property
    def shoot_degager(self):
	
	#Trouver un pt ou il n'y a personne entre	
	for y_ in range (0,GAME_HEIGHT):
		pt=Vector2D(x=GAME_WIDTH/2,y=y_)
		if self.qui_entre(self.ball_pos,pt)==False:
			return self.shoot_vers_norm(pt,6)
	
	#Si un tel pt n'est pas trouvE, shooter nord ou sud
	pt_nord=Vector2D(x=(self.ball_pos.x)+10,y=GAME_HEIGHT)
	pt_sud=Vector2D(x=(self.ball_pos.x)+10,y=0)
	if dist(self.ball_pos,pt_nord)<dist(self.ball_pos,pt_sud):
		return self.shoot_vers_norm(pt_nord,6)	
	else:
		return self.shoot_vers_norm(pt_sud,6)
	

    @property
    def degager(self):
	if self.test_peut_shooter:
		return self.shoot_degager
	else:
		return self.courir_vers_ball

    @property
    def degager_centre(self):
	if self.test_peut_shooter:
		return self.shoot_vers_norm(self.centre,6)
	else:
		return self.courir_vers_ball


    @property
    def shoot_piquer(self):
	 moi= self.player_moi
	 balle=self.balle

	 if self.est_enhaut(balle,moi):
	 		cible=self.ball_pos+ Vector2D(x=0,y=2);
	 else:
	 		cible=self.ball_pos- Vector2D(x=0,y=2);
		
	 return self.shoot_vers_norm(cible,0.5)

    @property
    def piquer_balle(self): #Intercepter balle/la piquer
	 if self.test_peut_shooter:
			return self.shoot_piquer
	
	 else:
	 	return self.courir_vers_ball
	


    ### QUI A LA BALLE ###

    @property
    def a_la_balle(self):

	#ADV ou ADV et MOI
	liste_adv=[(it, ip) for (it, ip) in self.state.players if (it!=self.key[0])]

	for p in liste_adv:
		if dist(self.ball_pos, self.state.player(p[0],p[1]).position)<BALL_RADIUS+PLAYER_RADIUS:
			return 3

	# J'AI LA BALLE, QUE MOI 
	if self.test_peut_shooter==True: 
		return 1

	# MON EQUIPE A LA BALLE
	liste_eq=[(it, ip) for (it, ip) in self.state.players if (it==self.key[0])]

	for q in liste_eq:
		if dist(self.ball_pos, self.state.player(q[0],q[1]).position)<BALL_RADIUS+PLAYER_RADIUS:
			return 2    

		else: # PERSONNE
			return 0
    
