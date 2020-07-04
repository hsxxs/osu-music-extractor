def locate(d,outputdir):
    import os

    name_l = os.listdir(d)
    size_l = []
    mp3 = []

    for i in name_l:
        i = d + "/" + i
        if os.path.isdir(i):
            continue
        if i[len(i)-4:len(i)] != ".mp3" or os.path.getsize(i) < 307200:
            continue
        mp3.append(i)
        size_l.append(os.path.getsize(i))
    
    if mp3 == []:
        return(False)

    return(mp3[size_l.index(max(size_l))])


#import getpass
import os
import shutil
import tkinter
from tkinter import filedialog

title_artist = True

#default_output_directory = "C:/Users/{}/AppData/Local/osu!/Songs".format(getpass.getuser())
#default_output_directory = os.path.expanduser("~/AppData/Local/osu!/Songs")

root = tkinter.Tk()
root.withdraw()

inputdir = filedialog.askdirectory(title = "Select the \"Songs\" Folder.",initialdir = os.path.expanduser("~/AppData/Local/osu!/Songs"))
if inputdir == "":
    exit()

#inputdir = "C:/Users/{}/AppData/Local/osu!/Songs".format(getpass.getuser())
outputdir = filedialog.askdirectory(title = "Select a output Folder.")
if outputdir == "":
    exit()

print("Inputdir:  " + inputdir)
print("Outputdir: " + outputdir)
print("Press Enter to start.")
input()

in_l = []
out_l = []

for song in os.listdir(inputdir):
    now = inputdir + "/" + song
    print("Scanning " + now)

    if os.path.isfile(now):
        print(now + " isn't a directory. Skipped.\n")
        continue

    found = locate(now,outputdir)
    if found == False:
        print("Nothing found in " + now + ". Skipped.\n")
        continue
    
    name = song
    try:
        if ord(song[:1]) in range(48,58):
            name = name[name.index(" ")+1:]
        if title_artist:
            name = name[name.index(" - ") + 3:] + " - " + name[:name.index(" - ")] + ".mp3"
        
        print(song)
        print(name)
    except BaseException:
        print("Error when processing the name. Skipped.")
        continue
        
    if os.path.isfile(outputdir + "/" + name):
        print(outputdir + "/" + name + " already exists. Skipped.\n")
        continue

    print("\n")

    in_l.append(found)
    out_l.append(outputdir + "/" + name)

for i in range(len(in_l)):
    print("From: " + in_l[i])
    print("To:   " + out_l[i])
    shutil.copy(in_l[i],out_l[i])
    print("Copied.\n")
