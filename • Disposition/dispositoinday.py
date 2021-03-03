
######################
with open("dispo.txt",'r') as fic:
	x = fic.read().split('&')
	dispo = x[0].strip()
	tasks = x[1].strip()


##########################
def nbheuresdispo(text):
	l = text.split(';')
	s = 0
	for ho in l:
		xx = ho.split('-')
		a = int(xx[0])
		b = int(xx[1])
		#print(a,b)
		if(b < a) and (a < 24 and b >= 0):
			b += 24
		s += (b-a)
	return s;
		
HEUREDISPO = nbheuresdispo(dispo)
print("HEURES : {}".format(HEUREDISPO))

def saisirmatiere(heuredispo,tasks):
	ll = tasks.split(',')
	n = len(ll)
	l = [ [ll[i].strip(),1/n,((1/n)*heuredispo)] for i in range(n)]
	l = [x for x in l if len(x)>1]
	return l

listes = saisirmatiere(HEUREDISPO,tasks)
#listes = [["BDD",0.75],["Compta",0.1],["Projet Voltaire",0.15]]
def afficherhorloge(nb):
	minutes = nb*60
	
	minutesrestantes = int(minutes%60)
	
	
	heure = int(minutes//60)
	print(minutes,minutesrestantes,minutesrestantes//30)
	if minutesrestantes//30 > 0:
		minutesrestantes = 30
	else:
		minutesrestantes = 0
	
	text = ""
	if heure > 0:
		text += str(heure) +"h "
	if minutesrestantes > 0:
		text += str(minutesrestantes)
		
	return text

def affiche(l,HEUREDISPO):
	print(" ------")
	i = 0
	for matiere in l:
		print("   {}) {} : {}".format(i,matiere[0],afficherhorloge(matiere[2])))
		i += 1
	print(" ------")




def augm(l,choix,pourcentage):
	c = choix[-1]
	
	n = len(l)
	diminpourcentage = (pourcentage/(n-1))
	
	if choix[0] == '-':
		c = int(choix[1])
		pourcentage *= -1
		diminpourcentage *= -1
	else:
		c = int(choix[0])
	
	
	i = 0
	
	for mat in l:
		
		if i == c:
			
			mat[2] = mat[2]*(1+pourcentage)
		else:
		
			mat[2] = mat[2]*(1-diminpourcentage)
			
		i+= 1
	return l		
		

def majmaj(listes):
	text = " ### Augmenter quel bail ? \n"
	choix = input(" > ")
	if choix == "wq":
		return True
		
	listes = augm(listes,choix,0.25)
	print(listes)
	return False
	
ok = False

while not ok:
	affiche(listes,HEUREDISPO)
	ok = majmaj(listes)
	


'''
listmatiere ]


'''
