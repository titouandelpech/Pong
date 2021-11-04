from tkinter import*
# import winsound


##### Fenêtre #####

def apparition():
    can.pack()#fait apparaître le "terrain"
    fen.geometry('900x500')
    fond.destroy()#fait disparaître le menu
    # remix=winsound.PlaySound('remix.wav',winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)#Musique lors de la partie

##### Partie commencée, en pause, ou terminée #####

def Start(event):
    global partie,x,y,X,Y,sb,sbb,V,score
    if sb >= score :# Score max à atteindre
        partie,V='terminée',1
        can.coords(balle,950,550,950,550)
        Vainqueur.configure(text="Player " + str(V) + " wins")
        Vainqueur.place(x=250,y=225)
    elif sbb >= score :#                    Arrêt de la partie si score atteint
        partie,V='terminée',2
        can.coords(balle,950,550,950,550)
        Vainqueur.configure(text="Player " + str(V) + " wins")
        Vainqueur.place(x=250,y=225)
    if partie != 'lancée' and partie != 'terminée':
        if partie == 'pointbarre':
            X=1
        if partie == 'pointbabarre':
            X=0
        partie='lancée'
        anime()
        
##### Nombre de points #####

def cinqp():
    global score
    score=5
    apparition()
    
def dixp():
    global score
    score=10
    apparition()

def quinzep():
    global score
    score=15
    apparition()

##### Barres #####

def Mouv(event):
    key=event.keysym #Permet de prendre le "nom/valeur" de la touche préssée
    global xb,xbb,yb,ybb,vitessebarre
    if key=="z" and yb-50>0:
        yb=yb-20
    if key=="s" and yb+50<500:
        yb=yb+20
    if key=="Up" and ybb-50>0:
        ybb=ybb-20
    if key=="Down" and ybb+50<500:
        ybb=ybb+20
    can.coords(barre,xb-4,yb-50,xb+4,yb+50)
    can.coords(babarre,xbb-4,ybb-50,xbb+4,ybb+50)

##### Repositionnement Balle #####

def DroiteBas():
   global x,y,Y,X,xbb,ybb,angle
   x,y=x+3,y+angle
   if x in (xbb-5,xbb):
       if y in range(ybb-50,ybb-16): #partie haute de la barre
         x,y=x-3,y-angle
         if angle>1:
             angle=angle-1
         X=1
         Y=0
       if y in range(ybb-15,ybb+15): #partie centrale de la barre
         x,y=x-3,y-angle
         X=1
         Y=0
       if y in range(ybb+16,ybb+50): #partie basse de la barre
         x,y=x-3,y-angle
         if angle<10:
             angle=angle+1
         X=1
         Y=0
   elif y>=490:
      x,y=x-3,y-3
      Y=1
      X=0
   can.coords(balle,x-7,y-7,x+7,y+7)

def DroiteHaut():
   global x,y,Y,X,xbb,ybb,angle
   x,y=x+3,y-angle
   if x in (xbb-5,xbb):
       if y in range(ybb-50,ybb-16):
           x,y=x-3,y+angle
           if angle<10:
               angle=angle+1
           X=1
           Y=1
       if y in range(ybb-15,ybb+15):
           x,y=x-3,y+angle
           X=1
           Y=1
       if y in range(ybb+16,ybb+50):
           x,y=x-3,y+angle
           if angle>1:
               angle=angle-1
           X=1
           Y=1
   elif y<=10:
      x,y=x-3,y+angle
      Y=0
      X=0
   can.coords(balle,x-7,y-7,x+7,y+7) 

def GaucheBas():
   global x,y,Y,X,xb,yb,angle
   x,y=x-3,y+angle
   if x in (xb,xb+5):
       if y in range(yb-50,yb-16):
           x,y=x+3,y-angle
           if angle>1:
               angle=angle-1
           X=0
           Y=0
       if y in range(yb-15,yb+15):
           x,y=x+3,y-angle
           X=0
           Y=0
       if y in range(yb+16,yb+50):
           x,y=x+3,y-angle
           if angle<10:
               angle=angle+1
           X=0
           Y=0
   elif y>=490:
      x,y=x+3,y-angle
      Y=1
      X=1
   can.coords(balle,x-7,y-7,x+7,y+7)

