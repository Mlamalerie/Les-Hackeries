# -*- coding: utf-8 -*-
"""
Created on Feb 2021

Github: https://www.github.com/Mlamalerie

"""


import os
import time
import winsound
from tkinter import filedialog,StringVar
import tkinter

root = tkinter.Tk()
root.withdraw()
root.attributes('-topmost', 1)


def play(fil,rep = 2,wait = 0):
    for x in range(rep):
        if wait > 0:
            time.sleep(wait)
        winsound.PlaySound(fil, winsound.SND_FILENAME)

def stop():
    winsound.PlaySound(None, winsound.SND_PURGE)

#from pydub import AudioSegment
#from scipy.io.wavfile import read

"""
def duration(fil):
    sample_rate_in_s, data = read(fil)
    length = data.shape[0] / sample_rate_in_s
    #print(f"length = {length}s")
    return length
"""
def typeDrum(fil):
    return 'hi'

def ecouter(fil):
    d_type = typeDrum(fil)
    try:
        if d_type == 'hi':
            play(fil)
        elif d_type == 'me':
            play(fil,2,0)
        elif d_type == 'lo':
            play(fil,1,1)
    except:
        print("ecouter error")
        stop()
        



def select_files(orig,i = 0,prof=1,select_dic = {}):
    espace = "  | "*prof
    
    audioext = ['.mp3','.wav','.ogg']

    if os.path.exists(str(orig)):
        listefichiers = os.listdir(orig)
        for fil in listefichiers:
            fil = orig + "\\" + fil
            if os.path.isdir(fil): #si dossier
                print(espace,"---",orig.split("\\")[-1], prof)
                i = select_files(fil,i,prof+1,select_dic)    
            else: # si fichier
                
                
                bay, ext = os.path.splitext(fil)
                if ext in audioext: #si fichier audio
                    print( espace," :",fil.split("\\")[-1])
                    ecouter(fil)
                    
                    
                   
                select_dic[i] = fil
                i+=1
              
       
        return i
    




def browse_button():
    return filedialog.askdirectory()

folder_path = browse_button()

#####################################################
while 1:
    print(folder_path)
    a = select_files(folder_path)
    print(a)
    time.sleep(5)






