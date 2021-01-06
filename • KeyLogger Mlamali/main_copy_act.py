import os
import time
import datetime
from shutil import copyfile
dateajd = datetime.datetime.now().strftime('%Y-%m-%d')
username = os.getlogin()

from others.variables_param import NOM_DOSSIER_SECRET

nomEmplacementBase = NOM_DOSSIER_SECRET
nomEmplacementSauvegarde = nomEmplacementBase
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

nomEmplacementSauvegarde += "/" + datetime.datetime.now().strftime('%Y-%m-%d') #dossier à la date de aujourd'hui
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)
nomfile = username + " touch " + dateajd + ".txt"

nomEmplacementSauvegarde += "/act"  
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)


time.sleep(30)
while 1:
	
	ancien = nomEmplacementBase + "/" + dateajd + "/" + nomfile
	nouveau = nomEmplacementSauvegarde+ "/" +nomfile
	if os.path.isfile(ancien):
		print("copy")
		copyfile(ancien,nouveau)
		
		time.sleep(60)
		
			
	else:
		print("no file txt")
		break;
	
