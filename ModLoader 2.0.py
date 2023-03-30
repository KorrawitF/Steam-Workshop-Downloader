from pysteamcmdwrapper import SteamCMD, SteamCMDException
from bs4 import BeautifulSoup
import requests
import os.path
import shutil
steamcmd = os.path.join(os.getcwd(), "steamcmd")
#Check if steam installed.
steam = SteamCMD(steamcmd)
try:
    steam.install()
except SteamCMDException:
    print("SteamCMD installed")
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
    def enqueue(self, element):
        self.queue.append(element)
        return element
    def dequeue(self):
        self.queue.pop(0)
LinkList = Queue()

#Mod installation.
def Install():
    if LinkList.isEmpty():
        return "Downloading is DONE!"
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
        steam.workshop_update(107410, ModID, os.path.join(os.getcwd(), "Mod"), validate = True)
        #Rename mod file.
        ModID = os.path.join(os.getcwd(), 'Mod/steamapps/workshop/content/107410/' +ModID)
        ModName = os.path.join(os.getcwd(), 'Mod/steamapps/workshop/content/107410/' +ModName)
        if os.path.isdir(ModName):
            shutil.rmtree(ModName)
        if os.path.isdir(ModID):
            os.rename(ModID, ModName)
        return Install()
        #End Recursive.

#Function call.

Links = input("Enter links here seperate by comma e.g(Link1, Link2): ")
for i in Links.split(","):
    LinkList.enqueue(i)
Install()
#Complete process.
print()
print()
input("Press any key to continue...")