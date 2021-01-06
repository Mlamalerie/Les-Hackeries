import os
import time
from shutil import copyfile


	
username = os.getlogin()

listesFichiersPy = [fic for fic in os.listdir(os.getcwd()) if fic[0:4] == "main" ]
print(listesFichiersPy)
def py_to_pyw_start():
	global listesFichiersPy
	nomEmplacementSauvegarde = ".pyw files"
	if not os.path.exists(nomEmplacementSauvegarde):
		os.makedirs(nomEmplacementSauvegarde)
	for ficpy in listesFichiersPy:
		
		namew = ficpy.split('.')[-2] + ".pyw"
		destination = nomEmplacementSauvegarde + "/" + namew
		
		try:
			copyfile(ficpy,destination) #envoyer vers 
		except:
			print(f" erreur copie {namew}")
		#else:
		#	copyfile(destination,f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{namew}") #envoyer vers demmarrage
		#	print(f" * copy {namew} in startUp")



def TRY_PYW(n,att):
    if n > 0:
        try:
           py_to_pyw_start()
        except:
            print(" ----------------------------------------! ERREUR de pytopyw()")
            time.sleep(att)
            TRY_PYW(n-1,att)  

TRY_PYW(2,1)
## commande pour envoyer le bail dans demmarrage
