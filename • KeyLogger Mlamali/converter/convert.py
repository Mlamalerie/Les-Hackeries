
import os


nomEmplacementSauvegarde = "result"
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)
	

def change(text):
	ligne = text.split("\n")
	tout = [lig.split(" ")[-1] for lig in ligne]
	heures = [lig.split(" ")[0] for lig in ligne]
	res = ""
	i = 0
	for c,h in zip(tout,heures):
		
		
		if len(tout[i]) == 3 and len(tout[i-1]) == 3 and i > 0:
			res += c[1:-1]
		
		elif 3 <= len(c) <= 5 :
				
			res += "\n" + c[1:-1]
		elif len(c) > 1:
			#if c[1:-1].isnumeric():
			#	c = chr(int(c[1:-1]))
			res += "\n " + h[:-3]
			res += " # " + c
		i+=1
	
	return res

nomEmplacementDonnees = "fichiersLog"
listesData = os.listdir(nomEmplacementDonnees)
for nomfic in listesData:
	with open(nomEmplacementDonnees+ "/" + nomfic,'r') as fic:
		text = fic.read()
		textres = change(text)
		with open(nomEmplacementSauvegarde + "/" + nomfic,'w') as ficres:
			ficres.write(textres)
