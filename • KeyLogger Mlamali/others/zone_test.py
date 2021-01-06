import os
s = 0
def parcours(f):
	global s
	if os.path.exists(f):
		if os.path.isdir(f):
			print(" * dir ~",f)
			for elem in os.listdir(f):
				ef = f + "/" + elem
				if os.path.isdir(ef):
					print("dir ~",ef)
					parcours(ef)
					#s += 1
				elif os.path.isfile(ef):
					print("fil ~",ef)
					s+= 1
				else:
					print('*')
		


f = "C:/W"

import zipfile

nomduZip = "C:/W/zippass.zip"

if not os.path.exists(nomduZip):
	mode = "w"
else:
	mode = "a"
		
with zipfile.ZipFile(nomduZip,mode) as my_zip:
	my_zip.write("C:/W/test0.txt")
	my_zip.setpassword(b"1234")

