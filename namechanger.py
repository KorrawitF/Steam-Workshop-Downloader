import os
import json
path = "C:/Users/flooc/Downloads/fake mod"
data = '{"2283985516":"@15th Malaya Regiment Training Ground", "2041057379":"@A3 Thermal Improvement", "903134884":"@Align", "2260572637":"@BettIR (Legacy v0.2.1)", "1795825073":"@USP Gear & Uniforms AIO", "2189592034":"@Ctab Devastator Edition", "1606874412":"@FRXAs TFAR Extra Retextured Equipment", "825172265" :"@Immerse", "1858075458":"@LAMBS_Danger.fsm", "1770265310":"@No More Aircraft Bouncing", "2162043396":"@RHS AirPlanes Sound Improve", "699630614":"@Specialist Military Arms (SMA) Version 2.7.1", "2268351256":"@Tier One Weapons", "2391439546":"@TMR", "1617004814":"@Gulfcoast Islands", "2266710560":"@UMB Colombia", "1883956552":"@Interiors for CUP", "1726494027":"@Kujari", "718649903":"@Lingor/Dingor Island", "939686262":"@Saint Kapaulio", "2131302796":"@F/A-18E/F Super Hornet 2020", "1381545544":"@FIREWILL Aviation Pack (Complete)", "2175069333":"@Laghisola", "682140680":"@kerama Islands By [Vétérans", "1858070328":"@LAMBS_RPG", "1808238502":"@LAMBS_Suppression", "1862208264":"@LAMBS_Turrets", "1252091296":"@Tembelan Island", "639497064":"@Porquerolles Island By [Vétérans]", "2127190744":"@Moe Pilot Gear Suite", "942955156":"@Royal Thai Armed Forces", "770418577":"@Splendid Smoke"}'
files = os.listdir(path)

name = json.loads(data)

noffiles = len(files)
x = 0
def rename(n):
    if n <= noffiles-1:
        if files[n] in name:
            os.chdir(path)
            folder = str(files[n])
            showname = str(name[files[n]])
            os.rename(folder, showname)
            return rename(n+1)
        else:
            print(files[n] + ' is not exist!')
            return rename(n+1)
    else:
        return
rename(x)


