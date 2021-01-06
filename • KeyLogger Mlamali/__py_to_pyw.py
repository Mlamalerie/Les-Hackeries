import os
from shutil import copyfile


	
username = os.getlogin()

listesFichiersPy = [fic for fic in os.listdir(os.getcwd()) if fic[0:4] == "main" ]
print(listesFichiersPy)
def py_pyw():
	global listesFichiersPy
	nomEmplacementSauvegarde = ".pyw files"
	if not os.path.exists(nomEmplacementSauvegarde):
		os.makedirs(nomEmplacementSauvegarde)
	for ficpy in listesFichiersPy:
		
		namew = ficpy.split('.')[-2] + ".pyw"
		destination = nomEmplacementSauvegarde + "/" + namew
		
		copyfile(ficpy,destination) 
		copyfile(destination,f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{namew}") #envoyer vers demmarrage
		print(f" * copy {namew} in startUp")


try:
	py_pyw()
	print(" ----------------------------------------> Yes py_pyw")
except:
	print(" ----------------------------------------! ERREUR de py_pyw")	
staller = input("Press ENTER to close")
## commande pour envoyer le bail dans demmarrage
