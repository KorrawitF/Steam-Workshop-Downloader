
@echo off
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[0]="@NOTHING"
set Mod[0]=#
set ModDownload[0]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[1]="@A3 Thermal Improvement"
set Mod[1]=2041057379
set ModDownload[1]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[2]="@Align"
set Mod[2]=903134884
set ModDownload[2]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[3]="@BettIR (Legacy v0.2.1)"
set Mod[3]=2260572637
set ModDownload[3]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[4]="@USP Gear & Uniforms AIO"
set Mod[4]=1795825073
set ModDownload[4]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[5]="@Ctab Devastator Edition"
set Mod[5]=2189592034
set ModDownload[5]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[6]="@FRXA's TFAR Extra Retextured Equipment"
set Mod[6]=1606874412
set ModDownload[6]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[7]="@Immerse"
set Mod[7]=825172265
set ModDownload[7]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[8]="@LAMBS_Danger.fsm"
set Mod[8]=1858075458
set ModDownload[8]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[9]="@No More Aircraft Bouncing"
set Mod[9]=1770265310
set ModDownload[9]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[10]="@RHS AirPlanes Sound Improve"
set Mod[10]=2162043396
set ModDownload[10]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[11]="@Specialist Military Arms (SMA) Version 2.7.1"
set Mod[11]=699630614
set ModDownload[11]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[12]="@Tier One Weapons"
set Mod[12]=2268351256
set ModDownload[12]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[13]="@TMR"
set Mod[13]=2391439546
set ModDownload[13]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[14]="@Gulfcoast Islands"
set Mod[14]=1617004814
set ModDownload[14]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[15]="@UMB Colombia"
set Mod[15]=2266710560
set ModDownload[15]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[16]="@Interiors for CUP"
set Mod[16]=1883956552
set ModDownload[16]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[17]="@Kujari"
set Mod[17]=1726494027
set ModDownload[17]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[18]="@Lingor/Dingor Island"
set Mod[18]=718649903
set ModDownload[18]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[19]="@Saint Kapaulio"
set Mod[19]=939686262
set ModDownload[19]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[20]="@F/A-18E/F Super Hornet 2020"
set Mod[20]=2131302796
set ModDownload[20]=false
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[21]="@FIREWILL Aviation Pack (Complete)"
set Mod[21]=1381545544
set ModDownload[21]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[22]="@Laghisola"
set Mod[22]=2175069333
set ModDownload[22]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[23]="@kerama Islands By [Vétérans"
set Mod[23]=682140680
set ModDownload[23]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[24]="@LAMBS_RPG"
set Mod[24]=1858070328
set ModDownload[24]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[25]="@LAMBS_Suppression"
set Mod[25]=1808238502
set ModDownload[25]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[26]="@LAMBS_Turrets"
set Mod[26]=1862208264
set ModDownload[26]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[27]="@Tembelan Island"
set Mod[27]=1252091296
set ModDownload[27]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[28]="@Porquerolles Island By [Vétérans]"
set Mod[28]=639497064
set ModDownload[28]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[29]="@Moe Pilot Gear Suite"
set Mod[29]=2127190744
set ModDownload[29]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[30]="@Royal Thai Armed Forces"
set Mod[30]=942955156
set ModDownload[30]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[31]="@Splendid Smoke"
set Mod[31]=770418577
set ModDownload[31]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
set ModName[32]="@#NOTHING"
set Mod[32]=#
set ModDownload[32]=false

:::::::::::::::::::::::::::::::::::::::::::::::::::::::

echo ModLoader is starting...

set "steamcmdpath=C:\Users\flooc\Downloads\steamcmd"
set "steamapppath=C:\Users\flooc\Downloads\Mod"

set /p login=Steam Login: 
echo.
set /p pass=Steam Pass: 
echo.

set "x=0"

:SymLoop
if defined Mod[%x%] (
if defined ModDownload[%x%] (
if defined ModName[%x%] (
cls
call set "name=%%ModName[%x%]%%"
call set "id=%%Mod[%x%]%%"
call set "downloads=%%ModDownload[%x%]%%"
if "%downloads%"=="true" (
cls
echo Downloading the Mod: %name% - ID: %id%
echo.
echo.
%steamcmdpath%\steamcmd +login %login% %pass% +"force_install_dir %steamapppath%" +"workshop_download_item 322330 %id%" +quit
set /a "x+=1"
GOTO :SymLoop
)
)
)