def GaucheHaut():
   global x,y,Y,X,xb,yb,angle
   x,y=x-3,y-angle
   if x in (xb,xb+5):
       if y in range(yb-50,yb-16):
           x,y=x+3,y+angle
           if angle<10:
               angle=angle+1
           X=0
           Y=1
       if y in range(yb-15,yb+15):
           x,y=x+3,y+angle
           X=0
           Y=1
       if y in range(yb+16,yb+50):
           x,y=x+3,y+angle
           if angle>1:
               angle=angle-1
           X=0
           Y=1
   elif y<=10:
      x,y=x+3,y+angle
      X=1
      Y=0
   can.coords(balle,x-7,y-7,x+7,y+7)

##### Animation Balle + Rebonds #####

def anime():
   global X,Y,x,y,partie,sb,sbb,xb,yb,xbb,ybb
   if x<=0:# la balle atteint la limite gauche de l'écran
       partie='pointbabarre'
       sbb=sbb+1# point au joueur 2 (barre Droite)
       scorebabarre.config(text=str(sbb))
       x,y=450,250
       xb,yb,xbb,ybb=45,250,855,250
       can.coords(balle,x-7,y-7,x+7,y+7)# repositionnement de la balle,...
       can.coords(barre,xb-4,yb-50,xb+4,yb+50)#...des barres 1...
       can.coords(babarre,xbb-4,ybb-50,xbb+4,ybb+50)#...et 2, après avoir marqué
   if x>=900:# la balle atteint la limite droite de l'écran
       partie='pointbarre'
       sb=sb+1# point au joueur 1 (barre Gauche)
       scorebarre.config(text=str(sb))
       x,y=450,250
       xb,yb,xbb,ybb=45,250,855,250
       can.coords(balle,x-7,y-7,x+7,y+7)
       can.coords(barre,xb-4,yb-50,xb+4,yb+50)
       can.coords(babarre,xbb-4,ybb-50,xbb+4,ybb+50)
   if X==0:## directions de la balle
      if Y==0:
         DroiteBas()
      elif Y==1:
         DroiteHaut()
   elif X==1:
      if Y==0:
         GaucheBas()
      elif Y==1:
         GaucheHaut()
   if partie=='lancée':
        fen.after(10,anime)

########## PROGRAMME PRINCIPAL ##########

fen=Tk()
fen.title('P.O.N.G')
fen.geometry('390x390')
fond=Canvas(fen, bg='black', height=500, width=900)
fond.pack()

Titre=Label(fond,text='PONG',fg='white',bg='black',font=("OCR A Extended",70))
Titre.place(x=80,y=20)

#Boutons des "modes de jeu"
pikachu=Button(fond,text='5 points',command=cinqp)
pikachu.place(x=175,y=180)
dracaufeu=Button(fond,text='10 points',command=dixp)
dracaufeu.place(x=172,y=220)
mew=Button(fond,text='15 points',command=quinzep)
mew.place(x=172,y=260)

can=Canvas(fen, bg='black', height=500, width=900)#"Terrain" de la partie
can.create_line(450,0,450,505,width=2,fill='white')

x,y,X,Y=447,250,0,0
sb,sbb=0,0
xb,yb=45,250
xbb,ybb=855,250
angle=3
partie='paslancée'
V=0# Joueur gagnant, soit '1' ou '2'
score=0# Score à atteindre pour gagner

scorebarre=Label(can,text=str(sb),fg='white',bg='black',font=("OCR A Extended",20))#Affichage des scores
scorebabarre=Label(can,text=str(sbb),fg='white',bg='black',font=("OCR A Extended",20))# " "
scorebarre.place(x=395,y=20)
scorebabarre.place(x=485,y=20)
Vainqueur=Label(fen,text="Player " + str(V) + " wins",fg='white',bg='black',font=("OCR A Extended",40))# Message joueur gagnant
Vainqueur.place_forget()# Message non affiché

barre=can.create_rectangle(xb-4,yb-50,xb+4,yb+50,fill='white')
babarre=can.create_rectangle(xbb-4,ybb-50,xbb+4,ybb+50,fill='white')
balle=can.create_oval(x-7,y-7,x+7,y+7,fill='white')

# menu=winsound.PlaySound('menu.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)#Musique du menu

fen.bind("<Return>",Start)
fen.bind("<Key>",Mouv)

fen.mainloop()
