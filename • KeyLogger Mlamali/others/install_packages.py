import os
import subprocess
os.system("python -m pip install --upgrade pip")

commandinstall = "pip install "


listes = ["pynput","pyautogui","smtplib","email"]

#listes2 = ["PyDrive"]


for mod in listes2:
	os.system(commandinstall + mod)
