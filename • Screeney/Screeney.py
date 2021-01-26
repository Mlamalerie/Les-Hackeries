import pyautogui
import time
import datetime
import os
import filecmp

from tkinter import *
from functools import partial
from tkinter import ttk

def SemblableFichier(fic,fic2):
	
	
	
	a = os.path.getsize(fic)
	b = os.path.getsize(fic2)
	diff = abs(a - b)
	if (diff > 3000):
		return (False,diff)
	else:
		return (True,diff)
	
def SupprimerFichier(path):
	if os.path.exists(path):
		os.remove(path)
	else:
		print("Impossible de supprimer le fichier " + path +" car il n'existe pas")
		
		
window = Tk()
window.title("SCREENEY")
window.iconphoto(False, PhotoImage(file='ico/icon.png'))
window.attributes('-topmost', 1)
window.geometry('320x210')

 #lbl = Label(window, text="Hello")
#lbl.grid(column=0, row=0)
labelChoix = Label(window, text = "Matières :")
labelChoix.pack()
listeMatieres=["Selectionner","AlgoProc","DataMining","BDD","EOE", "PPP","Compta" ]
listeMatieres.sort()
listeCombo = ttk.Combobox(window,values=listeMatieres,state="readonly",justify='center',width=15)
listeCombo.current(len(listeMatieres)-1)
listeCombo.pack()

c = 0
ancienphoto = ""

def capturer():
	global c,ancienphoto
	nomMatiere = listeCombo.get()
	nomEmplacementSauvegarde = "SCREENEY - " + nomMatiere
	if not os.path.exists(nomEmplacementSauvegarde):
		os.makedirs(nomEmplacementSauvegarde)

	nomEmplacementSauvegarde += "/" + datetime.datetime.now().strftime('%Y-%m-%d')
	if not os.path.exists(nomEmplacementSauvegarde):
		os.makedirs(nomEmplacementSauvegarde)
	
	semblable = False
	comm = Comment.get()
	comm = comm.strip()
	if len(comm) > 0:
		comm = ' ' + comm
	
	myDatetime = datetime.datetime.now()
	nomFichier= myDatetime.strftime('%Y-%m-%d-%H%M%S'+ comm )
	photo = nomEmplacementSauvegarde + "/" + nomFichier + ".png"
	
	# prendre photo	
	pyautogui.screenshot(photo)
	print("#" + str(c) + "# " + photo)
	
	# pour les photo sauf la premiere
	if (c > 0):	
		# si photo semblable a lancienne photo alors suprr photo
		semblable = SemblableFichier(photo,ancienphoto)
		if semblable[0]:
			print(">>> PAREIL! "+str(semblable[1]) + " # " +photo+" VS "+ancienphoto)
			label.config(text="Image similaire ! Je cala pas",fg='red')
			SupprimerFichier(photo)
		#sinon, si nouvelle photo
		else:
			c+= 1
			label.config(text="#"+str(c) + " ▪ "+ photo.split('/')[-1],fg='green')
			ancienphoto = photo
			
	else:
		c+=1
		label.config(text="#"+str(c) + " ▪ "+ photo.split('/')[-1],fg='green')
		ancienphoto = photo
		
	
	time.sleep(1)
	

def clicked():
	global value;
	capturer()
	

btn = Button(window, text="Screen 📸", command=clicked,width=17,
                           height=2)
btn.pack(padx=5, pady=10)

Comment = Entry(window, bd =3)
Comment.pack()


label = Label(window, text = "")
label.pack()



cred = Label(window, text = "Code by Mlamali Said Salimo.",font=("inherit", 8))
cred.pack(side='bottom')
window.mainloop()

