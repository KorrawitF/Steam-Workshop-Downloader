from bs4.element import ProcessingInstruction
from pysteamcmdwrapper import SteamCMD, SteamCMDException
from bs4 import BeautifulSoup
import requests
import os.path
import shutil
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog

Global_CMD = ""
Global_Mod = ""

#GUI.
GUI = Tk()
#GUI.iconbitmap(os.path.join(os.getcwd(), 'icon.ico'))
GUI.geometry("320x320")
GUI.minsize(320, 320)
GUI.maxsize(320, 320)
GUI.resizable(0, 0)
GUI.configure(bg = 'white')
GUI.title("Steam Workshop Mod Downloader")

#Mod Queue.
class Queue:
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return True if len(self.queue) == 0 else False
    def First(self):
        if self.isEmpty():
            return "No more order!"
        else:
            Link = self.queue[0]
            self.dequeue()
            return Link
    def Size(self):
        return len(self.queue)
    def enqueue(self, element):
        self.queue.append(element)
        return element
    def dequeue(self):
        self.queue.pop(0)
LinkList = Queue()

iDir = StringVar()
jDir = StringVar()

iLabel = Label(text = "Steamcmd directory.", font = ('Times'), bg = 'white')
iEntry = Entry(GUI, textvariable = iDir, font = ('Times'), bg = 'white')
iLabel.grid(row = 0, column = 0)
iEntry.grid(row = 0, column = 1)

jLabel = Label(text = "Mod store directory.", font = ('Times'), bg = 'white')
jEntry = Entry(GUI, textvariable = jDir, font = ('Times'), bg = 'white')
jLabel.grid(row = 1, column = 0)
jEntry.grid(row = 1, column = 1)

kLabel = Label(text = "Links.", font = ('Times'), bg = 'white')
kLabel.place(relx = 0.0, rely = 0.2, anchor = W)
kEntry = Text(GUI, height = 8, width = 35, bg = "white")
kEntry.place(relx = 0.03, rely = 0.25)
scroll_y = Scrollbar(GUI, orient = "vertical", command = kEntry.yview)
scroll_y.place(relx = 0.92, rely = 0.25, height = 165)
kEntry.configure(yscrollcommand = scroll_y.set)

progress = Progressbar(GUI, orient = HORIZONTAL, length = LinkList.Size(), mode = 'determinate')
progress.place(relx = 0.03, rely = 0.7, width = 284)

def getSteamcmdDir():
    ipath = GUI.filename = filedialog.askdirectory(initialdir = 'C:/', title = "Select Folder")
    iDir.set(ipath+ "/steamcmd")
    global Global_CMD
    Global_CMD = iDir.get()
def getModDir():
    jpath = GUI.filename = filedialog.askdirectory(initialdir = 'C:/', title = "Select Folder")
    jDir.set(jpath+ "/Mod")
    global Global_Mod
    Global_Mod = jDir.get() 
def StateChange():
    if kbutton['state'] == NORMAL:
        kbutton['state'] = DISABLED
    else:
        kbutton['state'] = NORMAL
def Downloading(i):
        progress['value'] += i
        GUI.update_idletasks()
    
#Check if directory existed.
def Check():
    if not os.path.isdir(Global_CMD):
        os.makedirs(Global_CMD)
    if not os.path.isdir(Global_Mod):
        os.makedirs(Global_Mod)
    #Check if steam installed.
    global steam  
    steamcmd = Global_CMD
    steam = SteamCMD(steamcmd)
    try:
        steam.install()
        steam.login('anonymous', '')
        Install()
    except SteamCMDException:
        print("SteamCMD installed")
        steam.login('anonymous', '')
        Install()

#Mod installation.
def Install():
    if LinkList.isEmpty():
        print("Downloading is DONE!")
        return StateChange()
    else:
        ModLink = LinkList.First()
        #Seperate ID from URL.
        ModID = ModLink.split("=", 1)[1]
        #Get mod's name.
        source = requests.get(ModLink)
        Soup = BeautifulSoup(source.text, 'html.parser')
        RealName = Soup.find('div', class_='workshopItemTitle').text
        ModName = "@" + RealName.translate ({ord(c): "-" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        #Download through steamcmd.
        steam.workshop_update(107410, ModID, os.path.join(os.getcwd(), Global_Mod), validate = True)
        #Rename mod file.
        ModID = os.path.join(os.getcwd(), Global_Mod+ '/steamapps/workshop/content/107410/' +ModID)
        ModName = os.path.join(os.getcwd(), Global_Mod+ '/steamapps/workshop/content/107410/' +ModName)
        if os.path.isdir(ModName):
            shutil.rmtree(ModName)
        if os.path.isdir(ModID):
            os.rename(ModID, ModName)
        Downloading(1)
        return Install()
        #End Recursive.

def getText():
    Links = kEntry.get("1.0", "end")
    for i in Links.split(","):
        LinkList.enqueue(i)
    Check()
    StateChange()

ibutton = Button(GUI, text = '...', command = getSteamcmdDir, bg = 'white', cursor = "hand2")
jbutton = Button(GUI, text = '...', command = getModDir, bg = 'white', cursor = "hand2")
kbutton = Button(GUI, text = 'Start', command = getText, height = 3, width = 42, bg = 'white', cursor = 'hand2')
ibutton.grid(row = 0, column = 2)
jbutton.grid(row = 1, column = 2)
kbutton.place(relx = 0.03, rely = 0.8)

GUI.mainloop()
#Complete process.