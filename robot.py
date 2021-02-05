import os

val = input("Do you want to start your day or close a day 1 for start 2 for close: ")
if val==1:
    os.system("open /Applications/Google\ Chrome.app")
    os.system("open /Applications/ClickUp.app")
    os.system("open /Applications/iTerm.app")
    os.system("open /Applications/Discord.app")
    os.system("open /Applications/Vs.app")
elif val ==2:
    os.system("pkill Chrome")
    os.system("pkill ClickUp")
    os.system("pkill iTerm")
    os.system("pkill Discord")
    os.system("pkill Vs")