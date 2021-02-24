# -*- coding: utf-8 -*-
"""
Created on Feb 2021

Github: https://www.github.com/Mlamalerie

"""


import os
import time
import winsound

def play(fil):
    return winsound.PlaySound(fil, SND_FILENAME)

format_low = 0
format_medium = 0
format_low = 0
#en fonction de la longueur du son alongé le temps d'attente

def select_files(orig,i = 0,prof=1,select_dic = {}):
    espace = "  | "*prof
    listefichiers = os.listdir(orig)
    audioext = ['.mp3','.wav','.ogg']
    
    for fil in listefichiers:
        fil = orig + "\\" + fil
        if os.path.isdir(fil):
            print(espace,"***",orig.split("\\")[-1], prof)
            i = select_files(fil,i,prof+1,select_dic)    
        else:
            print( espace," :",fil.split("\\")[-1])
            
            bay, ext = os.path.splitext(fil)
            if ext in audioext:
                wait = 0
                long = 1
                if long == format_low:
                    wait = 0
                
                time.sleep(wait)
                play(fil)
            select_dic[i] = fil
            i+=1
          
   
    return i

dossier = "G:\Mon Drive\Zone de Code Python\• Mes logiciels Hack\• Lecteur DrumKit"
while 1:
    print(dossier)
    a = select_files(dossier)
    print(a)
    time.sleep(3)




