#setThrowException(False)
setFindFailedResponse(PROMPT)
#define the logger
Settings.UserLogs = True
Settings.UserLogPrefix = "agbot"
Settings.UserLogTime = True
Debug.setUserLogFile("dx2-bot.log")

#define the counters
gatekeepersAvoided=0
healsAvoided=0
magChestsAvoided=0
floorsChanged=0
floorBossEncountered=0
connectionIssues=0
auraGateEnteredTimes=0
normalBattles=0
socialBattles=0
loopCount=0
#define info method
def printInfo():
    Debug.user("------------------------------------------------------------------------------")
    Debug.user( "auraGateEnteredTimes="+str(auraGateEnteredTimes)+" normalBattles="+str(normalBattles))
    Debug.user( "socialBattles="+str(socialBattles)+" gatekeepersAvoided="+str(gatekeepersAvoided))
    Debug.user( "healsAvoided="+str(healsAvoided)+" floorsChanged="+str(floorsChanged))
    Debug.user( "floorBossEncountered="+str(floorBossEncountered)+" magChestsAvoided="+str(magChestsAvoided))
    
#main bot logic
Debug.user("starting the bot..")
while True:
    loopCount+=1
    Debug.user("running detection loop no: "+str(loopCount))
    printInfo()
    if exists("LeveIExp.png",0):
        click("nextBtn1.png")
        wait("ExpScreen.png",FOREVER)
        click("expScreenNextBtn.png")
        wait("AcquiredScreen.png",FOREVER)
        click("itemScreenNextBtn.png")
        Debug.user("normal battle")
        normalBattles+=1
        continue
    if exists("1540225519391-1.png",0):
        Debug.user("social battle")        
        click("1540225519391-1.png")
        wait("withthisParty.png",FOREVER)
        click("GoWithThisPartySocialBattle.png")
        if exists("SocialBattleExpScreen.png",30):
            click("nextBtn1.png")
        if exists("attack.png",0):
            click("attack.png")
            wait("SocialBattleExpScreen.png",FOREVER)
            click("nextBtn1.png")
        wait("ExpScreen.png",FOREVER)
        click("expScreenNextBtn.png")
        wait("AcquiredScreen.png",FOREVER)
        click("itemScreenNextBtn.png")        
        wait("1540225712595-1.png",FOREVER)
        click("1540225712595-1.png")
        socialBattles+=1
        continue
    if exists("gatekeeper.png",0):
        Debug.user("gatekeeper")        
        click("gatekeeper.png")
        wait("dontFightBtn.png",FOREVER)
        click("dontFightBtn.png")
        wait(1)
        click("ignoreMessage.png")
        gatekeepersAvoided+=1
        continue
    if exists("FloorBossScreen.png",0):
        Debug.user("floor boss battle")        
        floorBossEncountered+=1
        click("Enter.png")
        wait("LeveIExp.png",FOREVER)
        click("nextBtn1.png")
        wait("ExpScreen.png",FOREVER)
        click("expScreenNextBtn.png")
        wait("AcquiredScreen.png",FOREVER)
        click("itemScreenNextBtn.png")
        wait(10)
        if exists("T0nextoor.png"):
            click("Enter-1.png")
            wait(10)
        if exists("AutoMoveBtn.png"):
            click("AutoMoveBtn.png")
            floorsChanged+=1
        continue
    if exists("MaidenoftheSpringScreen.png",0):
        Debug.user("healer")        
        click("lost.png")
        wait(1)
        click("heal.png")
        wait(1)
        click("Leave.png")
        healsAvoided+=1
        continue
    if exists("ItsAMAGchest.png",0):
        Debug.user("mag chest")        
        click("MAG.png")
        wait(2)
        click("Ignore.png")
        wait(1)
        click("ignore-1.png")
        magChestsAvoided+=1
        continue
    if exists("TheAuraGateClosedMsg.png",0):
        Debug.user("ag closed")        
        click("1540224949090-1.png")
        wait("1540224992674-1.png",FOREVER)
        click("1540225008178-1.png")
        continue    
    if exists("1540225947641-1.png",0):
        Debug.user("entering ag")        
        click("1540223058893-1.png")
        wait("1540223140256-1.png",FOREVER)
        click("1540223140256-1.png")
        wait("boostModebtn.png",FOREVER)
        click("boostModebtn.png")
        wait("1540223270060-1.png",FOREVER)
        click("1540223295983-1.png")
        click("1540223356357-1.png")
        wait(10)
        if exists("AutoMoveBtn.png"):
            click("AutoMoveBtn.png")
            auraGateEnteredTimes+=1
        continue
    if exists("1540225798213.png",0):
        Debug.user("connection error")        
        click("greenBtn.png")
        wait(1)
        if exists("AutoMoveBtn.png"):
            click("AutoMoveBtn.png")
            connectionIssues+=1
        continue